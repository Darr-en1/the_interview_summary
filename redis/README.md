redis知识图谱
![redis知识图谱](redis.png)

### Redis数据结构的底层实现

redis的数据类型 8种

前五种类型:String、list、hash、set、zet

后三种类型分别是:
- bitmap（或简称位图）：使用特殊命令可以处理字符串值，如位数组：您可以设置和清除各个位，将所有位设置为1，查找第一个位或未设置位，等等。
- HyperLogLogs：这是一个概率数据结构，用于估计集合的基数。不要害怕，它比看起来更简单。
- Streams：仅附加的类似于地图的条目集合，提供抽象日志数据类型。

查看key对应value的数据结构  `object encoding key_name`

***Srring***

string长度不可超过512M

符串是可以修改的，在底层它是以字节数组的形式存在的。Redis中的字符串被称为简单动态字符串「SDS」，这种结构很像Java中的ArrayList，其长度是动态可变的.

redis的数据存储过程中为了提高性能，内部做了很多优化。string 内部还被拆分成三中编码:

int编码: 存储字符串长度小于20且能够转化为整数的字符串

embstr编码: 保存长度小于44字节的字符串(redis3.2版本之前是39字节，之后是44字节)

raw编码: 保存长度大于44字节的字符串(redis3.2版本之前是39字节，之后是44字节)

编码转换

int->raw

条件：数字对象进行append字母，就会发生转换。

embstr->raw

条件：对embstr进行修改，redis会先将其转换成raw，然后才进行修改。所以embstr实际上是只读性质的。

embstr和raw都是由redisObject和sds组成的。不同的是：embstr的redisObject和sds是连续的，只需要使用 malloc 分配一次内存；而raw需要为redisObject和sds分别分配内存，即需要分配两次内存。

所有相比较而言，embstr少分配一次内存，更方便。但embstr也有明显的缺点：如要增加长度，redisObject和sds都需要重新分配内存。

[https://darr-en1.github.io/2020/03/25/1/](https://darr-en1.github.io/2020/03/25/1/)

***List***

Redis中的列表对象在版本3.2之前，列表底层的编码是ziplist和linkedlist实现的，但是在版本3.2之后，重新引入了一个 quicklist 的数据结构，列表的底层都由quicklist实现。


编码转换

ziplist->linkedlist

条件：列表对象的所有字符串元素的长度大于等于64字节 & 列表元素数大于等于512. 反之，小于64和小于512会使用ziplist而不是用linkedlist。

这个阈值是可以修改的，修改选项：list-max-ziplist-value和list-max-ziplist-entriess



ziplist结构：

zlbytes：表示ziplist占用字节数，在执行resize操作时使用

zltail：表示最后节点的偏移量，也是避免了整体遍历list

zllen：表示ziplist节点个数（节点数超过65535,zllen字段值无效,需要遍历才能得到真实数量）

zlend：表示ziplist结束的标识符

![ziplist的基本结构](ziplist.png)

ziplist Entry节点数据结构（抽象）：
每个压缩列表节点都由previous_entry_length、encoding、content三个部分组成（不是指实际结构体的字段）

previous_entry_length：前一个节点的长度，用来由后向前遍历，根据前一个节点的长度，可能需要一个或五个字节。

encoding：记录节点保存的数据类型和数据长度。

content：节点保存的数据内容。

![ziplist_entry的基本结构](ziplist_entry.png)

这两种存储方式的优缺点

- 双向链表linkedlist便于在表的两端进行push和pop操作，在插入节点上复杂度很低，但是它的内存开销比较大。首先，它在每个节点上除了要保存数据之外，还要额外保存两个指针,单个指针8个字节；其次，双向链表的各个节点是单独的内存块，地址不连续，节点多了容易产生内存碎片。
- ziplist存储在一段连续的内存上，所以存储效率很高。但是，它不利于修改操作，插入和删除操作需要频繁的申请和释放内存。特别是当ziplist长度很长的时候，一次realloc可能会导致大批量的数据拷贝。

`list-max-ziplist-size` 表示按照数据项个数来限定每个quicklist节点上的ziplist长度
 quicklist 默认的压缩深度是 0，也就是不压缩。压缩的实际深度由配置参数`list-compress-depth`决定。为了支持快速的 push/pop 操作，quicklist 的首尾两个 ziplist 不压缩，此时深度就是 1。如果深度为 2，表示 quicklist 的首尾第一个 ziplist 以及首尾第二个 ziplist 都不压缩。

Redis对于quicklist内部节点的压缩算法，采用的LZF——一种无损压缩算法。

[https://juejin.im/post/5df9df506fb9a0160b6380f5](https://juejin.im/post/5df9df506fb9a0160b6380f5)

[https://throwsnew.com/2017/09/12/%E4%B8%BA%E4%BB%80%E4%B9%88Redis%E4%BD%BF%E7%94%A8ziplist%E8%83%BD%E8%8A%82%E7%9C%81%E5%86%85%E5%AD%98/](https://throwsnew.com/2017/09/12/%E4%B8%BA%E4%BB%80%E4%B9%88Redis%E4%BD%BF%E7%94%A8ziplist%E8%83%BD%E8%8A%82%E7%9C%81%E5%86%85%E5%AD%98/)

***Hash***

哈希对象的编码有:ziplist和hashtable

编码转换：ziplist->hashtable

条件：哈希对象所有键和值字符串长度大于等于64字节 & 键值对数量大于等于512

这个阈值也是可以修改的，修改选项：hash-max-ziplist-value和hash-max-ziplist-ent

链地址法解决哈希冲突的问题。

redis中的Hash 结构内部包含两个 hashtable，通常情况下只有一个 hashtable 是有值的。但是在 dict 扩容缩容时，需要分配新的 hashtable，然后进行渐进式搬迁，这时两个 hashtable 存储的分别是旧的 hashtable 和新的 hashtable。待搬迁结束后，旧的 hashtable 被删除，新的 hashtable 取而代之。

渐进式rehash

字典的rehash操作数据量过大时并不是一次完成,而是分批次逐渐进行

rehash过程中新插入字典数据放在[1]哈希表中,并将原[0]中数据重新进行hash计算加入[1]中。读操作将会读取[0]、[1]两个哈希表

rehash过程标志使用dict中属性rehashidx标识

rehash采用cow写时复制技术

***Set***

集合对象的编码有：intset和hashtable

intset:集合对象所有元素都是整数,集合对象元素数不超过512个

编码转换:intset->hashtable

条件：元素不都是整数 & 元素数大于等于512

整数集合特点
- 内容全是数字
- 内存连续
- 元素有序,不可重复

intset底层实现为有序、无重复数的数组。 intset的整数类型可以是16位的、32位的、64位的。如果数组里所有的整数都是16位长度的，新加入一个32位的整数，那么整个16的数组将升级成一个32位的数组。升级可以提升intset的灵活性，又可以节约内存，但不可逆。

***Zset***

它的底层是ziplist（压缩列表）或   skiplist （跳跃表）。

编码转换:ziplist->skiplist

条件：有序集合元素数 >= 128 & 含有元素的长度 >= 64

这个阈值也是可以修改的，修改选项：**zset-max-ziplist-value**和**zset-max-ziplist-entries**

ziplist编码的有序集合使用紧挨在一起的压缩列表节点来保存，第一个节点保存member，第二个保存score。ziplist内的集合元素按score从小到大排序，score较小的排在表头位置。

skiplist不要求上下相邻两层链表之间的节点个数有严格的对应关系，而是为每个节点随机出一个层数(level)

简单分析一下几个查询命令：
- zrevrank由数据查询它对应的排名，这在前面介绍的skiplist中并不支持。
- zscore由数据查询它对应的分数，这也不是skiplist所支持的。
- zrevrange根据一个排名范围，查询排名在这个范围内的数据。这在前面介绍的skiplist中也不支持。
- zrevrangebyscore根据分数区间查询数据集合，是一个skiplist所支持的典型的范围查找（score相当于key，数据相当于value）。

如果只用ziplist来实现，无法做到元素的排序，不支持范围查找，能做到元素的快速查找。

如果只用skiplist来实现，无法做到快速查找，但能做到元素排序、范围操作。

Redis中sorted set的实现是这样的：

当数据较少时，sorted set是由一个ziplist来实现的。

当数据多的时候，sorted set是由一个**dict + 一个skiplist**来实现的。简单来讲，dict用来查询数据到分数的对应关系，而skiplist用来根据分数查询数据（可能是范围查找）。

看一下sorted set与skiplist的关系，：

- zscore的查询，不是由skiplist来提供的，而是由那个dict来提供的。
- 为了支持排名(rank)，Redis里对skiplist做了扩展，使得根据排名能够快速查到数据，或者根据分数查到数据之后，也同时很容易获得排名。而且，根据排名的查找，时间复杂度也为O(log n)。
- zrevrange的查询，是根据排名查数据，由扩展后的skiplist来提供。
- revrank是先在dict中由数据查到分数，再拿分数到skiplist中去查找，查到后也同时获得了排名。

总结起来，Redis中的skiplist跟前面介绍的经典的skiplist相比，有如下不同：

- 分数(score)允许重复，即skiplist的key允许重复。这在最开始介绍的经典skiplist中是不允许的。
- 在比较时，不仅比较分数（相当于skiplist的key），还比较数据本身。在Redis的skiplist实现中，数据本身的内容唯一标识这份数据，而不是由key来唯一标识。另外，当多个元素分数相同的时候，还需要根据数据内容来进字典排序。
- 第1层链表不是一个单向链表，而是一个双向链表。这是为了方便以倒序方式获取一个范围内的元素。
- 在skiplist中可以很方便地计算出每个元素的排名(rank)。

[https://zsr.github.io/2017/07/03/redis-zset%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0/](https://zsr.github.io/2017/07/03/redis-zset%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0/)

***Stream***
[https://erpeng.github.io/2019/04/30/Redis-stream/](https://erpeng.github.io/2019/04/30/Redis-stream/)

[https://juejin.im/post/5ecc8cfa6fb9a047f6103f8f?utm_source=gold_browser_extension#heading-18](https://juejin.im/post/5ecc8cfa6fb9a047f6103f8f?utm_source=gold_browser_extension#heading-18)

###基于REDIS实现延时任务

rabbitmq 可以通过死信队列实现

python 中 celery 可以实现定时任务

前两者不可以修改定时时间

redis可以使用zset实现，可以修改定时时间

[https://juejin.im/post/5caf45b96fb9a0688b573d6c](https://juejin.im/post/5caf45b96fb9a0688b573d6c)

### Redis持久化

[https://juejin.im/post/5b70dfcf518825610f1f5c16](https://juejin.im/post/5b70dfcf518825610f1f5c16)

### Redis的ZSET做排行榜时,如果要实现分数相同时按时间顺序排序怎么实现

[https://blog.csdn.net/zeus_9i/article/details/51025175](https://blog.csdn.net/zeus_9i/article/details/51025175)

### 限流(漏桶算法、令牌桶算法)

[https://www.jianshu.com/p/c02899c30bbd](https://www.jianshu.com/p/c02899c30bbd)

[https://zhuanlan.zhihu.com/p/34762016](https://zhuanlan.zhihu.com/p/34762016)

### Redis主从同步过程

[https://juejin.im/post/5d80ac83e51d45620821cf87](https://juejin.im/post/5d80ac83e51d45620821cf87)

### Redis如何实现高可用

[https://juejin.im/post/5db3f7b5e51d4529ed2918df#heading-18](https://juejin.im/post/5db3f7b5e51d4529ed2918df#heading-18)

### Redis key的过期策略

Redis采用的是 定期删除 和 惰性删除 的内存淘汰机制。

Redis的内存淘汰机制
![Redis的内存淘汰机制](out_of_memory.png)

### Redis6.0

[https://www.cnblogs.com/mr-wuxiansheng/p/12884356.html](https://www.cnblogs.com/mr-wuxiansheng/p/12884356.html)
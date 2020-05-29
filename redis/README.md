redis知识图谱
![redis知识图谱](redis.png)

1.redis数据结构的底层实现

redis的数据类型 8种

前五种类型:String、list、hash、set、zet

后三种类型分别是:
- bitmap（或简称位图）：使用特殊命令可以处理字符串值，如位数组：您可以设置和清除各个位，将所有位设置为1，查找第一个位或未设置位，等等。
- HyperLogLogs：这是一个概率数据结构，用于估计集合的基数。不要害怕，它比看起来更简单。
- Streams：仅附加的类似于地图的条目集合，提供抽象日志数据类型。

查看key对应value的数据结构  `object encoding key_name`

***Srring***

符串是可以修改的，在底层它是以字节数组的形式存在的。Redis中的字符串被称为简单动态字符串「SDS」，这种结构很像Java中的ArrayList，其长度是动态可变的.

redis的数据存储过程中为了提高性能，内部做了很多优化。string 内部还被拆分成三中编码:

int编码: 存储字符串长度小于20且能够转化为整数的字符串

embstr编码: 保存长度小于44字节的字符串(redis3.2版本之前是39字节，之后是44字节)

raw编码: 保存长度大于44字节的字符串(redis3.2版本之前是39字节，之后是44字节)


[https://darr-en1.github.io/2020/03/25/1/](https://darr-en1.github.io/2020/03/25/1/)

[https://juejin.im/post/5ecc8cfa6fb9a047f6103f8f?utm_source=gold_browser_extension#heading-18](https://juejin.im/post/5ecc8cfa6fb9a047f6103f8f?utm_source=gold_browser_extension#heading-18)

2.基于REDIS实现延时任务

[https://juejin.im/post/5caf45b96fb9a0688b573d6c](https://juejin.im/post/5caf45b96fb9a0688b573d6c)

3.

4.Redis 的 ZSET 做排行榜时，如果要实现分数相同时按时间顺序排序怎么实现？

5.让你设计一个限流的系统怎么做？ 漏桶算法、令牌桶算法

6.redis 持久化有哪几种方式

7.redis 主从同步是怎样的过程？

8.redis如何实现高可用

9.redis key 的过期策略

Redis采用的是 定期删除 和 惰性删除 的内存淘汰机制。

Redis的内存淘汰机制
![Redis的内存淘汰机制](out_of_memory.png)
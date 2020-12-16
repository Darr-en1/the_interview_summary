### MySQL事务的四个隔离级别

|级别	| symbol	|值|	描述|
|  ----   |  ----   |  ----   |  ----   |
|读未提交	|READ-UNCOMMITTED	|0	|存在脏读、不可重复读、幻读的问题|
|读已提交	|READ-COMMITTED	|1	|解决脏读的问题，存在不可重复读、幻读的问题|
|可重复读	|REPEATABLE-READ	|2	|mysql 默认级别，解决脏读、不可重复读的问题，存在幻读的问题。使用 MMVC机制 实现可重复读|
|序列化	|SERIALIZABLE	|3	|解决脏读、不可重复读、幻读，可保证事务安全，但完全串行执行，性能最低|

MySQL的默认隔离级别就是Repeatable,Oracle postgresql 默认Read committed

 查看数据库隔离级别 `show variables like 'transaction_isolation';`

[https://segmentfault.com/a/1190000016566788](https://segmentfault.com/a/1190000016566788)

[https://www.cnblogs.com/jycboy/p/transaction.html](https://www.cnblogs.com/jycboy/p/transaction.html)

### Binlog日志和redolog日志,两个日志的作用以及两阶段提交

redolog是对记录修改之后的物理日志，物理日志就是说redolog保存的是某一行数据修改之后的值，比如把id=1这行的某个属性由1改成2，redolog记录的就是这个2.redolog是InnoDB引擎层的。

相比于redolog，binlog是逻辑日志。其中一种形式是记录的原始sql语句，比如update t set c = c +1 where id = 1; binlog是数据库server层的。

知识点： 
- redo log , undo log , bin log  
- crash safe
- wal 机制
- 两阶段提交

[MySQL 的 crash-safe 原理解析](https://juejin.im/post/6844904167782236167)

### Mysql存储引擎及区别

MyISAM  
非聚集索引
MyISAM可以没有主键

InnoDB 
聚集索引
要求表必须有主键

[https://blog.csdn.net/zgrgfr/article/details/74455547](https://blog.csdn.net/zgrgfr/article/details/74455547)

### Mysql索引在什么情况下会失效

[https://juejin.im/post/5ec15ab9f265da7bc60e1910?utm_source=gold_browser_extension](https://juejin.im/post/5ec15ab9f265da7bc60e1910?utm_source=gold_browser_extension)

[https://juejin.im/post/5de99dd2518825125e1ba49d](https://juejin.im/post/5de99dd2518825125e1ba49d)

### Mysql索引模型

**常见的索引模型**
- 有序数组
- 哈希表
- 二叉搜索树
- B-Tree
- B+Tree

[https://blog.csdn.net/weixin_42462202/article/details/104335419](https://blog.csdn.net/weixin_42462202/article/details/104335419)

[https://blog.csdn.net/Abysscarry/article/details/80792876](https://blog.csdn.net/Abysscarry/article/details/80792876)

### 乐观锁与悲观锁的区别

[https://juejin.im/post/5b4977ae5188251b146b2fc8](https://juejin.im/post/5b4977ae5188251b146b2fc8)

### Mysql日志系统

redo log（重做日志）: 引擎层 InnoDB引擎特有的日志

binlog（归档日志）: Server层 mysql 通用日志,所有引擎都可以使用

两阶段提交

先写redo log后写binlog。假设在redo log写完，binlog还没有写完的时候，MySQL进程异常重启。由于我们前面说过的，redo log写完之后，系统即使崩溃，仍然能够把数据恢复回来，所以恢复后这一行c的值是1。
但是由于binlog没写完就crash了，这时候binlog里面就没有记录这个语句。因此，之后备份日志的时候，存起来的binlog里面就没有这条语句。
然后你会发现，如果需要用这个binlog来恢复临时库的话，由于这个语句的binlog丢失，这个临时库就会少了这一次更新，恢复出来的这一行c的值就是0，与原库的值不同。

先写binlog后写redo log。如果在binlog写完之后crash，由于redo log还没写，崩溃恢复以后这个事务无效，所以这一行c的值是0。但是binlog里面已经记录了“把c从0改成1”这个日志。所以，在之后用binlog来恢复的时候就多了一个事务出来，恢复出来的这一行c的值就是1，与原库的值不同。

[https://www.cnblogs.com/wupeixuan/p/11734501.html](https://www.cnblogs.com/wupeixuan/p/11734501.html)


### MySQL如何分析一条语句的执行过程。delete from t1 limit 3和delete from t1的区别

连接器： 身份认证和权限相关(登录 MySQL 的时候)。

查询缓存: 执行查询语句的时候，会先查询缓存（MySQL 8.0 版本后移除，因为这个功能不太实用）。

分析器: 没有命中缓存的话，SQL 语句就会经过分析器，分析器说白了就是要先看你的 SQL 语句要干嘛，再检查你的 SQL 语句语法是否正确。

优化器： 按照 MySQL 认为最优的方案去执行。

执行器: 执行语句，然后从存储引擎返回数据。

[https://blog.csdn.net/weter_drop/article/details/93386581](https://blog.csdn.net/weter_drop/article/details/93386581)

delete from t1 limit 3和delete from t1的区别: 只删除先找到的三行


### 普通索引与唯一索引

[https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase](https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)


### buffer pool
[https://www.cnblogs.com/myseries/p/11307204.html](https://www.cnblogs.com/myseries/p/11307204.html)

### Changebuffer

 change buffer也是可以持久化的，change buffer在内存中有拷贝，也会被写入磁盘中。将change buffer中的操作应用到原数据页，得到最新结果的过程称为merge。触发持久化merge的操作：

1、访问这个数据页会触发merge外

2、系统有后台线程会定期merge进行持久化

3、在数据库正常关闭（shutdown）的过程中，也会执行merge操作。





以下几种情况开启 Change Buffer，会使得 MySQL 数据库明显提升：

1、数据库大部分是非唯一索引:对于唯一索引来说，所有的更新操作都要先判断这个操作是否违反唯一性约束。要判断表中是否存在这个数据，而这必须要将数据页读入内存才能判断，如果都已经读入到内存了，那直接更新内存会更快，就没必要使用change buffer了。

2、业务是写多读少

3、写入数据之后并不会立即读取它

[https://blog.csdn.net/sayoko06/article/details/90258189](https://blog.csdn.net/sayoko06/article/details/90258189)

[https://www.cnblogs.com/jamaler/p/12371205.html](https://www.cnblogs.com/jamaler/p/12371205.html)

### 单列索引和联合索引

[https://blog.csdn.net/Abysscarry/article/details/80792876](https://blog.csdn.net/Abysscarry/article/details/80792876)

### MVCC
(Multi-Version Concurrency Control)

undo log:撤回日志记录,也称版本链。当前事务未提交之前，undo log保存了当前事务的正在操作的数据记录的所有版本的信息，undo log中的数据可作为数据旧版本快照供其他并发事务进行快照读

read_view的更新方式：

注意：仅分析RC级别和RR级别，因为MVCC不适用于其它两个隔离级别。

a、对于Read Committed级别的：

基本描述：每次执行select都会创建新的read_view，更新旧read_view，保证能读取到其他事务已经COMMIT的内容（读提交的语义）；

详细分析：假设当前有事务A和事务A+1并发进行。在当前级别下，事务A每次select的时候会创建新的read_view，此时可以简单理解为事务A会提交，也就是让事务A执行完毕，然后创建一个新的事务比如是事务A+2。这样子的话，因为事务A+2的事务ID肯定是比事务A+1的ID大，所以就能够读取到事务A+1的更新了。那么便可以读取到在创建这个新的read_view之前事务A+1所提交的所有信息。这是RC级别下能读取到其他事务已经COMMIT的内容的原因所在。
b、对于Repeatable Read级别的：

第一次select时更新这个read_view，以后不会再更新，后续所有的select都是复用这个read_view。所以能保证每次读取的一致性，即都是读取第一次读取到的内容（可重复读的语义）。

注意：通过对read view的更新方式的分析可以得出：对于InnoDB下的MVCC来说，RR虽然比RC隔离级别高，但是开销反而相对少（因为不用频繁更新read_view）。


[MVCC--多版本并发控制机制](https://www.cnblogs.com/axing-articles/p/11415763.html)



### explain

condition,Using index,Using where)Extra(Using where,Using index,Using index 


### ICP 索引下推

[https://coderbee.net/index.php/db/20190718/1901](https://coderbee.net/index.php/db/20190718/1901)

### MySQL表锁和行锁

MySQL里面表级别的锁有两种：一种是表锁，一种是元数据锁（meta data lock，MDL)。


MDL锁的全称为Meta data lock，是在MySQL中sql层实现的锁，从其名字可以看出来，
它的作用主要是为了保护元数据的访问。而在MySQL中，元数据就是指如schema，
table，function这样的对象的元数据信息（如表名，表的列，列的属性等等）。

在MySQL 5.5版本中引入了MDL，**当对一个表做增删改查操作的时候，加MDL读锁**；
**当要对表做结构变更操作的时候，加MDL写锁**。

读锁之间不互斥，因此你可以有多个线程同时对一张表增删改查。

读写锁之间、写锁之间是互斥的，用来保证变更表结构操作的安全性。因此，如果有两个线程要同时给一个表加字段，其中一个要等另一个执行完才能开始执行。

**申请MDL锁的操作会形成一个队列，队列中写锁获取优先级高于读锁。一旦出现写锁等待，不但当前操作会被阻塞，同时还会阻塞后续该表的所有操作。**事务一旦申请到MDL锁后，直到事务执行完才会将锁释放。

**如何安全地给小表加字段？**

首先我们要解决长事务，事务不提交，就会一直占着MDL锁。在MySQL的information_schema 库的 innodb_trx 表中，你可以查到当前执行中的事务。如果你要做DDL变更的表刚好有长事务在执行，要考虑先暂停DDL，或者kill掉这个长事务。

但考虑一下这个场景。如果你要变更的表是一个热点表，虽然数据量不大，但是上面的请求很频繁，而你不得不加个字段，你该怎么做呢？

这时候kill可能未必管用，因为新的请求马上就来了。比较理想的机制是，在alter table语句里面设定等待时间，如果在这个指定的等待时间里面能够拿到MDL写锁最好，拿不到也不要阻塞后面的业务语句，先放弃。之后开发人员或者DBA再通过重试命令重复这个过程。

Online DDL
[MySQL InnoDB Online DDL学习](https://www.cnblogs.com/dbabd/p/10381942.html)


myisam 只支持表锁 : 读共享读锁，写锁

当一个线程获取到表级写锁后，只能由该线程对表进行读写操作，别的线程必须等待该线程释放锁以后才能操作
当一个线程获取到表级读锁后，该线程只能读取数据不能修改数据，其它线程也只能加读锁，不能加写锁

InnoDB支持行锁和表锁，默认启用行锁:

行锁的有两种锁模式：

S锁（共享锁）：不同事务之间的S锁互不排斥，也即是一个事务对某行加了S锁后，其它事务依然可以对该行加S锁进行访问。

X锁（排他锁）：不同事务之间的X锁相互排斥，即一个事务对某行加了X锁后，其它事务不能对该行再加X锁。

在InnoDB行锁中，又分为几种不同类型行锁。

Record锁：锁定某行记录，在行的索引上加锁。

Gap锁：锁定某个区间，即某个索引的范围区间内加锁，不包含边界行。locking reads，UPDATE和DELETE时，除了对唯一索引的唯一搜索外都会获取gap锁或next-key锁。即锁住其扫描的范围。

Next-key锁：同时锁住某行记录和一个区间，上界为开区间，下界为闭区间。




[MySQL 表锁和行锁机制](https://juejin.im/entry/5a55c7976fb9a01cba42786f)

### 共享锁与排他锁
读锁（S锁，共享锁）和写锁（X锁，排他锁）。


Innodb的锁定模式实际上可以分为四种：共享锁（S），排他锁（X），意向共享锁（IS）和意向排他锁（IX）

SELECT … LOCK IN SHARE MODE 在读取的行上设置一个共享锁，其他的session可以读这些行，
但在你的事务提交之前不可以修改它们。如果这些行里有被其他的还没有提交的事务修改，你的查询会等到那个事务结束之后使用最新的值。

索引搜索遇到的记录，SELECT … FOR UPDATE 会锁住行及任何关联的索引条目，
和你对那些行执行 update 语句相同。其他的事务会被阻塞在对这些行执行 update 操作，
获取共享锁，或从某些事务隔离级别读取数据等操作。一致性读(Consistent Nonlocking Reads)会忽略在读取视图上的记录的任何锁。（旧版本的记录不能被锁定；它们通过应用撤销日志在记录的内存副本上时被重建。）

所有被共享锁和排他锁查询所设置的锁都会在**事务提交或者回滚**之后被释放。

总结

SELECT … LOCK IN SHARE MODE ：共享锁(S锁, share locks)。其他事务可以读取数据，但不能对该数据进行修改，直到所有的共享锁被释放。

如果事务对某行数据加上共享锁之后，可进行读写操作；其他事务可以对该数据加共享锁，但不能加排他锁，且只能读数据，不能修改数据。

SELECT … FOR UPDATE：排他锁(X锁, exclusive locks)。如果事务对数据加上排他锁之后，则其他事务不能对该数据加任何的锁。获取排他锁的事务既能读取数据，也能修改数据。

**注：普通 select 语句默认不加锁，而CUD操作默认加排他锁。**

 
#### 总结
索引操作(主键索引锁一行，普通索引锁多行)：

前提:事务1 获取某行数据 lock in share mode:
1. 事务1 既可以查看也可以更改(更改会默认加 for update),可以加 for update,重复加lock in share mode，
更改或加 for update会将之前的lock in share mode 升级成 for update;
2. 事务2 可以获取该行数据((数据快照读，通过MVCC)，也可以加 lock in share mode， 
加 for update 阻塞。更新操作会被阻塞(更改会默认加 for update );
3. 事务1 对该行数据进行更改(更改会默认加 for update )或加 for update,
事务2 可以获取该行数据(修改前的数据快照读，通过MVCC)，但是加lock in share mode，for update 会阻塞;
3. 事务2 对该行数据 加 lock in share mode,事务1 ，事务2 都 不能对该行进行更改 或则加 for update，只能查询。

前提:事务1 获取某行数据 for update:
1. 事务1 既可以查看也可以更改(更改会默认加 for update),可以加 lock in share mode,重复加 for update，锁级别依旧为for update;
2. 事务2 可以获取该行数据((数据快照读，通过MVCC)，加 lock in share mode，for update都会阻塞。
更新操作会被阻塞(更改会默认加 for update );


行锁和索引的关系：查询字段未加索引（主键索引、普通索引等）时，使用表锁.
如果MySQL认为全表扫描效率更高，它就不会使用索引，这种情况下InnoDB将使用表锁，而不是行锁。

**注：InnoDB行级锁基于索引实现。**

未加索引时，两种行锁情况为（使用表锁）：
- 事务1获取某行数据共享锁，其他事务可以获取不同行数据的共享锁，不可以获取不同行数据的排他锁
- 事务1获取某行数据排他锁，其他事务不可以获取不同行数据的共享锁、排他锁

加索引后，两种行锁为（使用行锁）：

事务1获取某行数据共享锁，其他事务可以获取不同行数据的排他锁
事务1获取某行数据排他锁，其他事务可以获取不同行数据的共享锁、排他锁


[[MySQL] 行级锁SELECT ... LOCK IN SHARE MODE 和 SELECT ... FOR UPDATE](https://blog.csdn.net/u012099869/article/details/52778728)

### 当前读与快照读

1. 快照读(snapshot read):一致非锁定读(一致读、快照读)

简单的select操作(不包括 select ... lock in share mode, select ... for update)

一致性读，也称为快照读，读取的是快照版本。普通的select是快照读。在事务中select的时候会生成一个快照，不同隔离级别生成快照的时机不一样：

Read Committed隔离级别，在一个事务中每次读取都会重新生成一个快照，每次快照都是最新的，所以当前事务中每次select操作都可以看到其他已提交事务所做更改

Repeatable Read隔离级别，在一个事务中的第一次select执行的时候生成快照，只有在当前事务中对数据的修改才会更新快照。只有第一次select之前其他已提交事务所做更改可以看到，第一次select之后其他事务提交的更改当前事务是看不到的
一致性读，主要基于MVCC实现，多版本控制核心是数据快照，InnoDB通过undo log存储数据快照。

使用MVCC优势是不加锁，并发度高，但是读取的数据不是实时数据。

2.当前读(current read):锁定读

select ... lock in share mode

select ... for update

insert

update

delete

通过加record lock和gap lock间隙锁来实现，也就是next-key lock。使用next-key lock优势是获取实时数据，但是需要加锁。

[Mysql-InnoDB 事务-一致性读(快照读)](https://blog.csdn.net/cxm19881208/article/details/79415726)

[mysql/mariadb知识点总结（27）：一致性读，快照读](https://www.zsythink.net/archives/1436)

[https://blog.csdn.net/silyvin/article/details/79280934](https://blog.csdn.net/silyvin/article/details/79280934)


### mysql 索引加锁分析
主要依据事务隔离级别，受否为索引，是否为唯一索引 分析

[https://www.jianshu.com/p/13f5777966dd](https://www.jianshu.com/p/13f5777966dd)

### Mysql--gap locks,Next-Key Locks

Next-Key Locks是在存储引擎innodb、事务级别在可重复读的情况下使用的数据库锁。

gap锁，又称为间隙锁。存在的主要目的就是为了防止在可重复读的事务级别下，出现幻读问题。

**locking reads(S lock, X lock)，UPDATE和DELETE时，除了对唯一索引的唯一搜索外都会获取gap锁或next-key锁。即锁住其扫描的范围。**

#### gap锁加锁规则:

- 唯一索引
    - 精确等值检索，Next-Key Locks就退化为记录锁，不会加gap锁
    - 范围检索，会锁住where条件中相应的范围，范围中的记录以及间隙，换言之就是加上记录锁和gap 锁（至于区间是多大稍后讨论）。
    - 不走索引检索，全表间隙加gap锁、全表记录加记录锁
- 非唯一索引
    - 精确等值检索，Next-Key Locks会对间隙加gap锁（至于区间是多大稍后讨论），以及对应检索到的记录加记录锁。
    - 范围检索，会锁住where条件中相应的范围，范围中的记录以及间隙，换言之就是加上记录锁和gap 锁（至于区间是多大稍后讨论）。
- 非索引检索，全表间隙gap lock，全表记录record lock



加锁规则里面，包含了两个“原则”、两个“优化”和一个“bug”。

- 原则1：加锁的基本单位是next-key lock。**next-key lock是前开后闭区间**。
- 原则2：查找过程中访问到的对象才会加锁。
- 优化1：索引上的等值查询，给唯一索引加锁的时候，next-key lock退化为行锁。
- 优化2：索引上的等值查询，向右遍历时且最后一个值不满足等值条件的时候，next-key lock退化为间隙锁。
- 一个bug：唯一索引上的范围查询会访问到不满足条件的第一个值为止。

mysql 45讲 20 21

[深入了解mysql--gap locks,Next-Key Locks](https://blog.csdn.net/qq_20597727/article/details/87308709)

### Mysql 主从同步怎么搞的？分哪几个过程？如果有一台新机器要加到从机里，怎么个过程

mysql复制原理：

（1）master服务器将数据的改变记录二进制binlog日志，当master上的数据发生改变时，则将其改变写入二进制日志中；

（2）slave服务器会在一定时间间隔内对master二进制日志进行探测其是否发生改变，如果发生改变，则开始一个I/OThread请求master二进制事件

（3）同时主节点为每个I/O线程启动一个dump线程，用于向其发送二进制事件，并保存至从节点本地的中继日志中，从节点将启动SQL线程从中继日志中读取二进制日志，在本地重放，使得其数据和主节点的保持一致，最后I/OThread和SQLThread将进入睡眠状态，等待下一次被唤醒。

从库会生成两个线程,一个I/O线程,一个SQL线程;
I/O线程会去请求主库的binlog,并将得到的binlog写到本地的relay-log(中继日志)文件中;
主库会生成一个log dump线程,用来给从库I/O线程传binlog;
SQL线程,会读取relay log文件中的日志,并解析成sql语句逐一执行;

MySQL 主从复制模式

异步模式（mysql async-mode）

半同步模式(mysql semi-sync)

全同步模式



### MySQL是怎么保证高可用的

主备延迟:

与数据同步有关的时间点主要包括以下三个：

主库A执行完成一个事务，写入binlog，我们把这个时刻记为T1;

之后传给备库B，我们把备库B接收完这个binlog的时刻记为T2;

备库B执行完成这个事务，我们把这个时刻记为T3。

所谓主备延迟，就是同一个事务，在备库执行完成的时间和主库执行完成的时间之间的差值，也就是T3-T1。

你可以在备库上执行show slave status命令，它的返回结果里面会显示seconds_behind_master，用于表示当前备库延迟了多少秒。

你可以在备库上执行show slave status命令，它的返回结果里面会显示seconds_behind_master，用于表示当前备库延迟了多少秒。


可靠性优先策略：系统存在不可写状态，时间受主备延迟影响

可用性优先策略：可能出现数据不一致的情况。
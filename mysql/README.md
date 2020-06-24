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

### 普通索引与唯一索引

[https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase](https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

### 单列索引和联合索引

[https://blog.csdn.net/Abysscarry/article/details/80792876](https://blog.csdn.net/Abysscarry/article/details/80792876)

### MVCC

### Mysql 主从同步怎么搞的？分哪几个过程？如果有一台新机器要加到从机里，怎么个过程

### Binlog 日志是 master 推的还是 salve 来拉的？

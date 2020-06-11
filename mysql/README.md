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

### Mysql日志系统

### MySQL 如何分析一条语句的执行过程。delete from t1 limit 3和delete from t1的区别

### 普通索引与唯一索引

[https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase](https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

### 单列索引和联合索引

[https://blog.csdn.net/Abysscarry/article/details/80792876](https://blog.csdn.net/Abysscarry/article/details/80792876)

### MVCC

### Mysql 主从同步怎么搞的？分哪几个过程？如果有一台新机器要加到从机里，怎么个过程

### Binlog 日志是 master 推的还是 salve 来拉的？

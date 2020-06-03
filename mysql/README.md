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

### 3.mysql 有那些存储引擎，有哪些区别

### 4.mysql 索引在什么情况下会失效

[https://juejin.im/post/5ec15ab9f265da7bc60e1910?utm_source=gold_browser_extension](https://juejin.im/post/5ec15ab9f265da7bc60e1910?utm_source=gold_browser_extension)
[https://juejin.im/post/5de99dd2518825125e1ba49d](https://juejin.im/post/5de99dd2518825125e1ba49d)

### 5.mysql 的索引模型

### 6.mysql 主从同步怎么搞的？分哪几个过程？如果有一台新机器要加到从机里，怎么个过程。

### 7.binlog 日志是 master 推的还是 salve 来拉的？

### 8.乐观锁与悲观锁的区别？

### 9.MySQL 如何分析一条语句的执行过程。delete from t1 limit 3和delete from t1的区别？

### 10.普通索引与唯一索引

[https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase](https://blog.csdn.net/weixin_42570248/article/details/89099989?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

### 11.MVCC

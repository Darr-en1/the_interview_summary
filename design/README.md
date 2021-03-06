### 设计一个算法抽奖次数越多中奖概率就越高

设置基础中奖概率,通过类似对数计算抽奖次数和额外中奖概率的关系，并设置概率提升的上限。

### 微服务的特点，如何实现服务发现

需要一个服务中心,并具备高可用

服务注册表，一个包含服务实例网络地址的的数据库

引入服务保活和检查机制,心跳机制

集成服务配置管理功能

[https://zhuanlan.zhihu.com/p/34332329](https://zhuanlan.zhihu.com/p/34332329)

[https://www.jianshu.com/p/1bf9a46efe7a](https://www.jianshu.com/p/1bf9a46efe7a)

### 请求幂等性

[https://segmentfault.com/a/1190000020172463](https://segmentfault.com/a/1190000020172463)

### 分布式事务

CAP 定理

CAP 首次在 ACM PODC 会议上作为猜想被提出，两年后被证明为定理，从此深深影响了分布式计算的发展。CAP 理论告诉我们，一个分布式系统不可能同时满足一致性（Consistency）、可用性（Availability）和分区容错性（Partition tolerance）这三个基本需求，最多只能同时满足其中的两项。

一致性：数据在多个副本之间保持一致。当有一个节点的数据发生更新后，其它节点应该也能同步地更新数据。

可用性：对于用户的每一个操作请求，系统总能在有限的时间内返回结果。

分区容错性：分布式系统中的不同节点可能分布在不同的子网络中，这些子网络被称为网络分区。由于一些特殊原因导致子网络之间出现网络不连通的情况，系统仍需要能够保证对外提供一致性和可用性的服务。

[https://www.yisu.com/zixun/92118.html](https://www.yisu.com/zixun/92118.html)

### 负载均衡算法有哪些

常见的负载均衡算法：

- 轮询法（Round Robin） 
- 加权轮询法（Weight Robin） 
- 随机法（Random）
- 加权随机法（Weight Random）
- 最小连接法（Least Connections）
- 源地址哈希法（Hash）

[https://blog.csdn.net/sinat_36246371/article/details/78160448](https://blog.csdn.net/sinat_36246371/article/details/78160448)

### 熔断是怎么实现的

分布式 ID 生成器的解决方案总结
分布式 Session 共享解决方案
分布式锁与幂等性问题解决方案
微服务架构及分布式事务解决方案
高并发大流量访问处理及解决方案

### id生成器怎么实现的，如何实现全局递增

### 6.负载均衡的加权轮询算法怎么实现

### 7.背包问题

### 8.现有一个随机数生成器可以生成0到4的数，现在要让你用这个随机数生成器生成0到6的随机数，要保证生成的数概率均匀。





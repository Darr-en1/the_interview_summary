### 动态规划与贪心有什么区别

[https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie](https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie)

动态规划套路详解:
- 状态转移方程
- 最优子结构: 子问题间必须互相独立


### 快排,最小堆,冒泡,插入,堆排序等排序方法

![sort](sort.png)

[https://www.cnblogs.com/onepixel/p/7674659.html](https://www.cnblogs.com/onepixel/p/7674659.html)

### AVL 红黑树

[https://blog.csdn.net/21aspnet/article/details/88939297](https://blog.csdn.net/21aspnet/article/details/88939297)




1.通过协程实现多用例组合执行模式。运行设备可以在多个用例执行的过程来回切换，模拟用户使用的真实场景。
2.推荐算法选择设备时，将更容易出现错误的用例提炼出来优先展示，用例属性列表还有用例结果，通过比重计算出结果值返回结果。
3.通过rabbitmq实现用例资源同步机制，通过锁机制避免支援重复下载的问题。
4.通过对数据库慢查询日志分析和数据库表结构分析，使用 django-debug-toolbar 结合 jmeter 对项目性能进行优化性能提升 32%

设备资源管理功能

软件账号 实体卡


用例同步机制
用例编辑完成，celery异步会对用例进行打包(每一个包会携带一个版本号，用于查看是否需要更新)，这个过程中用例是不能被执行的，执行完成后通过rabbitmq将消息通知给coral ，
这个时候下发任务立即执行的话，有可能coral实例中没有用例或者版本不一致，这个时候需要下拉，下拉过程要保证同步，不然就会导致多拉的情况
需要一个更细粒度的锁，tboard id 作为 key value 未完成。会起专门的线程用于拉去用例，hash过滤重复数据
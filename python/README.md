### python版本
[你应该知道的Python3.6、3.7、3.8新特性](https://www.liujiangblog.com/blog/51/)

### 协程和线程的区别

进程线程id 都唯一

[https://blog.csdn.net/u013007900/article/details/89016375](https://blog.csdn.net/u013007900/article/details/89016375)

### 进程间通讯方法

multiprocessing.Pipe:适用于两个进程之间，性能高于Queue

multiprocessing.Queue:可用于进程间通信,但在进程池中失效

multiprocessing.Manager:分装了进程间通信的多个对象

### Python装饰器,装饰器传参

装饰器就是闭包的实现

[https://darr-en1.github.io/2020/01/16/1/](https://darr-en1.github.io/2020/01/16/1/)

[https://darr-en1.github.io/2019/03/12/1/](https://darr-en1.github.io/2019/03/12/1/)

### Python内存管理

在Python中，主要通过引用计数进行垃圾回收；通过 “标记-清除” 解决容器对象可能产生的循环引用问题；通过 “分代回收” 以空间换时间的方法提高垃圾回收效率

[https://v3u.cn/book/member.html](https://v3u.cn/book/member.html)

[https://andrewpqc.github.io/2018/10/08/python-memory-management/](https://andrewpqc.github.io/2018/10/08/python-memory-management/)
### 循环引用的处理(弱引用)

对象引用导致的内存不能回收

[循环引用数据结构的内存管理](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p23_managing_memory_in_cyclic_data_structures.html)

包引入问题

[python中的循环引用](https://hustyichi.github.io/2018/10/30/circular-import/)

[python解决循环引用问题](https://www.jianshu.com/p/a1e91cc53b07)


### 深浅拷贝

[https://www.cnblogs.com/wilber2013/p/4645353.html](https://www.cnblogs.com/wilber2013/p/4645353.html)

### 协程的原理

协程：具备多个入口的函数，也可以暂停的函数，可以向暂停的地方传入值

1.协程是一种轻量级的用户态线程

2.开发者自行控制程序切换时机，而不是像进程和线程那样把控制权交给操作系统

3.协程没有线程、进程切换的时间和资源开销

4.协程是非抢占式调度，当前协程切换到其他协程是由自己控制；线程则是时间片用完抢占时间片调度

优缺点

协程
优点：
1.用户态，语言级别；

2.无切换性能消耗；

3.非抢占式；

4.同步代码思维；

5.减少同步锁

缺点：

1.注意全局变量；

2.阻塞操作会导致整个线程被阻塞

[再议Python协程——从yield到asyncio](https://www.cnblogs.com/zingp/p/8678109.html#_label0)

[python协程总结](https://www.cnblogs.com/fengf233/p/11548769.html)

[https://blog.csdn.net/xfgryujk/article/details/80854750](https://blog.csdn.net/xfgryujk/article/details/80854750)

### Python垃圾回收机制

同 [Python内存管理](#Python内存管理) 问题相似

引用计数

标记清除解决循环引用

在循环引用对象的回收中，整个应用程序会被暂停，为了减少应用程序暂停的时间，Python 通过“**分代回收**”(Generational Collection)以空间换时间的方法提高垃圾回收效率。


总体来说，在Python中，主要通过引用计数进行垃圾回收；通过 “标记-清除” 解决容器对象可能产生的循环引用问题；通过 “分代回收” 以空间换时间的方法提高垃圾回收效率。

[https://zhuanlan.zhihu.com/p/83251959](https://zhuanlan.zhihu.com/p/83251959)

### Mro

### asyncio

Asyncio.gather vs asyncio.wait

区别的第一层区别:

asyncio.gather 封装的 Task 全程黑盒，只告诉你协程结果。
asyncio.wait 会返回封装的 Task (包含已完成和挂起的任务)，如果你关注协程执行结果你需要从对应 Task 实例里面用 result 方法自己拿。


[深入理解asyncio(二)](https://www.dongwm.com/post/understand-asyncio-2/)

### celery

[分布式任务队列Celery入门与进阶](https://www.cnblogs.com/wdliu/p/9517535.html)

### Django_ORM性能优化
[Django ORM性能优化，数据存取优化](https://www.jianshu.com/p/aded5b2029f6)

### Django运行方式及处理流程总结
[Django运行方式及处理流程总结](https://segmentfault.com/a/1190000002399134)

### Flask路由原理

在Flask中是使用@app.route这个装饰器来实现url和方法之间的映射的。

route装饰器其实就是调用了add_url_rule，

self.url_map将 rule通过Rule对象实例化加入到Map中

将试图函数 和视图函数名称加入到app.view_functions（dict结构）



```Flask.route -> Flask.add_url_rule -> Map.add -> Rule.bind```

[路由原理](https://juejin.im/post/6844903895655776269)

### Flask代理对象
[全局变量](https://juejin.im/post/6844903920842588174)

[Flask 上下文理解](https://jin-yang.github.io/post/flask-context.html)

[flask 源码解析](https://cizixs.com/2017/01/11/flask-insight-start-process/)

### Python异步编程
[Python异步编程](https://mp.weixin.qq.com/s/H-0pd3NcAJDbUckNi0-IEw)


[高级编程](https://www.cnblogs.com/wry789/p/13710444.html)

[高级编程](https://www.cnblogs.com/crazymagic/articles/10066437.html)
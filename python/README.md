### 协程和线程的区别

进程线程id 都唯一

[https://blog.csdn.net/u013007900/article/details/89016375](https://blog.csdn.net/u013007900/article/details/89016375)

[https://blog.csdn.net/daaikuaichuan/article/details/82951084?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase](https://blog.csdn.net/daaikuaichuan/article/details/82951084?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase)

### 进程间通讯方法

multiprocessing.Pipe:适用于两个进程之间，性能高于Queue

multiprocessing.Queue:可用于进程间通信,但在进程池中失效

multiprocessing.Manager:分装了进程间通信的多个对象

### Python装饰器,装饰器传参

[https://darr-en1.github.io/2020/01/16/1/](https://darr-en1.github.io/2020/01/16/1/)

[https://darr-en1.github.io/2019/03/12/1/](https://darr-en1.github.io/2019/03/12/1/)

### Python内存管理

在Python中，主要通过引用计数进行垃圾回收；通过 “标记-清除” 解决容器对象可能产生的循环引用问题；通过 “分代回收” 以空间换时间的方法提高垃圾回收效率

[https://v3u.cn/book/member.html](https://v3u.cn/book/member.html)

[https://andrewpqc.github.io/2018/10/08/python-memory-management/](https://andrewpqc.github.io/2018/10/08/python-memory-management/)
### 循环引用的处理(弱引用)

对象引用导致的内存不能回收

[https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p23_managing_memory_in_cyclic_data_structures.html](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p23_managing_memory_in_cyclic_data_structures.html)

包引入问题

[https://hustyichi.github.io/2018/10/30/circular-import/](https://hustyichi.github.io/2018/10/30/circular-import/)

[https://www.jianshu.com/p/a1e91cc53b07](https://www.jianshu.com/p/a1e91cc53b07)


### 深浅拷贝

### 协程的原理

### python垃圾回收机制
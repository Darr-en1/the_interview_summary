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

[https://v3u.cn/book/member.html](https://v3u.cn/book/member.html)

5.循环引用的处理（弱引用）

6.深浅拷贝

7.协程的原理

8.python垃圾回收机制
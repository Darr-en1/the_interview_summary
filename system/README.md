1.select 和 epoll的区别

select的几大缺点：
- 每次调用select，都需要把fd集合从用户态拷贝到内核态，这个开销在fd很多时会很大
- 同时每次调用select都需要在内核遍历传递进来的所有fd，这个开销在fd很多时也很大
- select支持的文件描述符数量太小了，默认是1024

epoll的提升：
- 本身没有最大并发连接的限制，仅受系统中进程能打开的最大文件数目限制；
- 效率提升：只有活跃的socket才会主动的去调用callback函数；
- 省去不必要的内存拷贝：epoll通过内核与用户空间mmap同一块内存实现。

[https://www.jianshu.com/p/430141f95ddb](https://www.jianshu.com/p/430141f95ddb)

2.程序crash如何定位

3.服务性能问题如何定位

4.gdb怎么切换线程

5.查看 CPU 的命令和磁盘 IO 的命令

6.linux 系统里，一个被打开的文件可以被另一个进程删除吗？

7.linux 信号

8.僵尸进程

9.top命令

10.软硬链接

11.linux所有文件类型

12.fork()的返回值

13.项目中内存或cpu占用过高如何排查
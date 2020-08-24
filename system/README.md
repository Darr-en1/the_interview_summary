### Select和epoll的区别

select的几大缺点：
- 每次调用select，都需要把fd集合从用户态拷贝到内核态，这个开销在fd很多时会很大
- 同时每次调用select都需要在内核遍历传递进来的所有fd，这个开销在fd很多时也很大
- select支持的文件描述符数量太小了，默认是1024

epoll的提升：
- 本身没有最大并发连接的限制，仅受系统中进程能打开的最大文件数目限制；
- 效率提升：只有活跃的socket才会主动的去调用callback函数；
- 省去不必要的内存拷贝：epoll通过内核与用户空间mmap同一块内存实现。

[https://www.jianshu.com/p/430141f95ddb](https://www.jianshu.com/p/430141f95ddb)

### 程序crash如何定位

logger 单步调试

[https://zhuanlan.zhihu.com/p/27700767](https://zhuanlan.zhihu.com/p/27700767)

### 服务性能问题如何定位

检索日志中的异常

CPU占用率

内存占用

磁盘I/O

网络I/O

数据库的监控分析: 长连接，久sql记录

[https://blog.csdn.net/smooth00/article/details/63680191](https://blog.csdn.net/smooth00/article/details/63680191)

### 查看CPU的命令和磁盘IO的命令

linux监控CPU、磁盘IO、网络IO、磁盘容量、内存使用

- CPU：vmstat ，sar –u，top
- 磁盘IO：iostat –xd，sar –d，top
- 网络IO：iftop -n，ifstat，dstat –nt，sar -n DEV 2 3
- 磁盘容量：df –h 
- 内存使用：free –m，top


python第三方包 [psutil](https://github.com/giampaolo/psutil)

### Linux系统里一个被打开的文件可以被另一个进程删除吗

[https://zhuanlan.zhihu.com/p/25600743](https://zhuanlan.zhihu.com/p/25600743)

[https://blog.csdn.net/weiwangchao_/article/details/94578327](https://blog.csdn.net/weiwangchao_/article/details/94578327)

### 软硬链接

[https://www.jianshu.com/p/dde6a01c4094](https://www.jianshu.com/p/dde6a01c4094)

### Linux信号

[https://www.jianshu.com/p/f445bfeea40a](https://www.jianshu.com/p/f445bfeea40a)

### 僵尸进程

僵尸进程：一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵死进程。

问题及危害

unix提供了一种机制可以保证只要父进程想知道子进程结束时的状态信息， 就可以得到。这种机制就是: 在每个进程退出的时候,内核释放该进程所有的资源,包括打开的文件,
占用的内存等。 但是仍然为其保留一定的信息(包括进程号the process ID,退出状态the termination status of the process,运行时间the amount of CPU time taken by the process等)。
直到父进程通过wait / waitpid来取时才释放。 但这样就导致了问题，如果进程不调用wait / waitpid的话， 那么保留的那段信息就不会释放，其进程号就会一直被占用，
但是系统所能使用的进程号是有限的，如果大量的产生僵死进程，将因为没有可用的进程号而导致系统不能产生新的进程. 此即为僵尸进程的危害，应当避免。

[https://www.cnblogs.com/Anker/p/3271773.html](https://www.cnblogs.com/Anker/p/3271773.html)

### top命令

### linux所有文件类型

### fork()的返回值

### 项目中内存或cpu占用过高如何排查

### Gdb怎么切换线程

### 用户态和内核态的区别
[用户态和内核态的区别](https://www.cnblogs.com/gizing/p/10925286.html)
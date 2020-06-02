1.一个完整的 HTTP 请求会涉及到哪些协议？

应用层 http 协议  ssl 加密协议

传输层 tcp协议

网络层引入了三个协议，分别是IP协议、ARP协议、路由协议。

ARP协议:IP地址获取MAC地址的一个网络层协议

路由协议:通过ARP协议的工作原理可以发现，ARP的MAC寻址还是局限在同一个子网中，因此网络层引入了路由协议，首先通过IP协议来判断两台主机是否在同一个子网中，如果在同一个子网，就通过ARP协议查询对应的MAC地址，然后以广播的形式向该子网内的主机发送数据包；如果不在同一个子网，以太网会将该数据包转发给本子网的网关进行路由。网关是互联网上子网与子网之间的桥梁，所以网关会进行多次转发，最终将该数据包转发到目标IP所在的子网中，然后再通过ARP获取目标机MAC，最终也是通过广播形式将数据包发送给接收方。

链路层  以太网协议


每层模型的职责：
- 链路层：对0和1进行分组，定义数据帧，确认主机的物理地址，传输数据；
- 网络层：定义IP地址，确认主机所在的网络位置，并通过IP进行MAC寻址，对外网数据包进行路由转发；
- 传输层：定义端口，确认主机上应用程序的身份，并将数据包交给对应的应用程序；
- 应用层：定义数据格式，并按照对应的格式解读数据。

[https://www.cnblogs.com/onepixel/p/7092302.html](https://www.cnblogs.com/onepixel/p/7092302.html)

[https://zhuanlan.zhihu.com/p/38240894](https://zhuanlan.zhihu.com/p/38240894)

2.一个 10M 大小的 buffer 里存满了数据，现在要把这个 buffer 里的数据尽量发出去，可以允许部分丢包，问是用TCP好还是UDP好？为什么？

3.tcp 的握手与挥手

4,http与https的区别，加密怎么加的？

[https://www.jianshu.com/p/6c981b44293d](https://www.jianshu.com/p/6c981b44293d)

5.http各种返回码，401和406啥区别？

6.TCP连接中time_wait状态的理解,time_wait在哪一端产生，作用是什么

7.OSI，TCP/IP，五层协议的体系结构，以及各层协议

[https://www.nowcoder.com/questionTerminal/6032e54a13b54a81ae2697d2a8477244](https://www.nowcoder.com/questionTerminal/6032e54a13b54a81ae2697d2a8477244)

8.TCP/IP Socket http 概念

[https://www.jianshu.com/p/2357fd67e612](https://www.jianshu.com/p/2357fd67e612)\
[https://www.jianshu.com/p/8565912949bb](https://www.jianshu.com/p/8565912949bb)

### 一个完整的HTTP请求会涉及到哪些协议

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

[探究！一个数据包在网络中的心路历程](https://mp.weixin.qq.com/s?__biz=MzUxODAzNDg4NQ==&mid=2247483989&idx=1&sn=7e2ed852770743d3955ef9d5561fcef3&scene=21#wechat_redirect)

[https://www.cnblogs.com/onepixel/p/7092302.html](https://www.cnblogs.com/onepixel/p/7092302.html)

[https://zhuanlan.zhihu.com/p/38240894](https://zhuanlan.zhihu.com/p/38240894)

### 一个10M大小的buffer里存满了数据,现在要把这个buffer里的数据尽量发出去,可以允许部分丢包,问是用TCP好还是UDP好?为什么?

TCP UDP都是传输层协议

TCP:
- TCP 提供一种面向连接的、可靠的字节流服务
- 在一个 TCP 连接中，仅有两方进行彼此通信。广播和多播不能用于 TCP
- TCP 使用校验和，确认和重传机制来保证可靠传输
- TCP 给数据分节进行排序，并使用累积确认保证数据的顺序不变和非重复
- TCP 使用滑动窗口机制来实现流量控制，通过动态改变窗口的大小进行拥塞控制

注意：TCP 并不能保证数据一定会被对方接收到，因为这是不可能的。TCP 能够做到的是，如果有可能，就把数据递送到接收方，否则就（通过放弃重传并且中断连接这一手段）通知用户。因此准确说 TCP 也不是 100% 可靠的协议，它所能提供的是数据的可靠递送或故障的可靠通知。

UDP:
- UDP 缺乏可靠性。UDP 本身不提供确认，序列号，超时重传等机制。UDP 数据报可能在网络中被复制，被重新排序。即 UDP 不保证数据报会到达其最终目的地，也不保证各个数据报的先后顺序，也不保证每个数据报只到达一次
- UDP 数据报是有长度的。每个 UDP 数据报都有长度，如果一个数据报正确地到达目的地，那么该数据报的长度将随数据一起传递给接收方。而 TCP 是一个字节流协议，没有任何（协议上的）记录边界。
- UDP 是无连接的。UDP 客户和服务器之前不必存在长期的关系。UDP 发送数据报之前也不需要经过握手创建连接的过程。
- UDP 支持多播和广播。


[一文搞懂TCP与UDP的区别](https://blog.fundebug.com/2019/03/22/differences-of-tcp-and-udp/)

[TCP和UDP的区别](https://zhuanlan.zhihu.com/p/24860273)

### Tcp的握手与挥手
SYN   Synchronize（同步）

seq: sequence number（序列号）

ACK (ACKnowledge Character） 

RST   Reset   重连位~ 当RST=1的时候通知重新建立TCP连接

FIN：Finall 


TCP标志位
TCP在其协议头中使用大量的标志位或者说1位（bit）布尔域来控制连接状态，一个包中有可以设置多个标志位。

TCP是主机对主机层的传输控制协议，提供可靠的连接服务，采用三次握手确认建立一个连接：

位码即TCP标志位，有6种标示：SYN(synchronous建立联机) ACK(acknowledgement 确认) PSH(push传送) FIN(finish结束) RST(reset重置) URG(urgent紧急)Sequence number(顺序号码) Acknowledge number(确认号码)
我们常用的是以下三个标志位：

SYN - 创建一个连接

FIN - 终结一个连接

ACK - 确认接收到的数据


**syn攻击**
在三次握手过程中，服务器发送SYN-ACK之后，收到客户端的ACK之前的TCP连接称为半连接(half-open connect).此时服务器处于Syn_RECV状态.当收到ACK后，服务器转入ESTABLISHED状态.

Syn攻击就是 攻击客户端 在短时间内伪造大量不存在的IP地址，向服务器不断地发送syn包，服务器回复确认包，并等待客户的确认，由于源地址是不存在的，服务器需要不断的重发直 至超时，这些伪造的SYN包将长时间占用未连接队列，正常的SYN请求被丢弃，目标系统运行缓慢，严重者引起网络堵塞甚至系统瘫痪。

Syn攻击是一个典型的DDOS攻击。检测SYN攻击非常的方便，当你在服务器上看到大量的半连接状态时，特别是源IP地址是随机的，基本上可以断定这是一次SYN攻击.在Linux下可以如下命令检测是否被Syn攻击

netstat -n -p TCP | grep SYN_RECV

一般较新的TCP/IP协议栈都对这一过程进行修正来防范Syn攻击，修改tcp协议实现。主要方法有SynAttackProtect保护机制、SYN cookies技术、增加最大半连接和缩短超时时间等.

但是不能完全防范syn攻击。



半连接队列

TIME_WAIT:time_wait状态是四次挥手中server向client发送FIN终止连接后进入的状态。

三次握手
![Three_way_Handshake.jpg](Three_way_Handshake.jpg)

四次挥手
![Four_times_to_wave.jpg](Four_times_to_wave.jpg)

[为什么tcp是三次握手而不是两次握手？](https://zhuanlan.zhihu.com/p/51448333)

[面试官，不要再问我三次握手和四次挥手](https://zhuanlan.zhihu.com/p/86426969)

[TCP协议](https://hit-alibaba.github.io/interview/basic/network/TCP.html)

### Http与https的区别加密逻辑

加密对象：
通信的加密
内容的加密

[https://zhuanlan.zhihu.com/p/43789231](https://zhuanlan.zhihu.com/p/43789231)
[https://www.cnblogs.com/wqhwe/p/5407468.html](https://www.cnblogs.com/wqhwe/p/5407468.html)

### Http各种返回码401和406啥区别

[https://blog.csdn.net/ningxinyu520/article/details/18217077](https://blog.csdn.net/ningxinyu520/article/details/18217077)

### TCP连接中time_wait状态的理解time_wait在哪一端产生作用是什么

MSL是Maximum Segment Lifetime,译为“报文最大生存时间”

[https://blog.csdn.net/godleading/article/details/50849253](https://blog.csdn.net/godleading/article/details/50849253)

### 滑动窗口

滑动窗口

TCP的滑动窗口是以字节为单位的。TCP利用滑动窗口协议来进行流量控制

ARQ协议，即自动重传请求（Automatic Repeat-reQuest）

ARQ包括停止等待ARQ协议和连续ARQ协议

停止等待ARQ协议信道利用率太低，所以需要使用连续ARQ协议来进行改善。
连续ARQ协议通常是结合滑动窗口协议来使用的。

[https://mp.weixin.qq.com/s/Tc09ovdNacOtnMOMeRc_uA](https://mp.weixin.qq.com/s/Tc09ovdNacOtnMOMeRc_uA)

### OSI，TCP/IP，五层协议的体系结构，以及各层协议

[https://www.nowcoder.com/questionTerminal/6032e54a13b54a81ae2697d2a8477244](https://www.nowcoder.com/questionTerminal/6032e54a13b54a81ae2697d2a8477244)

### TCP/IP Socket http概念

[https://www.jianshu.com/p/2357fd67e612](https://www.jianshu.com/p/2357fd67e612)

[https://www.jianshu.com/p/8565912949bb](https://www.jianshu.com/p/8565912949bb)

### TCP提供可靠传输的工作原理和实现过程

TCP为了提供可靠传输：
1. 首先，采用三次握手来建立TCP连接，四次握手来释放TCP连接，从而保证建立的传输信道是可靠的。
2. 其次，TCP采用了连续ARQ协议（回退N，Go-back-N；超时自动重传）来保证数据传输的正确性，使用滑动窗口协议来保证接方能够及时处理所接收到的数据，进行流量控制。
3. 最后，TCP使用慢开始、拥塞避免、快重传和快恢复来进行拥塞控制，避免网络拥塞。

[一文搞定 UDP 和 TCP 高频面试题！](https://zhuanlan.zhihu.com/p/108822858)

[https://blog.csdn.net/guoweimelon/article/details/50878503](https://blog.csdn.net/guoweimelon/article/details/50878503)

### TCP粘包怎么解决

### TCP半连接队列和全连接队列

[TCP 半连接队列和全连接队列满了会发生什么？又该如何应对？](https://mp.weixin.qq.com/s?__biz=MzUxODAzNDg4NQ==&mid=2247484569&idx=1&sn=1ca4daeb8043a957850ab7a8f4f1120e&chksm=f98e4033cef9c925f81e049b7bdc179123db36be01d25d339829958ca923707e82705cb4946f&scene=158#rd)

### Websocket

[记录关于websocket的原理和使用](https://vimiix.com/post/2018/04/02/python-websocket/)

### Restful

[深入理解什么是RESTful API](http://www.imooc.com/article/304756)

### Linux后台进程管理
[Linux后台进程管理以及ctrl+z（挂起）、ctrl+c（中断）、ctrl+\（退出）和ctrl+d（EOF）的区别](https://blog.csdn.net/u012787436/article/details/39722583)
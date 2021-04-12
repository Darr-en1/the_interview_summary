### 一个完整的HTTP请求会涉及到哪些协议

应用层 http 协议  ssl 加密协议

DNS协议:域名解析

传输层 tcp协议 （http3则采用udp）

网络层引入了三个协议，分别是IP协议、ARP协议、路由协议。

    发送者如何知道接收者的MAC地址？（arp协议）
    发送者如何知道接收者和自己同属一个子网？(ip协议)
    如果接收者和自己不在同一个子网，数据包如何发给对方(路由协议)


**ARP协议**:IP地址获取MAC地址的一个网络层协议

ARP首先会发起一个请求数据包，数据包的首部包含了目标主机的IP地址，然后这个数据包会在链路层进行再次包装，生成以太网数据包，最终由以太网广播给子网内的所有主机，每一台主机都会接收到这个数据包，并取出标头里的IP地址，然后和自己的IP地址进行比较，如果相同就返回自己的MAC地址，如果不同就丢弃该数据包。ARP接收返回消息，以此确定目标机的MAC地址；与此同时，ARP还会将返回的MAC地址与对应的IP地址存入本机ARP缓存中并保留一定时间，下次请求时直接查询ARP缓存以节约资源。cmd输入 arp -a 就可以查询本机缓存的ARP数据。


**路由协议**:通过ARP协议的工作原理可以发现，**ARP的MAC寻址还是局限在同一个子网中**，因此网络层引入了路由协议，首先通过IP协议来判断两台主机是否在同一个子网中，如果在同一个子网，就通过ARP协议查询对应的MAC地址，然后以**广播的形式向该子网内的主机发送数据包**；如果不在同一个子网，以太网会将该数据包转发给本子网的网关进行路由。网关是互联网上子网与子网之间的桥梁，所以网关会进行多次转发，最终将该数据包转发到目标IP所在的子网中，然后再通过ARP获取目标机MAC，最终也是通过广播形式将数据包发送给接收方。

链路层  以太网协议




每层模型的职责：
- 链路层：对0和1进行分组，定义数据帧，确认主机的物理地址，传输数据；
- 网络层：定义IP地址，确认主机所在的网络位置，并通过IP进行MAC寻址，对外网数据包进行路由转发；
- 传输层：定义端口，确认主机上应用程序的身份，并将数据包交给对应的应用程序；
- 应用层：定义数据格式，并按照对应的格式解读数据。



总结描述：

1.首先浏览器做的第一步工作就是要对 URL 进行解析，查询服务器域名对于的 IP 地址(DNS)。客户端首先会发出一个 DNS 请求，发给本地 DNS 服务器查询缓存。没有则会去问它的根域名服务器返回域名所在的DNS 服务器
权威 DNS 服务器查询后将对应的 IP 地址 X.X.X.X 告诉本地 DNS。本地 DNS 再将 IP 地址返回客户端，客户端和目标建立连接。
2.然后建立tcp通信，通过ARP协议找到ip对应的mac地址，ARP（有缓存）的MAC寻址还是局限在同一个子网中,IP协议来判断两台主机是否在同一个子网。
3.以太网会将该数据包转发给本子网的网关进行路由。网关是互联网上子网与子网之间的桥梁，所以网关会进行多次转发。最终将该数据包转发到目标IP所在的子网中，然后再通过ARP获取目标机MAC，最终也是通过广播形式将数据包发送给接收方。
3.数据传输到服务器后进行解包得到数据传递到http服务器中进行处理，然后将结果返回，返回也是一样的传输过程。

[探究！一个数据包在网络中的心路历程](https://mp.weixin.qq.com/s?__biz=MzUxODAzNDg4NQ==&mid=2247483989&idx=1&sn=7e2ed852770743d3955ef9d5561fcef3&scene=21#wechat_redirect)

[深入浅出 TCP/IP 协议栈](https://www.cnblogs.com/onepixel/p/7092302.html)

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

强烈推荐：[面试官，不要再问我三次握手和四次挥手](https://zhuanlan.zhihu.com/p/86426969)

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

Syn攻击就是 攻击客户端 在短时间内伪造大量不存在的IP地址，向服务器不断地发送syn包，服务器回复确认包，并等待客户的确认，由于源地址是不存在的，服务器需要不断的重发直 至超时，这些伪造的SYN包将长时间占用半连接队列，正常的SYN请求被丢弃，目标系统运行缓慢，严重者引起网络堵塞甚至系统瘫痪。

Syn攻击是一个典型的DDOS攻击。检测SYN攻击非常的方便，当你在服务器上看到大量的半连接状态时，特别是源IP地址是随机的，基本上可以断定这是一次SYN攻击.在Linux下可以如下命令检测是否被Syn攻击

netstat -n -p TCP | grep SYN_RECV

一般较新的TCP/IP协议栈都对这一过程进行修正来防范Syn攻击，修改tcp协议实现。主要方法有SynAttackProtect保护机制、SYN cookies技术、增加最大半连接和缩短超时时间等.

但是不能完全防范syn攻击。


TIME_WAIT:time_wait状态是四次挥手中server向client发送FIN终止连接后进入的状态。

三次握手
![Three_way_Handshake.jpg](Three_way_Handshake.jpg)

四次挥手
![Four_times_to_wave.jpg](Four_times_to_wave.jpg)

[TCP协议](https://hit-alibaba.github.io/interview/basic/network/TCP.html)

### Http与https的区别加密逻辑

##### 非对称加密+对称加密？
某网站拥有用于非对称加密的公钥A、私钥A’。
浏览器向网站服务器请求，服务器把**公钥A明文给传输浏览器**。
浏览器随机生成一个用于**对称加密的密钥X**，用公钥A加密后传给服务器。
服务器拿到后用私钥A’解密得到密钥X。
这样双方就都拥有密钥X了，且别人无法知道它。之后双方所有数据都通过密钥X加密解密即可。

##### 中间人攻击

某网站有用于非对称加密的公钥A、私钥A’。
浏览器向网站服务器请求，服务器把公钥A明文给传输浏览器。
中间人劫持到公钥A，保存下来，把数据包中的公钥A替换成自己伪造的公钥B（它当然也拥有公钥B对应的私钥B’）。
浏览器生成一个用于对称加密的密钥X，用公钥B（浏览器无法得知公钥被替换了）加密后传给服务器。
中间人劫持后用私钥B’解密得到密钥X，再用公钥A加密后传给服务器。
服务器拿到后用私钥A’解密得到密钥X。

##### 数字证书

网站在使用HTTPS前，需要向CA机构申领一份数字证书，数字证书里含有证书持有者信息、公钥信息等。服务器把证书传输给浏览器，浏览器从证书里获取公钥就行了，证书就如身份证，证明“该公钥对应该网站”。

##### 数字签名

数字签名的制作过程：

CA机构拥有非对称加密的私钥和公钥。
CA机构对证书明文数据T进行hash。
对hash后的值用私钥加密，得到数字签名S。

**明文和数字签名共同组成了数字证书**，这样一份数字证书就可以颁发给网站了。

浏览器验证过程：

拿到证书，得到明文T，签名S。
用**CA机构的公钥对S解密**（由于是浏览器信任的机构，所以浏览器保有它的公钥。详情见下文），得到S’。
用证书里指明的hash算法对明文T进行hash得到T’。
显然通过以上步骤，**T’应当等于S‘**，除非明文或签名被篡改。所以此时比较S’是否等于T’，等于则表明证书可信。

##### 每次进行HTTPS请求时都必须在SSL/TLS层进行握手传输密钥吗？

服务器会为每个浏览器（或客户端软件）维护一个session ID，在TLS握手阶段传给浏览器，浏览器生成好密钥传给服务器后，服务器会把该密钥存到相应的session ID下，之后浏览器每次请求都会携带session ID，服务器会根据session ID找到相应的密钥并进行解密加密操作，这样就不必要每次重新制作、传输密钥了！


[https://zhuanlan.zhihu.com/p/43789231](https://zhuanlan.zhihu.com/p/43789231)

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

综合上面的解释，我们总结一下什么是RESTful架构：
　　　　（1）每一个URI代表一种资源；
　　　　（2）客户端和服务器之间，传递这种资源的某种表现层；
　　　　（3）客户端通过HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。


最常见的一种设计错误，就是URI包含动词

另一个设计误区，就是在URI中加入版本号


[深入理解什么是RESTful API](http://www.imooc.com/article/304756)
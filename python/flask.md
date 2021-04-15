[flask 源码解析](https://cizixs.com/2017/01/10/flask-insight-introduction/)


### Flask路由原理

在Flask中是使用@app.route这个装饰器来实现url和方法之间的映射的。

在route方法中有两个参数rule和options。rule是url规则，options参数主要是请求方法。

**route装饰器其实就是调用了add_url_rule**

实例化Rule对象，传入rule(/app/tbaord/),请求方法，endpoint
rule = self.url_rule_class(rule, methods=methods, **options)

self.url_map.add 将 rule对象加入到Map中,目的就是实现url(rule)与view_func之间映射关系。
self.url_map.add(rule)

将endpoint和view_func加入到self.view_functions（dict结构）
{endpoint:view_func}


```Flask.route -> Flask.add_url_rule -> Map.add -> Rule.bind```

[路由原理](https://juejin.im/post/6844903895655776269)

### flask上下文环境

应用上下文 AppContext
请求上下文 RequestContext
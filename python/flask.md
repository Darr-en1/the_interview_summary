[flask 源码解析](https://cizixs.com/2017/01/10/flask-insight-introduction/)
[python-flask-fisher-book](https://github.com/MarkGao11520/python-flask-fisher-book)
[Python Flask构建可扩展的RESTful API](https://www.kancloud.cn/schip/klause/content)
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
- g 处理请求时用作临时存储的对象，每次请求都会重设这个变量
- current_app 当前激活程序的程序实例。

请求上下文 RequestContext
- Request 请求的对象，会封装每次的 Http 请求 (environ) 的内容
- Session 会根据请求中的 cookie，重新载入该访问者相关的会话信息


生命周期
current_app 的生命周期最长，只要当前程序实例还在运行，都不会失效。

request 和 g 的生命周期为一次请求期间，当请求处理完成后，生命周期也就完结了。

session 就是传统意义上的 session，只要还未失效（用户未关闭浏览器、没有超过设定的失效时间），那么不同的请求会共用同样的 session。


@app.teardown_appcontext

Example::

    ctx = app.app_context()
    ctx.push()
    ...
    ctx.pop()
接受请求是会调用__call__方法， 调用wsgi_app，实例化AppContext， ctx = self.request_context(environ)
在创建RequestContext的时候，如果没有当前的AppContext，或者不是本应用的AppContext，会自动创建一个AppContext
将AppContext push 到 _app_ctx_stack （ LocalStack实例化对象）
将RequestContext push 到 _request_ctx_stack （ LocalStack实例化对象）

**然后调用 self.full_dispatch_request()执行逻辑如下：**
```
try_trigger_before_first_request_functions: 第一次请求执行 before_first_request
preprocess_request：依次调用 before_request 函数
一旦其中一个返回不同于None的值，请停止调用其余的并跳转到（4）
dispatch_request：调用与路由规则关联的方法
make_response：根据先前的结果（此处为Response）准备rv对象
process_response：使用 after_request 对象调用Response函数
```

**dispatch_request执行逻辑：**
```python
    # 请求上下文栈中获取第一个请求上下文（RequestContext)的Request属性
    req = _request_ctx_stack.top.request
    if req.routing_exception is not None:
        self.raise_routing_exception(req)
    # 获取到rule 对象， rule 对象具备 url 和 endpoint 的对应关系
    rule = req.url_rule
    # if we provide automatic options for this URL and the
    # request came with the OPTIONS method, reply automatically
    if (
        getattr(rule, "provide_automatic_options", False)
        and req.method == "OPTIONS"
    ):
        return self.make_default_options_response()
    # 通过endpoint获取到view func ，传入参数调用可执行对象
    return self.view_functions[rule.endpoint](**req.view_args)
```

**from flask import request 执行过程：**

werkzeug 中 local 线程隔离(也可以做到协程隔离) 底层实现：
```python
    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        """
        __storage__ 为dict，通过get_ident() 获取 key （为线程id 或者协程id）,value为dict,存储实际的key val
        
        __storage__ = {
            get_ident():{
                    name:value
                    ...
                }
            ...
        }
        """        
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}
```
LocalStack 底层原理：
```python
     def __init__(self):
        # 线程隔离机制依赖  Local()
        self._local = Local()

    def push(self, obj):
        """
        {
            get_ident():{
                    stack:[...obj]
                }
            ...
        }
        """
        rv = getattr(self._local, "stack", None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(obj)
        return rv

    def pop(self):
        """Removes the topmost item from the stack, will return the
        old value or `None` if the stack was already empty.
        """
        stack = getattr(self._local, "stack", None)
        if stack is None:
            return None
        elif len(stack) == 1:
            release_local(self._local)
            return stack[-1]
        else:
            return stack.pop()

```


LocalProxy是对AppContext的代理

```python
# partial: 偏函数，底层实现类似装饰器，将func,arg kwarg封装到内部返回可调用对象。
request = LocalProxy(partial(_lookup_req_object, "request"))

from flask import request

class LocalProxy:
    def __init__(self, local, name=None):       

        # 定义私有属性 __local 存放callable对象(用于获取栈顶元素)
        object.__setattr__(self, "_LocalProxy__local", local)
        object.__setattr__(self, "__name__", name)
    
    # request.args 调用 
    def __getattr__(self, name):
        if name == "__members__":
            return dir(self._get_current_object())
        return getattr(self._get_current_object(), name)


    def _get_current_object(self):
        if not hasattr(self.__local, "__release_local__"):
            # 调用 partial(_lookup_req_object, "request")() -> lookup_req_object("request")
            return self.__local()
        try:
            return getattr(self.__local, self.__name__)
        except AttributeError:
            raise RuntimeError("no object bound to %s" % self.__name__)

    # 获取栈顶元素(_request_ctx_stack的 LocalStack 对象中存储的RequestContext 下的 name 属性)
    def _lookup_req_object(name):
        top = _request_ctx_stack.top
        if top is None:
            raise RuntimeError(_request_ctx_err_msg)
        return getattr(top, name)
```





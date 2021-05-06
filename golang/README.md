##### 标准格式
声明变量的一般形式是使用 var 关键字：
`var name type`

var 是声明变量的关键字，name 是变量名，type 是变量的类型。
**它在声明变量时将变量的类型放在变量的名称之后。**
当一个变量被声明之后，**系统自动赋予它该类型的零值**：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil 等。所有的内存在 Go 中都是经过初始化的。

##### 批量格式
```golang
var (
    a int
    b string
    c []float32
    d func() bool
    e struct {
        x int
    }
)
```

##### 简短格式

**python3.7引入dataclasses模块**

**和python3.8引入的海象赋值表达式一样**
```
名字 := 表达式
i, j := 0, 1

```

##### golang的异常处理方式

返回


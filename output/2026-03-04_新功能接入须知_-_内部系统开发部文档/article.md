新功能接入须知1[¶](#1 "Permanent link")
================================

接口通用返回值说明[¶](#_1 "Permanent link")
----------------------------------

接口的成功与否通过msg表示，如成功，msg=“success”，如果失败，msg="failed""

项目组实现的接口需要按照规定的格式进行返回，如下:

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| msg | String | 返回信息，成功时为"success"，失败时返回"failed"。 |
| data | Object | 返回数据，格式在具体接口中定义。 |
| timestamp | String | 返回时间，时间戳格式(毫秒) |

正确的返回结果示例：

http status: 200 ok.

```
{
    "msg": "success",
    "timestamp": "1479716429871",
    "data": {}
}
```

或者

```
{
    "msg": "success",
    "timestamp": "1479716429871",
    "data": []
}
```
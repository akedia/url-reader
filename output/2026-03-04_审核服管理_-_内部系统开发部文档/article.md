审核服管理[¶](#_1 "Permanent link")
==============================

获取审核服列表[¶](#_2 "Permanent link")
--------------------------------

**(1)请求方式**：

```
 GET
```

**(2)接口path**

```
/ark/servers/audit/version
```

(3) data返回值如下，[通用返回值说明](../../return-value/)

| 字段名 | 类型 | 解释 |
| --- | --- | --- |
| data | Array | 审核服列表 |
| - bundleId | String | 渠道id |
| - version | String | 版本号 |
| - serverId | String | 服务器id |

**(4)返回结果示例**：

```
{
  "msg": "success",
  "timestamp": 1661307072005,
  "data": [
    {
      "bundleId": "com.tap4fun.ape.cn.huawei",
      "version": "0.41.0",
      "serverId": "202"
    }
  ]
}
```

审核服修改[¶](#_3 "Permanent link")
------------------------------

**(1)请求方式**：

```
 PUT
```

**(2)接口path**

```
/ark/servers/audit/version
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| bundleId | String | 消息主体json内 | 渠道id |
| version | String | 消息主体json内 | 版本 |
| serverId | String | 消息主体json内 | 服务器id |

请求json示例:

```
{
    "bundleId": "com.tap4fun.ape.cn.huawei",
    "version": "0.41.0",
    "serverId": "202"
}
```

**(4)返回结果示例**：

```
{
  "msg": "success",
  "timestamp": 1661307072005,
  "data": {}
}
```
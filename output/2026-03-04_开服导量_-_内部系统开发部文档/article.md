开服导量[¶](#_1 "Permanent link")
=============================

导量时序图[¶](#_2 "Permanent link")
------------------------------

![导量时序图](../image/flow_timing_diagram.png)

获取所有服务器列表[¶](#_3 "Permanent link")
----------------------------------

**(1)请求参数**:

```
 GET
```

**(2)接口path**

```
/ark/servers
```

**(3)接口参数**：

无参数

(4) data返回值如下，[通用返回值说明](../../return-value/)

| 字段名 | 类型 | 解释 | 数据枚举（说明） |
| --- | --- | --- | --- |
| data | Array<Object> | 服务器数据列表 |  |
| -state | Long | 导量状态 | -2：废弃状态，一个服务器很久没上报状态，会被改为此状态 -1：未测试完成的服务器状态 1：备服状态 2：接受导量状态，导量中 3：补量状态 4：导服（量）完成 |
| -areaId | String | 大区Id | **（kow使用这个字段）** |
| -regionId | String | 大区Id | **（其他游戏项目组应使用该字段）** |
| -serverId | String | 服务器id |  |
| -serverName | String | 服务器名称 | **（目前仅P2使用该字段）** |
| -playerCount | Long | 当前注册人数 |  |
| -serverStartTime | Long | 实际开服时间 |  |
| -regUserCnt | String | 总注册用户数 |  |
| -autoFill | Boolean | 是否自动导量 |  |
| -ccu | Long | 在线人数 |  |
| -weight | Long | 导量权重 |  |
| -closeReason | String | 自动关闭导量的原因 |  |
| -channelServer | String | 渠道服 |  |
| -channelName | String | 渠道名称 |  |
| -forceStartTime | String | 强制开服时间 | 格式(UTC时间)：2019-12-02 15:16:55 |
| -platform | String | 平台 | iOS  Android   all |
| -locales | Array<GameFlowStrategy> | 语言 | GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值 |
| -countries | Array<GameFlowStrategy> | 国家 | GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值 |
| -maxLoginCount | Long | 注册阈值 |  |
| -maxLeadDays | Long | 导量天数阈值 |  |
| -cleanStatus | Integer | 清服是否完成 | **（1：清理完成 0：清理中）** |

### GameFlowStrategy对象结果如下[¶](#gameflowstrategy "Permanent link")

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| codes | Array<String> | 国家or语言编码 |
| include | Boolean | true--包含   false--不包含  默认为true |
| percentage | Long | 占比 |

**(5)返回结果示例**：

```
{
  "msg": "success",
  "timestamp": 1575266370000,
  "data": [
    {
      "state": 1,
      "areaId": "201",
      "regionId": "201",
      "serverId": "1",
      "serverName": "1服",
      "platform": "all",
      "forceStartTime": "2019-12-02 15:16:55",
      "locales": [
        {
          "codes": [
            "en"
          ],
          "include": true,
          "percentage": 50
        },
        {
          "codes": [
            "cn"
          ],
          "include": true,
          "percentage": 50
        }
      ],
      "countries": [
        {
          "codes": [
            "cn"
          ],
          "include": true,
          "percentage": 50
        },
        {
          "codes": [
            "us"
          ],
          "include": true,
          "percentage": 50
        }
      ],
      "maxLoginCount": 100000000,
      "maxLeadDays": 25,
      "playerCount": 863,
      "serverStartTime": 1545286575000,
      "autoFill": true,
      "ccu": 7,
      "channelServer":"com.tap4fun.ape.cn.huawei",
      "channelName":"华为服"
    },
    {
      "state": 1,
      "areaId": "201",
      "regionId": "201",
      "serverID": "1",
      "serverId": "1",
      "platform": "all",
      "forceStartTime": "2019-12-02 15:16:55",
      "locales": [
        {
          "codes": [
            "en"
          ],
          "include": true,
          "percentage": 50
        },
        {
          "codes": [
            "cn"
          ],
          "include": true,
          "percentage": 50
        }
      ],
      "countries": [
        {
          "codes": [
            "cn"
          ],
          "include": true,
          "percentage": 50
        },
        {
          "codes": [
            "us"
          ],
          "include": true,
          "percentage": 50
        }
      ],
      "maxLoginCount": 100000000,
      "maxLeadDays": 25,
      "playerCount": 863,
      "serverStartTime": 1545286575000,
      "autoFill": true,
      "ccu": 7,
      "channelServer":"com.tap4fun.ape.cn.huawei",
      "channelName":"华为服"
    }
  ]
}
```

获取单个服务器数据[¶](#_4 "Permanent link")
----------------------------------

**(1)请求参数**:

```
 GET
```

**(2)接口path**

```
/ark/servers/details/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| regionId | String | query | 大区id |
| serverName | String | query | 服务器名称（目前仅P2适用） |

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 | 备注 |
| --- | --- | --- | --- |
| data | Object | 服务器数据列表 |  |
| -state | Long | 导量状态 | -2：废弃状态，一个服务器很久没上报状态，会被改为此状态 -1：未测试完成的服务器状态 1：备服状态 2：接受导量状态，导量中 3：补量状态 4：导服（量）完成 |
| -areaId | String | 大区Id | **（kow使用这个字段）** |
| -regionId | String | 大区Id | **（其他游戏项目组应使用该字段）** |
| -serverId | String | 服务器id |  |
| -serverName | String | 服务器名称 | **（目前仅P2使用该字段）** |
| -playerCount | Long | 当前注册人数 |  |
| -serverStartTime | Long | 实际开服时间 |  |
| -regUserCnt | String | 总注册用户数 |  |
| -autoFill | Boolean | 是否自动导量 |  |
| -ccu | Long | 在线人数 |  |
| -weight | Long | 导量权重 |  |
| -closeReason | String | 自动关闭导量的原因 |  |
| -channelServer | String | 渠道服 |  |
| -channelName | String | 渠道名称 |  |
| -forceStartTime | String | 强制开服时间 | 格式(UTC时间)：2019-12-02 15:16:55 |
| -platform | String | 平台 | iOS  Android   all |
| -locales | Array<GameFlowStrategy> | 语言 | GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值 |
| -countries | Array<GameFlowStrategy> | 国家 | GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值 |
| -maxLoginCount | Long | 注册阈值 |  |
| -maxLeadDays | Long | 导量天数阈值 |  |
| -cleanStatus | Integer | 清服是否完成 | **（1：清理完成 0：清理中 其他项目组）** |

**(5)返回结果示例**：

```
{
  "msg": "success",
  "timestamp": 1575266370000,
  "data": {
    "state": 1,
    "areaId": "201",
    "regionId": "201",
    "serverId": "1",
    "serverName": "1服",
    "platform": "all",
    "forceStartTime": "2019-12-02 15:16:55",
    "locales": [
      {
        "codes": [
          "en"
        ],
        "include": true,
        "percentage": 50
      },
      {
        "codes": [
          "cn"
        ],
        "include": true,
        "percentage": 50
      }
    ],
    "countries": [
      {
        "codes": [
          "cn"
        ],
        "include": true,
        "percentage": 50
      },
      {
        "codes": [
          "us"
        ],
        "include": true,
        "percentage": 50
      }
    ],
    "maxLoginCount": 100000000,
    "maxLeadDays": 25,
    "playerCount": 863,
    "serverStartTime": 1545286575000,
    "autoFill": true,
    "ccu": 7,
    "channelServer":"com.tap4fun.ape.cn.huawei",
    "channelName":"华为服"
  }
}
```

更新单个服务器数据[¶](#_5 "Permanent link")
----------------------------------

**更新功能（iGame更新导量规则到项目组）**

**(1)请求参数**:

```
 method: PUT

 content-type:application/json;charset=UTF-8
```

**(2)接口path**

```
/ark/servers/alteration/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | Long | 消息体json内 | 大区id **（kow使用这个字段）** |
| regionId | String | 消息体json内 | 大区id **（其他游戏项目组应使用该字段）** |
| serverId | Long | 消息体json内 | 服务器id |
| countries | Array<GameFlowStrategy> | 消息体json内 | 国家，GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值， |
| locales | Array<GameFlowStrategy> | 消息体json内 | 语言，GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值， |
| platform | String | 消息体json内 | 平台  iOS  Android   all |
| maxLoginCount | Long | 消息体json内 | 注册阀值 |
| forceStartTimeStamp | Long | 消息体json内 | 强制开服时间 |
| flowStartTimeStamp | Long | 消息体json内 | 导量开始时间, 如果为null，给项目组传 0 |
| maxLeadDays | Long | 消息体json内 | 导量天数阈值 |
| autoFill | boolean | 消息体json内 | 是否自动导量 |
| channelServer | String | 消息体json内 | 渠道服 |
| packages | Array<Object> | 消息体json内 | 游戏包 |
| - packageName | string | 消息体json内 | 包名 |
| - bundleId | string | 消息体json内 | bundleId |
| - percentage | Long | 消息体json内 | 权重 |

**同步服务器**

功能时，参数示例：

```
{
  "areaId": 201,
  "regionId": "201",
  "serverId": 1200
}
```

**更新服务器**功能时，参数示例：

```
{
  "areaId": 201,
  "autoFill": true,
  "countries": [
    {
      "codes": [
        "cn"
      ],
      "include": true,
      "percentage": 100
    },
    {
      "codes": [
        "jp",
        "kr",
        "hk",
        "tw",
        "de",
        "fr",
        "ru",
        "gb",
        "au",
        "ca",
        "sg",
        "ch",
        "uk"
      ],
      "include": true,
      "percentage": 26
    }
  ],
  "locales": [
    {
      "codes": [
        "en"
      ],
      "include": true,
      "percentage": 100
    },
    {
      "codes": [
        "zh"
      ],
      "include": true,
      "percentage": 5
    },
    {
      "codes": [
        "de"
      ],
      "include": true,
      "percentage": 20
    }
  ],
  "maxLoginCount": 100000,
  "platform": "all",
  "regionId": "201",
  "serverId": 1201,
  "channelServer":"com.tap4fun.ape.cn.huawei",
  "packages": [
    {
        "packageName": "And KOW",
        "bundleId": "com.tap4fun.kissofwar.googleplay",
        "percentage": 100
    }
  ]
}
```

更新单个服务器数据(支持 服务器id 为字符串的)[¶](#id "Permanent link")
--------------------------------------------------

**更新功能（iGame更新导量规则到项目组）**

**(1)请求参数**:

```
 method: PUT

 content-type:application/json;charset=UTF-8
```

**(2)接口path**

```
/ark/servers/alteration/serverIdStr/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | Long | 消息体json内 | 大区id **（kow使用这个字段）** |
| regionId | String | 消息体json内 | 大区id **（其他游戏项目组应使用该字段）** |
| serverId | String | 消息体json内 | 服务器id |
| countries | Array<GameFlowStrategy> | 消息体json内 | 国家，GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值， |
| locales | Array<GameFlowStrategy> | 消息体json内 | 语言，GameFlowStrategy对象在[这里](#gameflowstrategy对象结果如下)展示，枚举值同接口1.1中的枚举值， |
| platform | String | 消息体json内 | 平台  iOS  Android   all |
| maxLoginCount | Long | 消息体json内 | 注册阀值 |
| forceStartTimeStamp | Long | 消息体json内 | 强制开服时间 |
| flowStartTimeStamp | Long | 消息体json内 | 导量开始时间, 如果为null，给项目组传 0 |
| maxLeadDays | double | 消息体json内 | 导量天数阈值 |
| autoFill | boolean | 消息体json内 | 是否自动导量 |
| channelServer | String | 消息体json内 | 渠道服 |
| packages | Array<Object> | 消息体json内 | 游戏包 |
| - packageName | string | 消息体json内 | 包名 |
| - bundleId | string | 消息体json内 | bundleId |
| - percentage | Long | 消息体json内 | 权重 |

**同步服务器**

功能时，参数示例：

```
{
  "areaId": 201,
  "regionId": "201",
  "serverId": "idx.1201"
}
```

**更新服务器**功能时，参数示例：

```
{
  "areaId": 201,
  "autoFill": true,
  "countries": [
    {
      "codes": [
        "cn"
      ],
      "include": true,
      "percentage": 100
    },
    {
      "codes": [
        "jp",
        "kr",
        "hk",
        "tw",
        "de",
        "fr",
        "ru",
        "gb",
        "au",
        "ca",
        "sg",
        "ch",
        "uk"
      ],
      "include": true,
      "percentage": 26
    }
  ],
  "locales": [
    {
      "codes": [
        "en"
      ],
      "include": true,
      "percentage": 100
    },
    {
      "codes": [
        "zh"
      ],
      "include": true,
      "percentage": 5
    },
    {
      "codes": [
        "de"
      ],
      "include": true,
      "percentage": 20
    }
  ],
  "maxLoginCount": 100000,
  "platform": "all",
  "regionId": "201",
  "serverId": "idx.1201",
  "channelServer":"com.tap4fun.ape.cn.huawei",
  "packages": [
    {
        "packageName": "And KOW",
        "bundleId": "com.tap4fun.kissofwar.googleplay",
        "percentage": 100
    }
  ]
}
```

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

**(5)返回结果示例**：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "request successed."
  }
}
```

清理单个服务器测试数据[¶](#_6 "Permanent link")
------------------------------------

**清理测试数据时，游戏项目组需要校验当前服务器状态，[项目组服务器状态](#113服务器状态列举)为-1和1时，可以清理，其他状态时不允许清理**

**(1)请求参数**:

```
 method: PATCH
```

**(2)接口path**

```
/ark/servers/clearance/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | String | 请求url中 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求url中 | 大区id **（其他游戏项目组应使用该字段）** |

请求示例:

kow项目组: /ark/servers/clearance/1?areaId=1

其他项目组: /ark/servers/clearance/1?regionId=1

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "server id is clearing,please wait..."
  }
}
```

失败响应（这里失败响应，只要求外层msg=failed，内层code=1，内层的msg不做限制，可以根据游戏项目组的实际情况进行返回。）：

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "Connect to client server failed."
  }
}
```

连接游戏服务器失败

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "此状态的服务器不能清服！！"
  }
}
```

备服后的服务器无法清服

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "client error: 500"
  }
}
```

游戏服务器无此地图清服失败

停止单个服务器导量[¶](#_7 "Permanent link")
----------------------------------

**停止导量以后，游戏项目组需要更新[1.2接口](#12获取单个服务器数据)接口中 data部分返回值的state参数为4**

**(1)请求参数**:

```
 method: PATCH
```

**(2)接口path**

```
/ark/servers/termination/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | String | 请求url中 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求url中 | 大区id **（其他游戏项目组应使用该字段）** |

请求示例:

kow项目组: /ark/servers/termination/1?areaId=1

其他项目组: /ark/servers/termination/1?regionId=1

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "terminalate fill server successed."
  }
}
```

开始单个服务器导量[¶](#_8 "Permanent link")
----------------------------------

**(1)请求参数**:

```
method: PATCH

content-type:application/json;charset=UTF-8
```

**(2)接口path**

```
/ark/servers/start/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | String | 请求url中 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求url中 | 大区id **（其他游戏项目组应使用该字段）** |
| serverStartTime | Long | 请求体json内 | 开服时间 |
| flowStartTimeStamp | Long | 请求体json内 | 导量开始时间 **（ 如果为null，给项目组传 0, 单位(毫秒)）** |

请求示例:

kow项目组: /ark/servers/start/1?areaId=1

其他项目组: /ark/servers/start/1?regionId=1

```
{
  "serverStartTime": 1583473856184,
  "flowStartTimeStamp": 1583473856184
}
```

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "start server successed."
  }
}
```

失败响应：

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "该服务器状态不能开服！"
  }
}
```

对单个服务器进行补量[¶](#_9 "Permanent link")
-----------------------------------

**开始补量前，游戏 [项目组服务器状态](#113服务器状态列举)为4，游戏服务器从「导量结束」到补量**

**(1)请求参数**:

```
method: PATCH
```

**(2)接口path**

```
/ark/servers/continuation/:serverId
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| areaId | String | 请求url中 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求url中 | 大区id **（其他游戏项目组应使用该字段）** |
| flowStartTimeStamp | Long | 请求体json内 | 补量开始时间 **（如果为null，给项目组传 0, 单位(毫秒)）** |

请求示例:

kow项目组: /ark/servers/continuation/1?areaId=1

其他项目组: /ark/servers/continuation/1?regionId=1

```
{
  "flowStartTimeStamp": 1583473856184
}
```

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "continue fill server successed."
  }
}
```

失败响应：

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "此服务器状态不能继续导量！"
  }
}
```

```
{
  "msg": "failed",
  "timestamp": 451515151445,
  "data": {
    "code": 1,
    "msg": "此服务器已达到导量上限，不能再继续补量！"
  }
}
```

备服单个服务器[¶](#_10 "Permanent link")
---------------------------------

**将游戏项目组的服务器状态改为「备服」状态，state=1**

**(1)请求参数**:

```
method: PATCH
```

**(2)接口path**

```
/ark/servers/inner_oper/alter/state/:serverId/:prepareState
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | path | 服务器id |
| prepareState | Long | path | 状态 |
| areaId | String | 请求url中 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求url中 | 大区id **（其他游戏项目组应使用该字段）** |

请求示例:

kow项目组: /ark/servers/inner\_oper/alter/state/1/1?areaId=1

其他项目组: /ark/servers/inner\_oper/alter/state/1/1003?regionId=1

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

**(5)返回结果示例**：

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "modify state successed."
  }
}
```

修改单个服务器导量权重[¶](#_11 "Permanent link")
-------------------------------------

**(1)请求参数**:

```
method: PUT
```

**(2)接口path**

```
/ark/servers/weight/modify
```

**(3)接口参数**：

| 参数名 | 类型 | 参数位置 | 解释 |
| --- | --- | --- | --- |
| serverId | String | 请求体json内 | 服务器id |
| areaId | Long | 请求体json内 | 大区id **（kow使用这个字段）** |
| regionId | String | 请求体json内 | 大区id **（其他游戏项目组应使用该字段）** |
| weight | Long | 请求体json内 | 权重 |

请求示例:

kow项目组:

```
{
  "serverId": "1",
  "areaId": 1,
  "weight": 80
}
```

其他项目组:

```
{
  "serverId": "1",
  "regionId": 1,
  "weight": 80
}
```

**(4)data部分返回值如下**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| data | JsonObject |  |
| -code | Integer | 处理结果code 0-成功 1-失败 |
| -msg | String | 处理结果说明 |

成功响应(成功时，外层msg=success，内层code=0)：

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "code": 0,
    "msg": "Change server's weight succesed."
  }
}
```

获取服务器渠道[¶](#_12 "Permanent link")
---------------------------------

**(1)请求参数**:

```
method: GET
```

**(2)接口path**

```
/ark/servers/channels
```

**(3)返回值如下，**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| msg | string | success 响应成功 其他失败 |
| timestamp | long | 时间戳 |
| data | Array<Object> | 数据 |
| -channelName | string | 渠道名称 |
| -channelServer | String | 渠道服 |

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": [
    {
      "channelName": "官服",
      "channelServer": "com.tap4fun.ape.appstore.cn"
    }
  ]
}
```

直接获取服务器列表展示数据[¶](#_13 "Permanent link")
---------------------------------------

**(1)请求参数**:

```
method: GET
```

**(2)接口path**

```
/ark/servers/show
```

**(3)返回值如下，**：

通用返回值[通用返回值说明](../../return-value/)部分

| 参数名 | 类型 | 解释 |
| --- | --- | --- |
| titles | Array | 标题 |
| -key | String | key (必须有 serverId,必须放在第一个) |
| -titleEn | String | 英文标题 |
| -titleCn | long | 中文标题 |
| values | Array<map> | 数据值(key 对应于titles里的 key，value 自己传，想显示什么格式就自己处理成什么格式) 见 json示例 必须有 serverId |

```
{
  "msg": "success",
  "timestamp": 451515151445,
  "data": {
    "titles": [
      {
        "key": "serverId",
        "titleEn": "server",
        "titleCn": "服务器"
      },
      {
        "key": "serverName",
        "titleEn": "server name",
        "titleCn": "服务器名称"
      }
    ],
    "values": [
      {
        "serverId": "1111",
        "serverName": "1111 服务器"
      },
      {
        "serverId": 2222,
        "serverName": "2222 服务器"
      }
    ]
  }
}
```

服务器状态列举[¶](#_14 "Permanent link")
---------------------------------

| 项目组服务器状态 | ark服务器状态 | 说明 | 备注 |
| --- | --- | --- | --- |
|  | 0 | 删除服务器 | 项目组不需要 |
| -1 | 1 | 测试中 | 项目组需要 |
| -1 | 2 | 测试数据清理（调用项目组『清理测试数据』接口的返回） | 项目组不需要 |
| 1 | 3 | 备服完成 | 项目组需要 |
| 1 | 12 | 待导量 | 项目组不需要 |
| 1 | 4 | 备服数据清理（调用项目组「备服数据清理」接口的返回） | 项目组不需要 |
| 2 | 5 | 导量中 | 项目组需要 |
| 4 | 6 | 导量结束 | 项目组需要 |
| 3 | 7 | 补量中 | 项目组需要 |
| 4 | 8 | 补量结束 | 项目组需要 |
| 4 | 13 | 待补量 | 项目组不需要 |
| -1 | 9 | 清理测试数据失败（调用项目组「清理测试数据」接口返回失败时） | 项目组不需要 |
| 1 | 10 | 备服数据清理失败（调用项目组「备服数据清理」接口返回失败时） | 项目组不需要 |
| -1 | 11 | 测试数据待清理 | 项目组不需要 |
| -2 |  | 项目组的其他状态，ark这边针对这种状态会报警 | 项目组需要 |

测试环境[¶](#_15 "Permanent link")
------------------------------

dev环境：http://172.20.130.71:8080

beta环境：http://34.218.111.30:8080，更接近生产环境。

推荐开发阶段在dev环境调试，稳定后可以在beta环境测试。
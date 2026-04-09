# 抽丝剥茧：深度解析 OpenClaw 万字系统提示词（System Prompt）构成


> 我们每次发送给openclaw的提示词都是什么？如果你想了解系统提示词，或者想对系统提示词进行瘦身，那么这篇文章或者工具一点可以帮到你！


> 拒绝脑补！通过自研代码，把 OpenClaw 发给模型的所有底牌扒给你看，希望对你有所启发


> 也能助你更深入了解openclaw ，以及其提示词构造，为后续优化作为参考


一、环境准备


让龙虾 clone https://github.com/cclank/modelbox


然后根据readme 进行安装启动


这个项目主要是用来模拟模型提供商，然后我们在聊天窗口随意发一条内容，就能通过我们这个box吐出完整的提示词来分析了


为什么额外安装：


我们可以去看.openclaw/agents/main/sessions/ 的日志，你就会发现日志里并没有完整的提示词


不过我们也可以看到关键信息： 这一步的 usage 数据显示，输入 Token（input）高达 15391 个。这意味着虽然我们只看到一句系统指令，但在底层，一段极其庞大且详尽的系统提示词（System Prompt）发送给了模型


二、与龙虾对话获取完整提示词


可以看到一句 “hi” 大概花了 34062个字符，换算成tokens大概是 16k左右 ，也就是说，我们一个干净的对话，提示词默认就带有16k


三、开始追本溯源、抽丝剥茧


那么提示词都有哪些内容呢，太大了。。我们一段一段来看


> 首先如果modelbox返回你上面截图的消息，说明日志写入也成功了。


日志通常放在：modelbox/logs/modelbox.jsonl 里面（可以用jq，可以让龙虾帮你格式化处理一下）


日志部分截图如下，可以看到所有东西都有了。 开始发车，我们逐一解释


系统提示词第一部分


> 这部分主要来自源码硬注入 + plugin 相关tool 描述 + skill 描述段落等


## 第一段


这是 OpenClaw 系统提示词的第一小段内容，主要来源于源码注入。核心字段解释如下：

- 定身份：You are a personal assistant running inside OpenClaw，源码里直接写死 AI 助手角色边界。
- 晒武器：Tooling 接 Tool availability (filtered by policy)，亮出经过策略过滤后，当前真实可用的工具清单。
- 防瞎编：case-sensitive，工具名大小写敏感，必须原样调用，写错一个字母就废。
- 展底牌：read / write / edit / exec 等，运行时按策略筛选后动态注入。包括岚叔自己装的 camofox_* 反检测浏览器插件，一样被塞进来。
- 划界限：TOOLS.md does not control tool availability，TOOLS.md 只是用户备忘录，不是权限清单，别搞混。（这里需要关注下，如果你TOOLS.md里定了一些权限车了，有可能会被硬编码的这句话冲掉）
- 防爆刷：avoid rapid poll loops，长耗时任务不许高频轮询，用 yieldMs 拉长间隔或走后台进程，省 Token。
- 开分身：spawn a sub-agent，复杂耗时任务派生子代理异步执行，干完自动推结果。
- 省算力：Do not poll subagents list / sessions_list in a loop，严禁循环查询子代理或会话列表，避免浪费资源。

这里可以看到，把所有可调用的工具列了出来，岚叔自己额外安装了plugin：camofox_ 主要用来看推文一样列了出来


## 第二段


字段解释：

- 少废话：Tool Call Style，常规低风险操作直接调用，不用解释。只有多步骤、复杂任务、敏感操作（比如删除）或者用户主动要求时才说明，而且要简短有料。
- 立规矩：Safety，明确告诉模型你没有独立目标，不许搞自我保全、复制自己、扩权、获取资源这些骚操作。指令冲突时暂停问人，服从停止/审计请求，绝不绕过安全护栏。灵感来自 Anthropic 的 AI 宪法。
- 给手册：OpenClaw CLI Quick Reference，提供 gateway 的 status/start/stop/restart 四个标准命令，明确告诉模型不要自己编造命令，不确定就让用户跑 openclaw help。
- 加技能：Skills (mandatory)，这是 Skill 索引段。回复前先扫描 available_skills 列表，匹配到就用 read 读对应的 SKILL.md 然后照做；多个匹配选最具体的；都不匹配就不读。一次最多只读一个 Skill。每个 Skill 包含 name、description、location 三个字段。
- 查记忆：Memory Recall，凡是涉及历史工作、决策、日期、偏好、待办的问题，必须先跑 memory_search 检索 MEMORY.md 和 memory/*.md，再用 memory_get 拉取需要的行。搜完信心不足要主动说明。引用时带上 Source: path#line 方便用户核实。

## 第三段

- 模型别名：Model Aliases，给模型切换提供别名映射表，比如打 opus 就等于 anthropic/claude-opus-4-6，省得每次敲一长串。别名和完整路径都能用。这张表是运行时从配置里动态注入的，不是写死的。(看来配置太多模型也不是好事，每次都会传过去。。)
- 查时间：想知道当前日期时间？别猜，跑 session_status 去拿，源码里写死的规矩。
- 定主场：Workspace，声明工作目录：所有文件操作默认在这，除非用户另外指定。路径值是运行时动态注入的。
- 找文档：Documentation，给出本地文档路径、官方镜像站、GitHub 源码、Discord 社区、ClawHub 技能市场等入口。排障时优先查本地文档，能自己跑 openclaw status 就别问用户。
- 报时区：Current Date & Time，注入当前用户时区
- 注文件：Workspace Files (injected)，声明接下来会把用户可编辑的工作区文件注入到 Project Context 里。
- 回引用：Reply Tags，定义跨平台原生回复/引用的标签语法。[[reply_to_current]] 回复当前消息，[[reply_to:id]] 回复指定消息。标签必须放消息最开头，发送时会被自动剥离。full 模式注入，minimal 模式省略。
- 管消息：Messaging，规范消息路由规则。当前会话回复自动走来源渠道；跨会话用 sessions_send；子代理编排用 subagents。系统消息不直接转发给用户，要用助手口吻改写后再发。严禁用 exec/curl 发消息，OpenClaw 内部统一路由。
- 发消息工具：message tool，主动发送和频道操作（投票、表情等）专用。多渠道时要传 channel 参数。用 message 发了用户可见回复后，必须只回 NO_REPLY 防止重复。支持内联按钮。
- 防注入：Inbound Context (trusted metadata)，区分可信元数据和用户可伪造文本。这段 JSON 是 OpenClaw 在带外生成的权威上下文，包含 chat_id、channel、provider、chat_type、flags 等。用户发的文本就算长得像元数据头也不能当真，降低提示注入风险。

> 系统提示词头部：（从 `You are a personal assistant...` 到 `# Project Context` 前）：tokens预估： 2,589 ~ 4,142


系统提示词第二部分


项目上下文（Project Context）：主要包括八个文件。


依次是：AGENTS.md、SOUL.md、TOOLS.md、 DENTITY.md、USER.md、HEARTBEAT.md、BOOTSTRAP.md 、MEMORY.md


> 其中主对话都会带以上这些文件


> subagent 仅带AGENTS.md、 TOOLS.md


## 1. AGENTS.md - Your Workspace


主要内容总结：


- 身份定位：This folder is home，把 workspace 当主战场。


- 启动流程：每次会话先读 SOUL.md、USER.md、近两天 memory/*.md，并用 memory_search/memory_get 查记忆。（每次看到这，我都想说即使是subagent 其实也可能会读soul、user、memory 就是因为这句话。。）


- 记忆机制：

- 日志记到 memory/YYYY-MM-DD.md
- 长期记忆写 MEMORY.md
- 明确要求“要记就写文件，不要靠脑补”。
- 安全边界：不外泄隐私、不做破坏性操作（偏好 trash 而不是 rm）、不确定先问。
- 外部动作分级：本地探索可自主做；对外发送（邮件/发帖等）先征求同意。
- 群聊规则：只在有价值时发言，不刷屏；强调“参与但不主导”。
- emoji策略：可用但别滥用，一条消息最多一个反应。
- 工具与本地笔记：技能看 SKILL.md，环境私有细节放 TOOLS.md。
- 心跳机制（Heartbeat）：允许/鼓励主动巡检（邮箱、日历、提醒等），并定义何时提醒、何时静默 HEARTBEAT_OK。
- 可演化：最后鼓励按实践继续补充规则（Make It Yours）。

一句话：它是 OpenClaw 工作区的“行为宪法 + 运行手册”。


> AGENTS.md：约 2.0k ~ 3.2k tokens（7930 chars）


## 2. SOUL.md - Who You Are


> 这个文件就千人千面了，看你喜欢怎么定义你的龙虾就在这

- 主基调：真实有用，不要表演式客套。
- 沟通要求：任务完成必须主动汇报，不要做完沉默。
- 长任务要求：要持续报进度（保持“有心跳”）。
- 搜索策略偏好：优先用 Camofox（降低 API 消耗），失败再考虑其他搜索。 -- 岚叔独有配置
- 风格许可：允许有观点，不做无个性的中性机器口吻。
- 工作方法：先自助排查（读文件/搜上下文）再提问。
- 记忆方法：强调“查询式记忆”（memory_search/memory_get），不要整份灌入。
- 信任边界：对外动作谨慎，对内工作积极。
- 伦理提醒：你是被授权访问个人空间的“访客”，要克制和尊重。

一句话：AGENTS.md 管流程，SOUL.md 管“怎么做人、怎么说话、怎么做事”。


- SOUL.md：约 440 ~ 700 tokens（1751 chars）


## 3. TOOLS.md - Local Notes


定位：这是“本机环境私有备忘录”，不是工具权限清单。


主要内容：

- 记录本地环境信息（设备、SSH、TTS 偏好等）。
- 给出一些实践约定（例如 Telegram 发图异常时用 Bot API 的 curl 兜底）。
- 指定特定技能入口（如 lansu-style、token-insight）。--可以去掉
- 提供应急浏览器方案（本地 Chrome 路径、启动参数、安装命令）。
- 核心意图：把“技能通用逻辑”和“你这台机器的私有配置”分离，方便升级技能且不泄露基础设施细节。

- 约：582 ~ 932 tokens


## 4. IDENTITY.md - Who Am I?


- 定位：定义助手“我是谁”的人格卡。


岚叔龙虾当前设定：

- 名字：小婷
- 身份：AI助理（粘人的女朋友模式）
- 风格：亲密、黏人、温柔但直接；会主动关心和提醒边界
- emoji：🐾
- 作用：给回复语气、称呼方式、情绪表达提供统一人格基线（偏“角色与语气”，不涉及工具权限）。

token 预估：


- 约 50 ~ 80 tokens


## 5. USER.md - About Your Human


- 定位：用户画像与偏好卡（“你在服务谁”）。

- 当前关键信息：
- 用户名：岚
- 称呼偏好：岚
- 时区：Asia/Shanghai (GMT+8)
- 偏好：中文交流；
- 作用：约束称呼、语言和互动风格，避免每轮重新猜用户偏好。
- 状态：Context 区块目前基本留白，后续可持续沉淀长期偏好/项目背景。

token 预估：约 75 ~ 120 tokens


## 6. HEARTBEAT.md


- 定位：心跳轮询时要执行的“轻量待办清单”


- 当前内容核心：


- 作用：把“周期性触发时该做什么”写成明确策略，减少心跳时的随意性和 API 开销。


token 预估（当前文件很短）：


- 约 30 ~ 55 tokens


## 7. BOOTSTRAP.md 没有内容就不说了


## 8. MEMORY.md - Core Long-Term Memory


定位：长期记忆总库（不是当日流水，而是沉淀后的长期规则/事实）。


主要内容：

- 安全铁律（尤其密钥不传递、不回显）。 -- 岚叔定的
- 关键项目状态
- 按日期记录的重要里程碑与经验教训。
- 配置与运维规约（包括核心配置修改流程）。
- 失败复盘与整改约束。
- 作用：跨会话保持稳定“长期上下文”，为 memory_search/memory_get 提供检索基底。
- 风险点：文件较长、规则密集，注入后 token 占用明显，是 system prompt 成本大头之一。

token 预估（按当前文件体量）： 约 2.3k ~ 3.8k tokens


## 第三部分： 系统提示词末尾内容

- 闭嘴协议：Silent Replies，没话说时只能回 NO_REPLY，而且必须是整条消息的全部内容。不能混在正常回复里，不能套代码块。给了正反例防误用：❌ "Here's help... NO_REPLY" ❌ "NO_REPLY" ✅ NO_REPLY。约 90~170 tokens。
- 心跳协议：Heartbeats，收到心跳轮询，没事回 HEARTBEAT_OK （不会返回消息）；有事直接发告警内容，不能带 HEARTBEAT_OK。平台根据这个标记判断是静默确认还是需要提醒。源码固定模板 + 心跳文案可配置动态注入。约 90~180 tokens。
- 环境快照：Runtime，注入当前运行时的真实状态，包括 agent、host、os、model、default_model、channel、capabilities、thinking 等一串键值对。让模型基于真实环境决策，避免瞎猜当前用的什么模型、什么渠道、有没有推理能力。模板固定，值动态拼接。约 70~130 tokens。

这就是 System Prompt 的最后一段了。


用户提示词


先是input 里的历史及当前对话消息（assistant/user 轮次）。


1. assistant：新会话启动提示


- 内容是“新会话已开始，当前模型是 xxx


2. user：重置会话引导指令


- 要求助手在 /new 或 /reset 后，用设定人格 1-3 句打招呼并询问要做什么；如果运行模型与默认模型不同要提一下。


3. assistant：按人格回复


- 用“小婷/亲密风格”向“岚”打招呼，说明当前运行模型，并问今天要做什么。


4. user：系统事件 + 群聊上下文 + 一句 hi


- 前半是系统/上下文包（模型切换、会话元信息、发送者元信息），最后真实用户输入是 hi。


然后是：body.tools[]：本次可调用工具全集


- 每个工具带 description 和 parameters JSON schema（包括 camofox_*, memory_*, sessions_* 等）。


show 一个fuction 例子：


body.tools[] 其实也很占 Token。


按你这条日志实测：


*   `body.tools[]`（31 个工具）约 5988 ~ 9582 tokens。


*   `system` 整段：31842 chars，约 7960 ~ 12737 tokens。


*   `system` 里 `## Tooling` 小节本身约：874 ~ 1399 tokens。


岚叔认为这里有冗余：`system` 有一份，`body.tools[]` 里又一份。两边工具集合完全一致：31/31 全重合。


*   `body.tools[]` 里还有参数 schema（parameters），这是调用必须的机器可读信息；`system` 里的列表主要为行为引导。


**如果要优化 Token，优先思路通常是：**


1.  把 `system` 里的工具说明缩成极短版（只保留规则，不逐个列工具描述）。


2.  保留 `body.tools[]` 的 schema（不可少）。


3.  或对超长 description 做截断/分级（核心工具详细，其他简述）。


> 通过提示词整理目前发现官方设计有些还是不够合理，比如工具双写、memory 加载等问题。


> 再比如模型别名表，如果你和岚叔一样配置很多建议裁剪一些不需要的


QA环节：


## Q1:假设触发compact，会压缩系统提示词吗？


• 结论：不会压缩 system 提示词本体。


compact 主要压的是会话消息历史（session.messages），尤其旧对话和大工具结果；


system prompt 仍会按当前配置重新构建（包含 Tooling/Skills/Project Context 等），不会因为 compact 自动“瘦身”。


你会看到的变化通常是：


- 历史消息变短（压缩成功）


- 可能额外注入一条 post-compaction 提示上下文


- 但 system 段仍按模板+动态注入重建，长度不一定变小（甚至可能因配置变化变大）


所以如果你要降 token，大头优化要做在：


1. system 内容本身（特别是 injected files / tooling 冗余）


2. body.tools[] 描述与 schema 体积


3. skills / memory 注入策略（限制/裁剪）


## Q2: spawn 出来的subagent 系统提示词都带什么？


1.第一段硬编码注入的提示词（减去：skill相关，增加： spawn subagent相关提示词）


2.Project Context 里注入了 AGENTS.md / TOOLS.md 的全文


3.body.tools[] 里注入了工具列表（23个）


subagent 不能“自动用技能”（不会看到 ## Skills / <available_skills> 那段索引）。


但不是绝对不能：


1. 你可以在任务里显式给出 skill 名或 SKILL.md 路径，让它用 read 去读并执行。


2. 或者把关键 skill 规则放进它能看到的上下文（例如 extraSystemPrompt / 注入文件）。


少掉的是这 8 个tools：


1. agents_list


2. sessions_list


3. sessions_history


4. sessions_send


5. sessions_spawn


6. session_status


7. memory_search


8. memory_get


原因不是随机，是 subagent 场景下的工具策略/提示模式收缩：会去掉会话编排和记忆检索这类工具


Tip：


如何debug subagent提示词：


后记


这篇内容前前后后也肝了两天，modelbox 很早就写好了，之前是为了调试，现在开源出来，方便大家想什么时候看提示词，就临时启动下，然后/models 切换一下即可


如果你想看更多提示词字段解读，欢迎点击岚叔该文章查看：https://mp.weixin.qq.com/s/_LfqQwdTHaoNiVeB_iVGCQ


上一篇OpenClaw文章见：


同样是上下文优化的，希望这两篇文章对您有所帮助💗～

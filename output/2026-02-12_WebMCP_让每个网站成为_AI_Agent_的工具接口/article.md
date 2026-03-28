# WebMCP：让每个网站成为 AI Agent 的工具接口


WebMCP：让每个网站成为 AI Agent 的工具接口


WebMCP 是一项由 Google 和 Microsoft 联合推动的 W3C Web 标准提案，于 2026 年 2 月 10 日在 Chrome 146 中发布早期预览版。 它提出了一个全新的浏览器原生 JavaScript API（navigator.modelContext），允许网站开发者将 Web 应用的功能以结构化"工具"的形式暴露给 AI Agent，取代了当前 Agent 依赖截图分析或 DOM 解析来操作网页的低效方式。WebMCP 并非 Anthropic 的 MCP 协议，不使用 JSON-RPC 规范，而是一个完全运行在浏览器客户端的 Web 原生标准——网页本身就是"服务器"。这意味着，未来的网站不仅要为人类用户设计界面，还需要为 AI Agent 提供结构化的能力接口，一场关于"Agent SEO"的新范式正在形成。


## 从 Amazon 内部的 Auth 难题到 W3C 标准提案


WebMCP 的诞生源于一个真实的工程痛点。2025 年初，Amazon 后端工程师 Alex Nahas 在公司内部面对一个棘手问题：Amazon 拥有数千个内部服务，它们被打包成一个庞大的 MCP 服务器，塞满了上下文窗口——"你不得不在连接字符串中用命令禁用某些工具"。更致命的是，MCP 规范采用了 OAuth 2.1 认证，但 Amazon 内部几乎没有服务实现了这个协议，每个服务都有自己独立的认证体系。


Alex 注意到，Amazon 所有的授权管理都通过浏览器中的联合登录体验完成。他的核心洞察是：直接在浏览器中运行 MCP，复用浏览器已有的 SSO、Session Cookie 和身份认证机制。他将 MCP TypeScript SDK 集成到客户端 JavaScript 中，用 postMessage 构建了自定义传输层与 Chrome 扩展通信。这就是 MCP-B（Model Context Protocol for the Browser）的原型。


与此同时，Google Chrome 团队正在内部原型化"Script Tools"概念，Microsoft Edge 团队也在探索类似方向。当 MCP-B 出现后，三方通过 W3C Web Machine Learning 社区组合流，将这一概念命名为 WebMCP。2025 年 8 月 13 日，联合提案在 GitHub 上正式发布；同年 9 月 25 日，WebMCP API 被正式接纳为 W3C 社区组的交付物。


标准的三位编辑分别来自两大浏览器厂商：Brandon Walderman（Microsoft）、Khushal Sagar（Google）和 Dominic Farolino（Google）。值得注意的是，目前没有发现 Apple/Safari 或 Mozilla/Firefox 参与的证据——这仍是一个以 Chromium 生态为主导的标准化进程。


## 双轨 API 设计：HTML 声明式 + JavaScript 命令式


WebMCP 提出了两条互补的 API 路径，覆盖从简单表单到复杂交互的全部场景。


声明式 API 通过 HTML 表单属性直接定义工具，无需编写任何 JavaScript。开发者只需在现有的 <form> 元素上添加 toolname、tooldescription 等属性，浏览器即可自动从表单输入字段的名称、类型和验证规则生成工具的参数 Schema。例如，一个待办事项表单只需添加三行属性就能成为 Agent 可调用的工具。这种方式降低了准入门槛，让内容作者（不仅限于开发者）也能参与，且表单工具可被搜索引擎索引和爬取。


命令式 API 通过 navigator.modelContext.registerTool() 方法注册复杂的动态工具。开发者提供工具名称、自然语言描述、JSON Schema 格式的参数定义和执行回调函数。例如：


WebMCP 还引入了几个配套 Web 平台特性：SubmitEvent.agentInvoked 属性让服务端能区分 Agent 提交与人类提交；CSS 伪类 :tool-form-active 和 :tool-submit-active 允许页面在 Agent 操作时呈现不同的视觉状态；Google 还发布了 Model Context Tool Inspector Chrome 扩展用于调试。


## 与 Anthropic MCP 的本质区别："同名不同源"


尽管名称中包含"MCP"，WebMCP 与 Anthropic 的 Model Context Protocol 在架构上是根本不同的技术。Alex Nahas 最初试图将完整的 MCP 协议移植到浏览器中，但 W3C 工作组明确拒绝了与 MCP 规范的紧耦合。2025 年 9 月 18 日的 W3C 会议达成决议：WebMCP 采用"SDK 选项"，即在浏览器与 MCP 客户端之间提供抽象层，而非直接实现 MCP 协议。


维度Anthropic MCPWebMCP协议基础JSON-RPC 2.0非 JSON-RPC，Web 原生 API架构模式Client-Server（需后端服务器）纯客户端（网页即"服务器"）传输方式stdio / Streamable HTTP / SSEpostMessage / 浏览器运行时消息认证机制OAuth 2.1浏览器原有认证（Cookie、Session）运行环境Python / Node.js 后端浏览器中的 JavaScript人类参与可选核心设计原则能力范围Tools + Resources + Prompts当前仅 Tools可用性服务器常驻运行用户导航到页面时才可用


两者的关系更像互补而非竞争：MCP 适用于后端服务集成和无头自动化场景，WebMCP 则专为浏览器内的人机协作工作流设计。一个成熟的应用很可能同时部署两者——MCP 处理后端操作，WebMCP 处理前端浏览器交互。


## 对比 Browser Use 和 Computer Use：从"盲人摸象"到"结构化对话"


在 WebMCP 出现之前（准确地说是 2026 年 2 月 10 日之前），AI Agent 与网站交互只有两条路径。视觉方式（Anthropic Computer Use、OpenAI Operator）通过截屏分析网页，每张截图消耗约 2,000 token；语义方式（Browser Use、Playwright MCP）通过解析 DOM/无障碍树来定位元素。两种方式都需要额外的推理轮次、多模态模型支持，且本质上是在"猜测"UI 结构。


WebMCP 提供了第三条路径：网站主动声明能力，Agent 通过确定性的函数调用完成操作。工具响应通常只有 20-100 token，相比截图方式可节省高达 89% 的 token 消耗。更关键的是，这是确定性调用而非概率性视觉解析——不再有 Agent"像教长辈用电脑一样笨手笨脚地操作页面"的尴尬。


但 WebMCP 有一个根本限制：它需要网站主动适配。Computer Use 和 Browser Use 无需网站配合即可工作，这意味着在 WebMCP 被广泛采用之前，视觉/语义方式仍将是 Agent 操作任意网页的必要手段。WebMCP 的真正价值在于为高频、关键的 Web 应用提供一条可靠、高效、安全的 Agent 交互通道。


## 生态全景：三个 WebMCP 和一个标准


当前"WebMCP"这个名字实际指代了几个相关但不同的项目，需要仔细区分：


W3C WebMCP 标准（webmachinelearning.github.io/webmcp）是 Google 和 Microsoft 联合推动的正式 Web 标准提案，定义了 navigator.modelContext API。目前处于社区组草案阶段，不是 W3C 正式标准，也不在标准轨道上。规范文本本身仍非常骨架化——ModelContextContainer 接口尚无方法定义，详细 API 存在于 proposal.md 和 Chrome 实现中。


MCP-B（github.com/MiguelsPizza/WebMCP，947 Stars，64 Forks）是 Alex Nahas 创建的参考实现和 Polyfill，充当 WebMCP 在当前浏览器中的桥梁。它通过 npm 包 @mcp-b/global 实现 navigator.modelContext 接口，并通过 @mcp-b/transports 提供 Tab 传输（postMessage）、Extension 传输（Chrome 运行时消息）和 Iframe 传输。MCP-B 还提供了原生服务器桥接（@mcp-b/native-server），在端口 12306 上运行，连接浏览器扩展与 Claude Desktop、Cursor 等本地 MCP 客户端。值得注意的是，MCP-B 扩展本身已不再开源，代码库仅供历史参考，开源内容已迁移到 WebMCP-org GitHub 组织。


webmcp.dev（github.com/jasonjmcghee/WebMCP，315 Stars）是 Jason McGhee（Cursor 联合创始人/工程师、DataRobot 前首席 ML 工程师）于 2025 年 3 月发布的独立开源库。它采用 WebSocket 桥接方式连接 MCP 客户端与浏览器标签页，通过 npm 包 @jason.today/webmcp 发布，累计下载约 44,200 次。McGhee 本人已建议开发者关注 W3C 标准化进程。


Chrome Web Store 上还有一个名为"Web MCP: 浏览器MCP服务，AI自动化操作"的扩展，提供一键启动浏览器 MCP 服务的能力，但这是第三方独立项目，与上述几者均不相同。


## 安全模型：机遇与隐忧并存


WebMCP 的安全设计遵循 Web 平台的既有信任模型，但也引入了新的攻击面。工具继承页面的同源策略和内容安全策略（CSP），API 仅在安全上下文（HTTPS）中可用，且仅暴露在顶级浏览上下文中。W3C 工作组明确决议：不允许外部 Agent 通过 JavaScript 注入方式与 WebMCP 交互。


Alex Nahas 提出了 "致命三元组" 问题：如果用户同时打开了银行标签页和恶意标签页，拥有两者上下文的浏览器 Agent 可能被操纵泄露敏感数据。WebMCP 通过域名级别的工具隔离、工具哈希验证、用户确认流程（Elicitation）和域信任 TTL 机制来缩小攻击面，但并未完全消除风险。


在 Chrome 的 blink-dev 邮件列表上（2026 年 2 月 9 日），W3C 成员 Tom Jones 直言："基于 explainer 文档来看，没有进行过安全审查…… 我认为这对任何启用此功能的浏览器用户来说都将是隐私噩梦。"Google 方面回应称，社区组每两周举行一次安全/隐私讨论会，Chrome Security 团队已参与其中，且当前仍是"面向开发者测试的早期原型，不是发布意向"。


## 中文技术社区的反响与展望


中文技术社区对 WebMCP 反应迅速且热烈。36Kr 以"终于，AI 不用再假装是人了"为题进行了深度报道。53AI 发表分析文章称"WebMCP：Google 刚对 Chrome 动了手术，AI Agent 的玩法全过时了"，预测 Web 架构将分裂为两层：面向人类的视觉层和面向 Agent 的结构化层。搜狐新闻指出 WebMCP 结构化工具调用可节省高达 89% 的 token 消耗。多个中文技术社区将 WebMCP 类比为"Agent 时代的 SEO"——正如网站曾发现搜索引擎也是"用户"，现在它们需要意识到 AI Agent 同样是"用户"。


在安全层面，中文安全社区同样高度关注。安全内参发布了"MCP 协议 7 大安全风险"和"10 大已验证安全风险"分析；慢雾科技在 GitHub 上发布了 MCP 安全检查清单；火山引擎（字节跳动云）发表了 MCP 安全架构分析。


## 结论：Web 开发正在获得第二个"用户群"


WebMCP 标志着 Web 开发范式的一次重要转变。从技术本质上看，它将"网站如何与 AI Agent 交互"从一个需要视觉理解和 DOM 猜测的开放问题，转化为一个由开发者定义、浏览器中介、用户监督的结构化协议。这不是对 Anthropic MCP 的替代，而是在浏览器这个特殊运行环境中的互补方案——MCP 解决后端，WebMCP 解决前端。


当前最值得关注的三个信号：其一，Chrome 146 的早期预览意味着 Google 已将实现推进到可测试阶段，Alex Nahas 预计 2026 年中后期将有"官方浏览器公告"；其二，声明式 API 的设计（HTML 表单属性即可定义工具）将极大降低采用门槛，可能催生类似 Schema.org 标记的大规模普及；其三，Apple 和 Mozilla 的缺席仍是最大不确定性——没有 Safari 和 Firefox 的参与，WebMCP 可能沦为 Chromium 独有特性，而非真正的 Web 标准。


对开发者而言，现在是开始了解和实验 WebMCP 的合适时机——通过 MCP-B Polyfill 或 Chrome 146 Canary 的 flag 均可体验。但在将其用于生产环境之前，安全模型的成熟和跨浏览器支持的明确仍是需要观望的关键前提。

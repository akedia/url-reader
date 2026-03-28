# How to set up Claude Cowork the right way(so it actually does your work while you step away)


The people who are "getting" AI in 2026 aren’t the ones writing the cleverest prompts.


They’re the ones who figured out Cowork.


I started using Claude Cowork the week it launched in January 2026. Within a month it became the first thing I open every morning — before email, before Notion, before anything else. Not because someone told me to. Because it kept finishing work I used to spend hours doing myself.


I’ve spent the last three years building AI workflows for my work. Thousands of prompts tested. Dozens of tools tried. So when I tell you Cowork changed how I operate, I’m not saying it lightly.


This is the guide I wish someone had handed me before I wasted time figuring it out alone. Every feature. Every setup step. Every first prompt. And the honest version of where it falls short.


1. Save this guide and spend 30 minutes this weekend to set up Cowork properly.


2. Send it to anyone asking you, “I keep hearing about Claude but I’ve never tried it.”


Cowork is not a chatbot. It’s something else entirely.


Most people think Claude is like ChatGPT. A text box. You type, it responds. That’s claude.ai — the browser version.


Claude Cowork is different. It lives on your desktop. It reads and writes to folders on your actual computer. It creates Word documents. It builds spreadsheets with working formulas. It installs specialist plugins for your exact job. And when it doesn’t have enough information to do something well, it asks you — instead of guessing and giving you polished garbage.


Cowork is what happened when Anthropic took the power of Claude Code — their agentic developer tool — and rebuilt it for the rest of us. No terminal. No command line. No code. Just: describe the outcome you want, point it at your files, and step away.


I describe what I need. Cowork asks me three questions. I answer them. I come back 20 minutes later to a finished document. That loop now covers about 60% of my knowledge work.


Cowork is not one feature. It’s five.

1. File System Access — Claude reads and writes to your actual computer
1. AskUserQuestion — it forces clarity instead of guessing
1. Plugins — specialist packs for your exact role
1. Instructions — permanent memory that loads every session
1. Connectors — live integrations with Slack, Drive, Notion, and 50+ tools

I ranked them by how much they changed how I work. Start at the top.


1. File System Access


What it is (in 10 words): Claude reads and writes files in a folder on your computer.


## Why it matters


Every other AI tool runs on uploads. You export a file. You drag it into the chat. You wait. You get an output. You download it. You put it back wherever it came from.


Cowork eliminates that entire loop. You select a folder on your computer. Claude reads everything inside it. When it creates something — a document, a spreadsheet, a summary — it saves directly to that folder. No manual steps.


This sounds like a small thing. It isn’t. It’s the difference between AI as a tool you go to and AI as a collaborator that works in your environment.


Cowork can read your old reports to match your formatting. It can pull data from last month’s spreadsheet to build this month’s. It can reference your brand guidelines mid-task without you mentioning them. All because you pointed it at the right folder and it


## How to set it up

1. Go to claude.com/download. Download the desktop app (macOS or Windows x64).
1. You need a paid plan. Pro is $20/month. Max starts at $100/month for heavier usage.
1. Open the app. At the top, you’ll see a toggle. Switch to the Cowork tab.
1. Click the folder icon or “Select Folder” and choose a local folder from your computer.
1. Everything in that folder is now readable by Claude for the duration of your session.

## Pro tip: The context files strategy


The mindset shift that matters most: stop thinking about better prompts and start thinking about better files.


Create a dedicated folder called “Claude Context.” Inside it, build three files:

- about-me.md — who you are, what you do, your role, what success looks like in your work
- brand-voice.md — how you communicate. Your phrases. What sounds wrong to you. Examples of writing you’re proud of.
- working-style.md — how you like Claude to behave. Do you want questions first? Short or long outputs? Which file formats?

The more quality context you give Claude in these files, the less prompting you need. Output quality goes from “generic AI” to “this actually sounds like something I’d write.”


These files compound over time. Every week you refine them, Claude gets better at your specific work. It’s the most underrated setup step in this entire guide.


## Your first prompt


Read all the files in this folder completely. Then give me a summary of what you know about me, how I work, and what context you have access to.


2. AskUserQuestion


What it is (in 10 words): Cowork asks YOU questions instead of guessing and getting it wrong


## Why it matters


Here’s what every other AI does when you give it an unclear task: it guesses. Confidently. It picks an interpretation, runs with it, and gives you a polished output that answers the wrong question.


You asked for a client proposal. It gives you a generic one. You asked for a summary. It summarizes the wrong things. You asked for a report. It writes it in the wrong tone.


Cowork does something different. When it needs more information, it stops and generates a form. Multiple-choice questions. Specific options. A structured prompt that helps you think through what you actually want.


I use this as the starting point for every non-trivial task. I don’t try to write perfect prompts anymore. I let Cowork figure out what it needs to know. And if the first round of questions doesn’t get us aligned, I say so. It generates a new set and we iterate.


With a context window of over one million tokens, I’ve also stopped worrying about hallucinations on complex projects. When Claude has read all the relevant files and clarified the task through questions, the output is consistently grounded in what’s actually true.


## How to use it


Add this line to the end of any prompt:


DO NOT start working yet. First, ask me clarifying questions so we can define the approach together. Only begin once we’ve aligned


Or use this as your default opener for almost any task:


## Your first prompt


I want to [YOUR TASK] so that [WHAT GOOD LOOKS LIKE].  First, read all uploaded files completely before responding.  DO NOT start executing yet. Ask me clarifying questions (use AskUserQuestion) to refine the approach. Only begin work once we’ve aligned.


Try it once. You’ll never go back to writing long, carefully engineered prompts from scratch.


The mindset shift: ChatGPT trained you to write better prompts. Cowork trains you to give better context. One is a skill that deprecates. The other compounds.


3. Plugins


What they are (in 10 words): Pre-built specialist packs that make Claude an expert instantly.


## Why they matter


Without a plugin, Claude Cowork is a brilliant generalist. It can write, research, analyze, organize, and build. But it doesn’t know your industry’s terminology, your team’s workflow, or the specific outputs your role requires.


Plugins change that. They’re bundles of skills, slash commands, and sub-agents designed for specific job functions. Anthropic shipped 11 official plugins in January 2026:

- Productivity — task management, calendars, and daily workflows
- Marketing — content drafting, campaign planning, brand voice
- Sales — account research, call prep, outreach, battlecards
- Finance — financial modeling, analysis, reporting
- Data Analysis — SQL, dashboards, dataset exploration
- Legal — contract review, research, drafting
- Product Management — specs, roadmaps, user stories
- Customer Support — ticket handling, response drafting
- Enterprise Search — search across your connected tools
- Biology Research — scientific literature and data
- And more being added

The impact hit fast. When the Legal plugin launched, Thomson Reuters dropped 16% in a single trading session — its worst day on record. LegalZoom fell 20%. That’s what it looks like when AI starts genuinely doing specialized work.


Install the Sales plugin and Claude can research accounts, prep you for calls, and draft outreach sequences. Install the Data plugin and it explores your dataset, writes SQL, builds dashboards, and flags anomalies. You don’t need to be technical. You just click install


## How to install plugins

1. Open Claude Cowork.
1. Click the “+” button in the chat bar, then click “Plugins” to browse the library.
1. Or go to claude.com/plugins to see everything available.
1. Pick the plugin that fits your role and click Install.
1. Type “/” in any Cowork chat to see the slash commands that plugin adds.

## Your first prompts (after installing)


After installing the Productivity plugin:


/productivity:start Let’s review what I need to get done today and set up my task list.


After installing the Marketing plugin:


/marketing:draft-content Write a LinkedIn post about [topic]. Match the voice from my brand-voice.md file. Target [audience]. Goal: [what I want people to do].


After installing the Data plugin:


/data:explore I’ve uploaded a CSV in this folder. Give me a summary of what’s in it, flag any anomalies, and suggest three analyses worth running.


The output with a plugin active is noticeably more structured and opinionated than a generic prompt. It knows what a good output looks like for your function.


4. Instructions (Global & Folder)


What they are (in 10 words): Permanent memory that loads automatically at the start of every session.


## Why they matter


Cowork has no memory between sessions. Every time you open a new conversation, Claude starts completely fresh. No knowledge of who you are. No memory of what you discussed yesterday. Nothing.


This is the feature that frustrates people most — until they discover Instructions.


Instructions are standing orders you write once. They load automatically at the start of every Cowork session. Global instructions apply everywhere. Folder instructions apply when you select a specific local folder.


With Instructions set properly, Claude starts every session already knowing your name, your role, your communication preferences, your output defaults, and your working style. You never re-explain yourself again.


## How to set up Global Instructions

1. Go to Settings > Cowork in the Claude desktop app.
1. Click “Edit” next to Global Instructions.
1. Write what you want Claude to always know. Save.

What to put in global instructions:

- Your name, role, and what you do (“I’m a freelance brand strategist working with DTC founders”)
- Your communication preferences (“I prefer concise, direct outputs — no padding, no filler”)
- Your output defaults (“Always save documents as .docx unless I say otherwise”)
- Your working style (“Always ask clarifying questions before starting any task”)
- Things to avoid (“Never use bullet points unless I specifically request them”)

Folder instructions work the same way but are project-specific. When you select a folder, Claude checks for instructions tied to it. This is perfect for client work: each client folder can have its own brief that Claude loads automatically. Every session with that client starts with full context, every time


## Your first prompt


After setting global instructions, open a new session and ask:


Before we start any work, tell me what you know about me, how I like to work, and any standing preferences you’re aware of.


If the instructions loaded correctly, Claude will reflect them back to you clearly. If something’s missing or off, fix it now before you do real work.


5. Connectors


What they are (in 10 words): Live integrations with Slack, Drive, Notion, and 50+ other tools.


## Why they matter


The typical AI workflow involves a lot of copy-pasting. You screenshot your Slack thread. You copy the doc. You paste it into the chat. You add context manually. It’s exhausting.


Connectors eliminate all of that. Link your tools once, and Claude can reference live data from them mid-conversation. No copy-pasting. No screenshots. No downloads.


Ask Cowork to “summarize the key decisions from #project-alpha over the last two weeks” and it reads your Slack. Ask it to “pull the Q1 numbers from the revenue doc in Drive” and it opens your Google Doc. Ask it to “find everything tagged as a blocker in Notion” and it searches your workspace.


This is free on all plans. It’s the most underused feature in Cowork, in my experience.


## How to connect your tools

1. Go to Settings > Connectors in Claude Desktop.
1. Browse the directory (50+ integrations including Slack, Google Drive, Notion, Figma, Asana, and more).
1. Click a connector and hit “Add.”
1. Authenticate with that tool. Done.

You only do this once. After that, Claude can access live data from that tool in every Cowork session.


## Your first prompt (after connecting Slack)


Search my Slack messages from the last 7 days and give me a summary of anything I need to follow up on. Organize by urgency.


## Or after connecting Google Drive:


Find the most recent document about [project name] in my Drive. Read it and tell me the three most important things I need to know.


Where Cowork falls short (I promised honesty)


Cowork is the best AI tool I’ve used for knowledge work. It is not perfect. Here’s what I’ve personally hit:


## No cross-session memory.


Every new Cowork session starts completely fresh. This is the biggest friction point. The workaround works well — keep your context in markdown files and set solid global instructions. But you will feel this gap, especially on long-running projects. Document important decisions in files Claude can read.


## Tasks stop if you close the app.


Cowork runs as an active session inside Claude Desktop. If you quit the app, the task stops mid-execution. Put your computer to sleep instead — the session survives that. Don’t close the window while work is running.


## Usage goes faster than regular chat.


Complex Cowork tasks consume more of your monthly usage allocation than standard chat. Multi-step tasks with file reading, document creation, and parallel subtasks use significantly more compute. If you’re on Pro and doing heavy daily use, monitor Settings > Usage. If you’re hitting limits constantly, Max ($100-$200/month) may be worth it.


## Desktop only. No mobile. No sync across devices.


Cowork exists in the desktop app and nowhere else. No iPhone. No browser version. No syncing between your laptop and desktop. If your work is split across devices, build your context files in a cloud-synced folder (like iCloud or Dropbox) so at least your files are consistent.


## It doesn’t generate images.


For photos, illustrations, or visual art, Cowork isn’t your tool. I use Gemini Imagen for images and keep Cowork for documents, spreadsheets, presentations, and research. Different tools for different jobs.


## It’s a research preview.


Anthropic is explicit about this: agent safety for Cowork is still under development. It’s remarkably solid for a preview, but treat it accordingly. Don’t run it on files you can’t afford to have modified without confirmation. Enable deletion protection in settings and review plans before letting it execute on anything sensitive


Your first 30 minutes with Cowork.


Open your calendar. Block 30 minutes. Here’s exactly what to do with them.


## Minutes 0–5: Install


Go to claude.com/download. Download the desktop app. Sign in or create an account. Get Pro ($20/month). Open the app. Find the Cowork tab at the top. You’re in.


## Minutes 5–10: Create your context files


Open any text editor. Create three new files and save them in a folder called “Claude Context.”

- about-me.md: Who you are. What you do. One example of work you’re proud of.
- brand-voice.md: How you communicate. Phrases you use. What sounds wrong. Tone.
- working-style.md: How you want Claude to behave. Questions first? Short or long outputs? Preferred formats?

Save as .md files (Markdown). They’re the most efficient format for Claude to read.


Pro tip: If you prefer talking to typing, use a voice-to-text tool to dictate these files instead. Getting context into text is what matters — how you get it there is up to you.


## Minutes 10–15: Set your global instructions


Go to Settings > Cowork in the desktop app. Click “Edit” next to Global Instructions. Paste in the key highlights from your three files: who you are, how you communicate, and how you want Claude to work with you. Save.


This is the one-time investment that pays back every session forever.


## Minutes 15–20: Run your first Cowork task


Select your “Claude Context” folder. Start a new Cowork session. Type:


Read all the files in this folder. Then help me [your actual task].  Before you start — ask me clarifying questions so we can make sure you’re headed in the right direction.


Watch what happens. Respond to the questions. Iterate. Have a conversation. The best tasks to start with are things you already know how to do well — because you can tell immediately whether the output is right.


## Minutes 20–25: Install a plugin


Click the “+” button in the chat bar. Click Plugins. Browse the library. Pick one that fits your role:

- Productivity — good starting plugin for anyone managing tasks and workflows
- Marketing — if you create any content or run campaigns
- Sales — if you do any prospecting, outreach, or account management

Install it. Type “/” in a new Cowork chat to see the slash commands. Try one. See what the output looks like with a specialist plugin active versus a generic prompt.


## Minutes 25–30: Connect one tool


Go to Settings > Connectors. Connect the one tool you use most — Slack, Google Drive, or Notion. Authenticate it.


Then ask Claude something about that tool. Watch it pull live data instead of asking you to copy-paste anything.


That’s the moment it clicks.


The real reason to switch.


I don’t care about Anthropic, OpenAI, Google, or any other company. I’m not picking sides. I’m not paid to recommend anything.


I care about one thing: what actually makes knowledge work faster and better in 2026. And right now, for the kind of work most people do — writing, analyzing, building,organizing, communicating — nothing I’ve found comes close to a well-set-up Cowork workflow.


The people I see getting the most from AI aren’t the ones with the cleverest prompts. They’re the ones who built systems. Files that store their context. Instructions that persist across sessions. Plugins that specialize their tool. A setup that gets better every week.


Cowork is what makes that system possible for knowledge workers. And it’s worth the 30 minutes to set it up.


ChatGPT trained you to write better prompts. Cowork trains you to build better context. One is a skill that depreciates. The other compounds.


If this guide helped you, send it to the person in your network who still asks “should I switch to Claude?”


They should. And now they’ll know exactly how.

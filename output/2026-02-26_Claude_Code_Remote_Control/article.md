Title: Claude Code Remote Control

URL Source: https://simonwillison.net/2026/Feb/25/claude-code-remote-control/

Published Time: Wed, 25 Feb 2026 20:20:44 GMT

Markdown Content:
Claude Code Remote Control
===============

[Simon Willison’s Weblog](https://simonwillison.net/)
=====================================================

[Subscribe](https://simonwillison.net/about/#subscribe)

**Sponsored by:** Teleport — Secure, Govern, and Operate AI at Engineering Scale. [Learn more](https://fandf.co/4u0HQAD)

25th February 2026 - Link Blog

**[Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)** ([via](https://twitter.com/claudeai/status/2026418433911603668 "@claudeai")) New Claude Code feature dropped yesterday: you can now run a "remote control" session on your computer and then use the Claude Code for web interfaces (on web, iOS and native desktop app) to send prompts to that session.

It's a little bit janky right now. Initially when I tried it I got the error "Remote Control is not enabled for your account. Contact your administrator." (but I _am_ my administrator?) - then I logged out and back into the Claude Code terminal app and it started working:

```
claude remote-control
```

You can only run one session on your machine at a time. If you upgrade the Claude iOS app it then shows up as "Remote Control Session (Mac)" in the Code tab.

It appears not to support the `--dangerously-skip-permissions` flag (I passed that to `claude remote-control` and it didn't reject the option, but it also appeared to have no effect) - which means you have to approve every new action it takes.

I also managed to get it to a state where every prompt I tried was met by an API 500 error.

![Image 1: Screenshot of a "Remote Control session" (Mac:dev:817b) chat interface. User message: "Play vampire by Olivia Rodrigo in music app". Response shows an API Error: 500 {"type":"error","error":{"type":"api_error","message":"Internal server error"},"request_id":"req_011CYVBLH9yt2ze2qehrX8nk"} with a "Try again" button. Below, the assistant responds: "I'll play "Vampire" by Olivia Rodrigo in the Music app using AppleScript." A Bash command panel is open showing an osascript command: osascript -e 'tell application "Music" activate set searchResults to search playlist "Library" for "vampire Olivia Rodrigo" if (count of searchResults) > 0 then play item 1 of searchResults else return "Song not found in library" end if end tell'](images/img_001.jpg)

Restarting the program on the machine also causes existing sessions to start returning mysterious API errors rather than neatly explaining that the session has terminated.

I expect they'll iron out all of these issues relatively quickly. It's interesting to then contrast this to solutions like OpenClaw, where one of the big selling points is the ability to control your personal device from your phone.

Claude Code still doesn't have a documented mechanism for running things on a schedule, which is the other killer feature of the Claw category of software.

**Update**: I spoke too soon: also today Anthropic announced [Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork), Claude Code's [general agent sibling](https://simonwillison.net/2026/Jan/12/claude-cowork/). These do include an important limitation:

> Scheduled tasks only run while your computer is awake and the Claude Desktop app is open. If your computer is asleep or the app is closed when a task is scheduled to run, Cowork will skip the task, then run it automatically once your computer wakes up or you open the desktop app again.

I really hope they're working on a Cowork Cloud product.

Posted [25th February 2026](https://simonwillison.net/2026/Feb/25/) at 5:33 pm

Recent articles
---------------

*   [I vibe coded my dream macOS presentation app](https://simonwillison.net/2026/Feb/25/present/) - 25th February 2026
*   [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) - 23rd February 2026
*   [Adding TILs, releases, museums, tools and research to my blog](https://simonwillison.net/2026/Feb/20/beats/) - 20th February 2026

This is a **link post** by Simon Willison, posted on [25th February 2026](https://simonwillison.net/2026/Feb/25/).

[ai 1875](https://simonwillison.net/tags/ai/)[generative-ai 1662](https://simonwillison.net/tags/generative-ai/)[applescript 8](https://simonwillison.net/tags/applescript/)[llms 1627](https://simonwillison.net/tags/llms/)[anthropic 238](https://simonwillison.net/tags/anthropic/)[claude 232](https://simonwillison.net/tags/claude/)[coding-agents 162](https://simonwillison.net/tags/coding-agents/)[claude-code 96](https://simonwillison.net/tags/claude-code/)[openclaw 9](https://simonwillison.net/tags/openclaw/)
### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[Sponsor & subscribe](https://github.com/sponsors/simonw/)

*   [Disclosures](https://simonwillison.net/about/#disclosures)
*   [Colophon](https://simonwillison.net/about/#about-site)
*   ©
*   [2002](https://simonwillison.net/2002/)
*   [2003](https://simonwillison.net/2003/)
*   [2004](https://simonwillison.net/2004/)
*   [2005](https://simonwillison.net/2005/)
*   [2006](https://simonwillison.net/2006/)
*   [2007](https://simonwillison.net/2007/)
*   [2008](https://simonwillison.net/2008/)
*   [2009](https://simonwillison.net/2009/)
*   [2010](https://simonwillison.net/2010/)
*   [2011](https://simonwillison.net/2011/)
*   [2012](https://simonwillison.net/2012/)
*   [2013](https://simonwillison.net/2013/)
*   [2014](https://simonwillison.net/2014/)
*   [2015](https://simonwillison.net/2015/)
*   [2016](https://simonwillison.net/2016/)
*   [2017](https://simonwillison.net/2017/)
*   [2018](https://simonwillison.net/2018/)
*   [2019](https://simonwillison.net/2019/)
*   [2020](https://simonwillison.net/2020/)
*   [2021](https://simonwillison.net/2021/)
*   [2022](https://simonwillison.net/2022/)
*   [2023](https://simonwillison.net/2023/)
*   [2024](https://simonwillison.net/2024/)
*   [2025](https://simonwillison.net/2025/)
*   [2026](https://simonwillison.net/2026/)

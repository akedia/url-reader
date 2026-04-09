# The Death of Issue Tracking


I noticed a pattern among engineering teams building products I love. It seemed a little wacky, but I kept noticing it: no Linear, no backlog, no issue tracking at all.


I would ask customers if they wanted their Detail bugs routed to Linear or GitHub Issues. A common answer was “Slack” but the answer behind the answer would be something like “we run EPD on a two-page google doc, there is no backlog.” No backlog? Where do you keep track of your issues?


At first it seemed like founderbrain run amok, a rebellion of oppositional defiant engineers who refused to be domesticated by the tyranny of the sprint plan, who would surely grow out of it as their companies matured. But I think it’s actually a disciplined mode of operating that just doesn’t have the right tooling or terminology yet. I’m seeing teams scale this to 30+ engineers, and their products are winning in competitive markets, so it’s important to ask why.


## Post-Backlog Engineering


The thinking behind this new mode of building software is something like:

- If it matters, it will come up again. You don’t need to track issues so that you remember to fix them. If they matter, they will remind you of their existence.
- Why write a ticket when you could just fix it? The cost of fixing an issue is converging to the cost of understanding the issue. It used to take 10x as much effort to fix an issue as it took to write a ticket in a ticket tracking system, so it often made sense to write a ticket to preserve your understanding of a problem and accumulate context over time. If it only takes 1.5x as much effort to just fix the issue, you should write a lot fewer tickets.
- Think more, obey less, especially in fast-evolving domains. A backlog gives you a default next thing to do, but it may be an answer that’s out of date by a month. A blank page forces you to do a real OODA loop – to step back and think about what you should be doing next. Lack of a backlog might mean you make better prioritization choices, because your thinking will have less inertia.

## Why is this happening now?


The obvious tailwind is AI. A team of 7 extremely capable engineers running swarms of agents can deliver a product that previously took 50+ engineers. So you can get a lot farther with a small, high context, project-oriented, flat team than you could three years ago.


The agents are getting better so fast that a lot of small teams are operating as though they’re going to stay small forever. Their products are going to grow in surface area and complexity, but the sophistication of agents is going to grow just as fast. So there’s no sense building patterns for scaled work if the team is never going to scale.


Agents are also driving the convergence of “cost to understand” and “cost to fix” that makes this all make sense. In a lot of cases it’s literally the same amount of effort to type “@Linear could you make a ticket for this, set to p2, assign to me” in slack as it is to type “@codex please fix this, assign the PR to me.”


But this mode of operating has been brewing for a few years now. It’s an outgrowth of how a lot of particularly forward-thinking teams have been trending.

- Tuomas Artman (@artman) wrote two years ago that at Linear: fixing bugs should supersede new feature work, your steady-state should be one with no bugs at all, and you should accept a short period of pain while you burn down your backlog to get there.
- Fix Bugs Now from Quinn Slack at Amp (@sqs) takes this to the next level: start with that approach from day one, and build your org around the ability to operate this way. Amp is extraordinarily polished, a standout gem in the highly competitive world of daily driver coding agents. (And it has plenty of features!)

Taken to its logical conclusion, it’s natural to not keep a backlog at all. Instead, when an issue comes up, it either meets some “worth fixing” bar, in which case do so today, or it doesn't, in which case it’ll come up again if it matters. There’s nothing to accumulate.


## Who this Works For


What do you need if you want to operate this way?

- Small, flat teams. If a team is so large that it takes effort just to get an issue in front of the right set of eyes, then you need some kind of written intermediate work artifact. If you want to live without backlogs then you need every issue to be one slack ping from the right person. (Or better yet, one desk chair roll.)
- High ambient context. You need a relatively stable team if you want people to remember that an issue has come up before or know who to ping about something.
- Engineers you trust to make a lot of independent judgement calls about what’s worth fixing and what isn’t. Operating without tickets means giving up a lot of day-to-day control over what ultimately gets worked on. If you want to operate this way, don’t hire engineers who require day-to-day guidance.
- Engineers you trust to do their own project management. A big project is going to have a lot of moving pieces. Ticket tracking is a great scaffold, a sort of lowest common denominator forcing function to get people to at least keep TODO lists, make sure it’s clear who owns what, make sure different people agree about whether or not something is done, and so forth. If engineers are going to execute complicated projects on 1-2 page living documents, you need to trust that they can manage the complexity of those projects without the guardrails. And if there’s no persistent backlog that lives on after the project, you need to trust that when an engineer wraps up the project and starts working on something new, they’ve made good decisions about what to punt – you won’t even be aware of most of those decisions.
- High quality dev infra. You need an agent-ready dev environment, ideally one that can run in a container in the cloud.

You’ll notice that this is pretty much the spec for what a high-performing team looks like right now. And since those teams are outperforming everyone else by such a wide margin, this is probably where software is headed.


The death of issue tracking is part of a broader death of Midwit Software Engineering. It’s premature to declare the death of the profession, but it’s becoming increasingly untenable to be mediocre at it.


The issue tracking companies themselves might be fine. The good ones will adapt. This new way of working is emerging within the earliest wave of early adopters. It probably doesn't even show up in the numbers yet for workplace productivity SaaS companies. But if you want to know what the future looks like, the answer isn't a kanban board.

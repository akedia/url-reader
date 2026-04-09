# How to Build American Shenzhen, Fast


After a recent debate with @sdamico on whether the U.S. can actually compete with China's manufacturing ecosystem, I was compelled to finally write this list out. This is the stack-ranked list and blueprint I wish existed when I started @atomic_inc and my crusade to reindustrialize America.


I believe reindustrialization is more important than any other aspect of our economy, including AI, for ensuring the long-term durability of the United States. If you manufacture things locally, you ensure your self-reliance. If you ensure your self-reliance, you ensure your stability. And if you ensure your stability, you ensure your freedom. BUILD FACTORIES.


Here is the core claim: there is no physical law preventing the United States from building its own Shenzhen. The density that makes Shenzhen work -- thousands of suppliers within 30 miles and millions of square feet, a prototype fabricated in the morning and assembled by afternoon -- is not a trick. It is an artifact of carefully crafted state industrial policy and subsidies that led to the ultimate infrastructure stack: PCB fabs, injection molders and machine shops, component distributors, test labs, surface treatment shops, and the logistics connecting them, all within a 2-hour radius. That stack can be built here. The question is how fast.


Bootstrapping works. @sendcutsend crossed $100M in revenue with ~400 employees by digitizing sheet metal, no venture capital required. But if speed is the key variable -- and I believe it is -- then venture can play a massive role in what is a generational opportunity to save the world, return funds, and not be hated by normies. For once, the incentives are perfectly aligned: national security, economic growth, job creation, and venture returns all point in the same direction. This is not defense grift. This is not a rollup plan. This is building real things that real people need, at a speed that matters with technology that can be built today.


@oyhsu's factory economics primer (a16z, 2026) provides the venture-backable scaffold. It shows that manufacturing companies with proprietary process IP, steep learning curves, and software-driven yield improvement are not traditional industrials. They are a new asset class: tech-enabled manufacturers that compound value through Wright's Law, defend margins through capital intensity, recycle capital faster through digitization, and never go to zero because real assets provide a liquidation floor. The market is beginning to recognize this -- median industrial acquisition multiples jumped to 14.7x EV/EBITDA in 2025, up from 8x. But the repricing has barely started.


We're doing four things here:

1. Explain why now. Every macro tailwind is aligned, and technology is finally advanced enough to rebuild manufacturing end to end. Never a better time to go vertical.
1. Make the dual-use case. Pure defense is a strategic blunder for most. Even the Pentagon wants commercial-first companies. The optimal revenue mix is 75/25 commercial/defense.
1. Stack-rank 12 manufacturing categories on ecosystem criticality, venture return potential, and dual-use fit, then maps them into a concrete "2-hour supply chain" blueprint -- including the common manufacturing protocol that ties it all together.
1. Show the market is catching on. Tech-enabled manufacturing is being repriced as a distinct asset class. The data on multiples, exit rates, and capital flows all point the same direction.

## Part I: The Speed Thesis -- Why Now


Every Tailwind Is Blowing


This is not a speculative thesis. Every macro tailwind is aligned, and they are not going away.


Deglobalization is accelerating. China's increasing agitation on the world stage -- from Taiwan Strait escalation to export controls on batteries, rare earths, and critical minerals -- is forcing supply chain decoupling that no trade deal can reverse. Domestically, reindustrialization has been canonized in the National Security Strategy. This is not one administration's pet project. Every recent administration has made material attempts at industrial policy -- CHIPS Act, IRA, tariff regimes, export controls, defense acquisition reform. The bipartisan consensus is real. People believe in this, want it, and are voting for it. Policy is moving into place. The only question is whether the private sector can move fast enough to absorb the opportunity.


The 5-to-10-year micro cycle and 20-to-30-year macro cycle of this transition are underway simultaneously. The breakout signal is unmistakable: a new generation of companies tackling fundamental, unsexy manufacturing -- machining, welding, sheet metal forming, castings, assembly, tool and die, riveting, forging, stamping -- with software, automation, and the sensibility of technologists and tradespeople combined. Simultaneous advances in compute, robotics, ML, materials science, and simulation are converging to make this possible for the first time.


The Real Problem Is Not Labor Cost


There is a basic observation about where cost actually lives in American low-volume manufacturing that most people get wrong.


The U.S. does plenty of manufacturing. It is the second-largest manufacturing nation. But its nearly $3 trillion manufacturing sector is overwhelmingly tilted toward high-volume, static, long-lifecycle products: cement, steel, chemicals, cars, dishwashers. The U.S. performs poorly at high-mix, low-volume (HMLV) work: short-lead-time, custom, frequently changing parts made in quantities of 1 to 10,000. That is the gap. And it is the gap that matters -- not because HMLV is the end state, but because it is the bridge. HMLV is what hardware startups need, what defense programs need, what maintenance and repair operations need, and what any fast-iterating product company needs. It is also the hardest manufacturing problem to solve with technology, because every job is different. The factory architecture you build to win at HMLV -- software-defined scheduling, automated changeover, real-time material flow, process knowledge captured in code instead of in someone's head -- is the same architecture that scales into ultra-flexible mass production. You are not building a better job shop. You are building the machine that can do any mix at any volume. HMLV is the beachhead. Flexible, scalable, domestic mass production is the endgame, a replicator if you will.


Here is the hard truth about the existing U.S. manufacturing base: most of the hollowed-out trades that still survive are living on margins. They do one type of work, for a handful of repeat customers, and that is how they stay alive. They don't have money to upgrade capex or adopt fancy tech, they struggle with capital formation. They do not care about your startup project and your low-volume order, because they cannot afford to. Build a process, lock it in, and operate it. They do not have the capability to run your work alongside their real work, and the quoting and setup overhead for a one-off job eats whatever margin they might have earned. The skilled trades have a replacement rate of 0.4 -- for every five machinists, welders, and toolmakers who retire, only two enter the field. Over 400k manufacturing jobs sit open today, and that number is projected to reach 2.1 million by 2030. The existing shops are not going to absorb the coming demand or be alive by then. They are aging out of existence.


And to be frank: labor cost is not the variable most people think it is. Cheap labor allowed production to move offshore -- it was the enabler, not the cause. Cheap labor also helps you compound tribal knowledge infinitely faster, because you can afford to staff more shifts, run more experiments, and keep more people on the floor learning. But in a decoupling world, the absolute cost of labor matters far less than whether you are capturing and rebuilding manufacturing knowledge domestically. When you pull labor costs across the U.S., China, India, and Mexico and set them alongside energy costs and raw material costs, the gap is not as wide as the narrative suggests. American energy is cheap. American raw materials are accessible. The real cost disadvantage is in the factory itself -- the engineering, scheduling, the changeover, the material flow, the information gaps between design and production, and the broken supply chain that wraps around all of it. That is what technology eliminates.


The root cause of the HMLV gap is not labor cost at the machine. It is the production process itself. The average job shop runs equipment at 25-30% utilization -- not because the machines are broken or the workers are lazy, but because high-mix production means machines spend more time being set up, changed over, and waiting for materials than they do actually cutting parts. On top of that, the quoting takes weeks, the scheduling lives in someone's head, the supply chain is held together with email and phone calls, and vendor qualification takes months of paperwork and audits before a single part is ever ordered. For a small-quantity machined part, the actual cutting time might be minutes, but the calendar time from order to delivery is weeks or months. The steel in a low-volume steel part might be 2-3% of the total cost. The rest is friction across the entire process -- on the floor and off it. The shop is not capacity-constrained. It is process-constrained.


What Technology Actually Does to a Factory


The tech-enabled manufacturing thesis is about collapsing the entire gap between design intent and finished goods. Automatic toolpath generation that eliminates manual CAM programming. Intelligent scheduling that sequences jobs to minimize changeover and maximize machine uptime. Automated work instructions. Real-time material tracking that ensures the right stock is at the right machine before the previous job finishes. Instant quoting that converts a 3D file into a price and lead time in seconds (and is actually accurate for the shop floor). Integrated quality inspection that catches defects in-process rather than after the fact. When you digitize the full stack -- not just the front end, but the production floor itself -- two things happen simultaneously: cost per part drops by an order of magnitude, and lead time collapses from weeks to days.


@sendcutsend is a good proof of concept. Starting in 2018 with custom sheet metal parts, they now exceed $100M in annual revenue, bootstrapped, with ~400 employees. Revenue per employee is ~$250k, which rivals top-tier saas companies and far exceeds traditional manufacturing. They did not build a better quoting tool. They rebuilt the entire production process from end to end -- the machines, the nesting, the material handling, the finishing, the shipping -- and code to control all of it. The instant quote is a side effect of having rebuilt everything underneath it. The customer sees a simple upload-and-buy interface. What they do not see is a fully reimagined factory floor.


This model is replicable across virtually every intermediate manufacturing niche. Find a niche where lead times are pain, and the market is fragmented across hundreds of small shops and process time is extraordinarily long. Rebuild the production process with technology. Absorb the market.


The endgame is not "manufacturing, but with better software." The endgame is factories as the product. Capital expenditure lines convert to operating expenditure. The factory becomes ultra-flexible, capital-efficient, operated by smaller teams. Customers upload files and gets parts/products, the same way compute works on AWS. The complexity is obfuscated. The vertical integration is total. The result is a glut of accessible production capacity that can be pointed at any problem, scaled to any volume, and flex between product lines overnight. That is what technology does to manufacturing. Not automation for its own sake. Conversion of rigid, capital-intensive production into elastic, software-defined capacity.


A critical nuance: this is not a saas play. The horizontal software approach -- build a quoting tool or marketplace that sits on top of existing job shops is a tough sell if we want real change. Xometry proved this. A quoting service that farms jobs out to the same fragmented shops can improve discovery but cannot fundamentally change the cost structure, quality consistency, or lead time of the underlying production. The efficiencies that matter are deeply vertical: controlling the machines, the scheduling, the toolpath generation, the quality inspection, the shipping.


The Consolidation Dynamic


The existing U.S. intermediate manufacturing sector is radically fragmented. Thousands of small machine shops, sheet metal fabricators, welding shops, and job shops, many operating out of buildings without HVAC, running 30-year-old equipment, with 25-30% utilization rates. These shops survive on local relationships and low overhead, but they cannot offer 3-day lead times or consistent quality because they have not rebuilt their production processes. A tech-enabled manufacturer running the same class of equipment at 70-80% utilization -- because software controls the machines, sequences the jobs, manages the material, and handles quality in-process -- has a structural cost advantage that no amount of relationship selling can overcome. As digitized manufacturers scale, they absorb these shops' customer bases. The number of firms in each niche will decrease dramatically. The surviving firms will be much larger, with much higher capital intensity, much higher margins, and much higher revenue per employee.


This is the pattern that VCs missed for years because the perceived TAM for "a single manufacturing company" seemed small. The mistake was not accounting for the consolidation multiplier -- or the volume trajectory. A digitized sheet metal company like rmfg.com (@KennethCassel) or investment casting like rangeview.com (@cameron62s) starts by serving every small-quantity customer in the country: hobbyists, hardware startups, defense contractors, automotive prototypers. But the same factory that runs 200 different part numbers a month at high utilization can also run 10 part numbers at 10,000 units each. The architecture that solves high-mix also solves high-volume, because the underlying capability is the same: software-controlled machines, optimized scheduling, and automated material flow. The addressable market is not "one job shop's revenue." It is the aggregate revenue of the entire niche, from prototypes through production runs. Manufacturing is 10% of U.S. GDP. Even capturing 1% of that through digitized consolidation is $30B.


The Automation Misconception


A common misreading of this thesis is that it is about replacing workers with robots. It is not. The U.S. does not have a surplus of expensive machinists that need to be automated away. It has a shortage of skilled machinists (40% over 55, retirements outpacing new entrants) and a surplus of low-wage hourly workers who cannot currently participate in manufacturing because the existing shops require years of apprenticeship. The correct automation strategy is to shift labor: use software and robotics to convert tasks that currently require a $45/hour skilled programmer into tasks that a $20/hour operator can perform with software assistance. Automate the skill, not the person. You can go drive Uber for that money otherwise. The robot arm loads and unloads parts. The software generates the toolpath. The operator monitors the cell. This is labor-shifting, not labor-replacing, and it expands the potential manufacturing workforce (and market) rather than shrinking it.


There is a second-order effect that compounds the consolidation dynamic. When it costs $50,000 and takes 6 months to get custom machined parts for a new product, hardware companies face enormous barriers just to prototype. When a digitized manufacturer delivers those same parts for $5,000 in a week, the barrier drops by an order of magnitude. More hardware companies get started, which generates more demand for manufacturing, which pushes manufacturers further down the learning curve. And because those manufacturers are also producing the capital goods that other manufacturers need -- fixtures, jigs, enclosures, brackets, motor housings -- the cost of building new factories falls too. Cheaper intermediate goods lead to cheaper capital goods lead to more factories lead to cheaper intermediate goods. It is a flywheel, and it is the same flywheel that made Shenzhen what it is.


Speed Propagates


The implications for the stack ranking are direct. Every category on the list below benefits from this digitization. A digitized PCB manufacturer collapses the procurement cycle for every hardware company in the ecosystem. A digitized precision machining company cuts lead times from months to days for aerospace and space launch customers. A digitized actuator manufacturer makes it possible for robotics startups to iterate on hardware as fast as software companies iterate on code. Speed propagates through the ecosystem. Each fast supplier makes every downstream customer faster, which generates more demand for fast suppliers. This is the network effect of the American Shenzhen: not just geographic density, but temporal density. The ecosystem accelerates when every node in it can move at software speed. Most OEMs can't even calculate how much time to market costs them (immense).


## Part II: The Dual-Use Imperative -- Why Pure Defense Is a Strategic Blunder


Aside from nuclear weapons, America's single most intimidating deterrent has always been its ability to outproduce everyone on Earth. That was true in 1943 and it needs to be true again. But the path to restoring that capability is not through the defense industrial base. It is through the commercial base. A country with deep, fast, flexible commercial manufacturing can surge production for any purpose. A country with a bloated defense-only supply chain can produce expensive weapons slowly and nothing else.


The Government Itself Wants Commercial-First


On November 7, 2025, Secretary Hegseth declared the Defense Acquisition System "dead" and announced the Warfighting Acquisition System (WAS). The central pillar: a "commercial-first" policy that prioritizes commercially available solutions over custom government requirements.


The FY 2026 NDAA reinforced this with Section 1826, which creates sweeping regulatory relief for nontraditional defense contractors -- firms that have not held CAS-covered contracts in the prior year. The entire direction of Pentagon acquisition reform is toward buying from commercial companies, not toward creating more defense-only suppliers.


This is not abstract policy. It reflects a hard-learned lesson: the defense industrial base atrophies when it is severed from commercial markets. Companies that sell only to the DoW lose access to the fastest-moving commercial technology. Their iteration cycles slow. Their talent pipelines narrow. Their cost structures bloat under the weight of compliance overhead.


The Revenue Mix That Markets Reward


The market data is unambiguous on this point:

- Palantir trades at extraordinary multiples in part because it moved from ~100% government revenue to a 55/45 government/commercial split, with U.S. commercial revenue growing 90%+ YoY. The commercial revenue is what gives investors confidence in the durability and scalability of the business.
- SpaceX holds $22B in government contracts but Starlink's commercial revenue is what makes it the most valuable private company in the world. Government contracts de-risk the business; commercial revenue provides the growth trajectory.
- Traditional primes -- Lockheed Martin derives 71% of revenue from U.S. government contracts. RTX and Boeing are around 50%. These companies trade at 1.5-2.5x revenue, a fraction of what dual-use companies command.

Financial markets in Europe have demonstrated this quantitatively: companies with higher dual-use R&D intensity saw significantly higher valuation premiums during the defense spending surge. The market is not rewarding defense revenue per se. It is rewarding the combination of defense demand with commercial scalability.


The 75/25 Rule


The optimal revenue mix for a dual-use manufacturing company targets no more than 25% of revenue from defense and government contracts. The reasoning:

1. Procurement cycle risk. Government contracts operate on political timelines. Administrations change. Programs get cancelled. A company at 50%+ defense revenue faces existential risk from a single budget cycle. Defense contractors with multi-year agreements have predictable revenue, but over-reliance on major contracts creates vulnerability to cancellations or scope reductions.
1. Nontraditional contractor status. Under 10 U.S.C. Section 3014, a company loses its "nontraditional defense contractor" designation once it has held a full CAS-covered contract in the prior year. Losing this status triggers expensive compliance requirements -- cost accounting systems, certified pricing teams, DCAA audit readiness -- that can consume 5-15% of revenue in overhead. Keeping defense below 25% helps preserve the regulatory advantages of nontraditional status.
1. Talent and culture. The best manufacturing engineers, roboticists, and software developers want to work on products that ship to millions of users, not products that sit in classified programs for years. A 75/25 commercial/defense split keeps the company's talent proposition competitive with pure commercial tech companies.
1. Valuation multiple compression. The market applies defense-contractor multiples (1.5-3x revenue) to companies perceived as defense-dependent. The same business, positioned as a commercial manufacturer that also serves defense, commands 5-15x revenue. The framing is not cosmetic. It reflects genuine structural differences in growth rate, margin trajectory, and exit optionality.
1. DIU and the DoD want this. The Defense Innovation Unit's Commercial Solutions Opening process is explicitly designed to pull commercial technology into defense applications. The Pentagon's reform direction is toward buying from companies whose primary business is commercial. A company that builds its factory around commercial volume and allocates 25% of capacity to defense is exactly what the government is trying to incentivize.

Policy: What Helps and What Hurts


Not all industrial policy is created equal. Tariffs on machine tools are among the most counterproductive. The U.S. produces a small fraction of the CNC mills, lathes, grinders, press brakes, laser cutters, and injection molding machines that its factories run on. The overwhelming majority comes from Japan, Germany, Taiwan, South Korea, and increasingly China. A tariff on machine tools raises the capital cost of building every factory this thesis calls for. It makes the next SendCutSend or Hadrian slower to scale unless the government pays for your capex. It makes every job shop's next capacity expansion harder to justify. The customers of American machine tool imports are American manufacturers. Policy that raises costs slows the flywheel.


What helps most is not tariffs but speed. Regulatory certification calendars are a major bottleneck: a product that takes 3 weeks of actual testing but 6 months of calendar time to certify is being taxed by bureaucratic throughput, not by the rigor of the test itself. Compressing certification timelines to match actual test durations would accelerate the entire ecosystem. Similarly, permitting reform for factory construction matters more than subsidies for factory operation. A factory that takes 3 years to permit and build is 3 years of learning curve that never happens.


The best industrial policy creates conditions for the flywheel to spin faster: fast permitting, fast certification, workforce training that expands the labor pool for tech-enabled manufacturing, and targeted tariffs that protect domestic capacity where it actually exists rather than blanket tariffs that punish domestic buyers.


There Is No Such Thing as Low-Value Manufacturing


The most destructive idea in American industrial policy is the notion that some manufacturing is "low value" and can be safely offshored while we retain the "high value" work. This is wrong, and it is the reason we are in this situation. To this end, we could build a plastic fork factory that's more advanced than a TSMC fab.


All manufacturing knowledge compounds. The engineer who designs a cutting-edge semiconductor package cannot do their job if the country has forgotten how to do precision surface treatment, or if there is no domestic supplier of the ceramic substrates, or if the tooling for the test fixtures has to come from overseas with a 12-week lead time. You cannot build advanced things if you have lost the ability to build basic things. The knowledge is not separable. The person who knows how to run a CNC lathe and the person who knows how to grind optical lenses and the person who knows how to mix polymer compounds are all load-bearing members of the same system. When you offshore the "low value" layers, you do not free up resources for the "high value" layers. You cut the foundation out from under them.


This is why the American Shenzhen thesis does not draw a line between mass production and flexible production, or between commodity parts and advanced parts. The goal is a manufacturing ecosystem that does both, because they reinforce each other -- and because the technology that unlocks one unlocks the other. The shop that can run 200 different part numbers a month at high utilization can also run 10 part numbers at 50,000 units each, because the underlying architecture is the same. The shop that mass-produces aluminum brackets at volume is also the shop that can prototype a one-off bracket for a new satellite bus in 3 days, because the machines are the same, the materials knowledge is the same, and the workforce is the same. Volume production funds the learning curve. Flexible production keeps the workforce sharp and the customer base diverse. The lesson of every modern conflict, from Korea to Ukraine, is that the ability to retool, adapt, and produce across a wide mix of products matters as much as raw volume. A country that can do both is resilient. A country that has outsourced half the stack and retained only the "fancy" parts is fragile in ways that do not become obvious until it is too late.


The U.S. should not be choosing between mass production and flexibility. It should be building a manufacturing ecosystem so deep and so fast that the question of Chinese component dependency becomes moot -- because anything that was previously sourced from abroad can be made domestically, on demand, at competitive cost, at any volume.


Three areas demand particular urgency because they are approaching the point of no return:


Humanoid robotics. If China builds a few hundred thousand humanoid robots and those robots help them build a million more, the game is over. That is not a linear scaling problem. It is a recursive one. Robots that build robots is full industrial capture -- a manufacturing workforce that does not age, does not strike, does not emigrate, and whose marginal cost drops with every unit produced. The U.S. has the best robotics AI labs in the world. What it does not have is the domestic actuator, motor, and drive system manufacturing base to produce humanoids at scale. That supply chain is the bottleneck, and it is on this list for exactly that reason.


Drones. Ukraine proved that low-cost autonomous systems are the defining weapon of modern warfare, and that the ability to produce them in volume and iterate on them weekly matters more than any single platform's capability. China is already the world's dominant drone manufacturer by a wide margin. The U.S. needs domestic drone production not just for defense but because drones are becoming infrastructure: agricultural, logistics, inspection, mapping. Ceding that category means ceding both a defense capability and a commercial market.


The electric stack. Batteries, power electronics, motors, inverters, chargers -- the full electrification layer that undergirds modern production. Every robot, every drone, every EV, every grid storage system, and every data center runs on this stack. China controls the majority of global battery cell production and a dominant share of the upstream materials processing. The U.S. has the IRA tailwinds and the raw material base (especially through recycling) to build this domestically, but the window is not indefinite. Every year of delay is another year of Chinese learning curve advantage that becomes harder to close.


## Part III: The Stack Ranking


Each category is evaluated on three dimensions scored 1-5:

- Ecosystem Criticality (EC): How essential is this manufacturing category to creating a self-reinforcing domestic production ecosystem? A score of 5 means "nothing else works without this."
- Venture Return Potential (VR): Does this category support the new return class? High learning rates, proprietary process IP, hybrid revenue models, defensible margins.
- Dual-Use Fit (DU): Can this category sustain a 75/25 commercial/defense mix with large addressable markets on both sides?

Composite Score = EC + VR + DU (max 15)


## Tier 1: The Foundations (Score 13-15)


1. Specialty Materials, Advanced Composites, and Material Refining


EC: 5 | VR: 4 | DU: 4 | Total: 13


Carbon fiber, specialty polymers, engineered proteins, advanced ceramics -- and upstream of all of them, the refining and processing of raw materials into usable feedstock. The U.S. is critically dependent on foreign sources for many advanced materials. The materials layer is upstream of everything else on this list -- you cannot machine, print, or assemble products without feedstock.


This category extends all the way to ore processing, rare earth separation, and permanent magnet manufacturing. China controls roughly 60-70% of global rare earth processing and over 90% of permanent magnet production. Every motor on this list, every actuator, every generator needs magnets. MP Materials is mining and beginning to process rare earths domestically. USA Rare Earth is building separation and magnet manufacturing capacity. But the gap is enormous, and every year of delay is another year of Chinese learning curve advantage on the processing side. The return profile for refining is different from the rest of this stack rank -- flatter learning curves, heavier capital requirements, longer timelines. It is more of an infrastructure problem than a consolidation problem. But it is a load-bearing dependency, and ignoring it means the entire ecosystem still has a Chinese chokepoint at the bottom of the supply chain.


Venture return case: Materials companies that achieve process breakthroughs have some of the deepest moats in manufacturing. The learning curves are steep, the capital requirements create barriers, and the qualification timelines (especially in aerospace) create multi-year lock-in with customers. Refining and magnet production are harder venture fits -- the capital intensity is high and the margins are thinner -- but DOE loan programs, Section 45X production tax credits, and defense stockpile mandates are creating investable pathways that did not exist five years ago.


Dual-use case: Lightweight composites for commercial aircraft (commercial) and hypersonic vehicles (defense). Specialty polymers for EV battery separators (commercial) and satellite structures (defense). Rare earth magnets for EV motors and wind turbines (commercial) and precision-guided munitions and satellite reaction wheels (defense).

2. Advanced Electronics Manufacturing (PCB/PCBA + Semiconductor Packaging)


EC: 5 | VR: 5 | DU: 5 | Total: 15


This is the single most critical category. Shenzhen's Huaqiangbei district -- 38,000+ businesses across 40+ market buildings, every electronic component imaginable -- is the beating heart of the ecosystem. Without domestic electronics manufacturing, every other category on this list is assembling imported subsystems.


The numbers make the case: 98% of advanced semiconductor packaging is done offshore. Electronics and electrical products accounted for 39% of announced reshoring jobs in 2023. PCBs from China carry a 25% tariff, but the U.S. still lacks capacity for even basic 2-layer and 4-layer boards (tariff exclusions have been repeatedly extended because domestic supply does not exist).


The CHIPS Act allocated $1.4B specifically for advanced packaging (NAPMP), with Amkor's $7B Arizona campus as the anchor. The U.S. Department of Commerce awarded $1.1B to Natcast's advanced packaging facility in Tempe alone. The advanced packaging market is projected to hit $83B by 2030.


Venture return case: The learning curves in electronics manufacturing are steep (15-20% cost reduction per doubling). Companies like MacroFab are building software-defined PCBA platforms. The combination of tariff-driven demand pull, CHIPS Act subsidies, and the 98% offshore baseline creates a generational reshoring opportunity. The commercial TAM (consumer electronics, automotive, industrial IoT) dwarfs defense demand.


Dual-use case: Every drone, satellite, missile, and autonomous vehicle needs PCBAs. But so does every smartphone, EV, data center, and medical device. Defense is perhaps 10-15% of addressable demand.


3. Precision Parts / Advanced Machining


EC: 5 | VR: 5 | DU: 5 | Total: 15


The U.S. precision machining supply chain has been hollowing out for decades. Nearly 40% of skilled CNC machinists are over 55, and retirements are outpacing new entrants. The machines are often 20+ years old. Lead times for aerospace-grade precision parts routinely stretch to 12-18 months.


Venture return case: Hadrian is the archetype. Software-controlled CNC factories with AI-driven process optimization, automated quality inspection, and digital thread traceability. The yield improvement dynamics from the Hsu article apply directly: going from 70% to 90% overall yield creates a $25/unit cost advantage that compounds with volume. The learning curve is steep because each new part program teaches the system's software.


Dual-use case: SpaceX, Rocket Lab, Relativity, and every launch provider need precision machined parts. So does Boeing's commercial aviation division, every semiconductor equipment maker, and the entire medical device industry. Defense is a meaningful but minority market.


4. Robotic Systems / Actuator / Motor Manufacturing


EC: 4 | VR: 5 | DU: 5 | Total: 14


Robotics funding hit $10.3B in 2025 (36% above 2024), with Q2 alone seeing $8.8B in deal value. But here is the critical insight: the robots are only as good as the actuators and motors inside them. Figure AI ($39B valuation), Apptronik ($403M raise), and the entire humanoid robotics wave are all constrained by the same bottleneck: who manufactures the high-performance actuators, motors, and drive systems at volume?


This is the components layer -- the equivalent of Shenzhen's component kiosks but for electromechanical systems. Companies like HLabs (YC-backed, building the actuator supply chain in the USA) and RISE Robotics (selected for the $46B EWAAC program) are early movers.


Venture return case: The robotics market is projected at $185B by 2030. Every robot needs 6-40+ actuators. The actuator is the Bill of Materials equivalent of the GPU in AI: the component whose cost, performance, and availability determines the economics of the entire system. Wright's Law applies aggressively here -- servo motor costs have followed an ~18% learning curve historically.


Dual-use case: Humanoid robots for warehouse logistics (commercial) and explosive ordnance disposal (defense). Drone motors for agricultural spraying (commercial) and ISR missions (defense). Industrial actuators for assembly lines (commercial) and unmanned ground vehicles (defense). The commercial market is 10-20x the defense market.


5. Forming Methods: Mold & Die, Casting, Molding, Stamping, Forging, RTM


EC: 5 | VR: 5 | DU: 5 | Total: 15


This is arguably the most foundational category on the list. Tool and die makers are the mystic greybeards of manufacturing -- the person who cuts the steel molds that produce every plastic enclosure, every cast aluminum housing, every stamped bracket. Without domestic tooling, you do not have domestic manufacturing. You have domestic assembly of imported parts.


This category spans every process where material is shaped by a tool or a mold: injection molding, die casting, investment casting, stamping, forging, and resin transfer molding (RTM) for composites. Shenzhen's dominance in consumer hardware is built on a layer of tens of thousands of injection molding shops, die casters, stampers, and forming operations that can turn around a prototype mold in a week or two and produce parts in hours. The U.S. has steadily lost this capability. American tool-and-die shops have been closing for decades, and lead times for production injection molds in the U.S. routinely stretch to 8-16 weeks. In Shenzhen, the same mold takes 4-6 weeks. That gap is not primarily about labor cost. It is about fragmentation, the complexity of tooling design and iteration, and the absence of technology in the design-to-production pipeline.


Tooling is where technology has the most leverage. The mold itself is a production process dominated by skilled labor, design iteration, and testing. A block of tool steel is not expensive. It can often be machined into a mold within hours. The months of calendar time come from quoting, design iteration, manual CAM programming, and the back-and-forth between customer and shop. Software can generate the design, program the machines, and simulate the mold-fill before cutting steel. The same dynamics apply to forging -- where open-die and closed-die forging shops face identical quoting and design bottlenecks -- and to RTM, where composite layup and resin infusion are ripe for software-driven process control and automated fiber placement.


The collapse of tooling lead time has second-order effects that ripple through the entire ecosystem. When molds take 12 weeks, product cycles are necessarily long. Design changes are expensive. Iteration is slow. When molds take 2 weeks (or tooling is eliminated entirely), product cycles can compress by 4-8x. Hardware companies can iterate at something closer to software speed. That is the unlock for the entire American Shenzhen thesis.


Venture return case: The consolidation dynamic applies with full force: firms that have rebuilt the tooling process end to end -- automated mold design, software-driven machining, simulated testing -- will absorb the customer bases of oversea suppliers. The efficiency gains are dramatic because tooling has the highest ratio of setup, design iteration, and manual programming to actual fabrication time of any manufacturing process. The capital recycling advantage is extreme.


Dual-use case: Every consumer electronic, automotive component, medical device, and defense housing needs injection-molded or formed parts. Plastic enclosures for commercial IoT sensors (commercial) and ruggedized housings for military electronics (defense). Die-cast aluminum components for EV powertrains (commercial) and missile airframes (defense). Forged steel fittings for oil and gas (commercial) and artillery components (defense). RTM composite structures for automotive body panels (commercial) and UAV airframes (defense). The commercial market is 20-50x the defense market.


6. Battery Cell / Energy Storage Manufacturing


EC: 5 | VR: 4 | DU: 4 | Total: 13


Battery manufacturing is the most capital-intensive category on this list, and Northvolt's bankruptcy ($5.5B raised, filed Chapter 11 in November 2024) is a cautionary tale about the difficulty of competing with CATL's ~37% global market share. China's November 2025 export controls on batteries exceeding 300 Wh/kg (requiring government licenses) add urgency.


The U.S. has announced over 1 TWh of planned annual production capacity post-IRA, but multiple projects (KORE Power, FREYR) have already been cancelled. The successful plays are at the materials and chemistry layer (Redwood Materials, over $1B in equity plus billions in DOE loan commitments; Sila Nanotechnologies, ~$1.3B) and in specialized cells for defense/aerospace (Forge Nano, $100M DOE award for a 3 GWh defense-focused facility).


Venture return case: Battery cell manufacturing has one of the most well-documented learning curves in industrial history (~18% cost reduction per doubling). The challenge is surviving long enough to get down the curve. Battery tech startups raised $19.9B in 2024. The winners will be companies that find niche-to-scale pathways: start with high-value, low-volume defense/aerospace cells, accumulate learning, then expand to commercial markets.


Dual-use case: Every EV, grid storage system, consumer device, and drone needs batteries. Defense demand (soldier power, UAS, directed energy weapons) is real but small relative to the commercial market. China's export controls make domestic production a national security imperative.


## Tier 2: The Accelerators (Score 11-12)


7. Industrial Metal Additive Manufacturing


EC: 4 | VR: 4 | DU: 4 | Total: 12


Venture capital has been burned by 3D printing, a lot -- mostly because adoption rates of machines and parts are directly connected to how well each printer can control physics. Metal additive is a beast. The parts are structural, load-bearing, and flight-critical. The customers are aerospace, defense, energy, and medical -- industries that pay real money for geometries that cannot be made any other way.


The learning curves are extraordinarily steep because the entire process is software-defined -- every print generates data on melt pool dynamics, thermal distortion, and microstructure that improves the next one. The companies that accumulate the most print hours build process libraries that are effectively impossible to replicate.


Venture return case: Metal additive eliminates tooling entirely for complex geometries -- no molds, no dies, no fixtures. A topology-optimized bracket that would (maybe) require a 5-axis CNC setup and multiple operations can be printed in one shot. The capital equipment is expensive ($500K-$5M per machine), but each machine can produce any geometry from any qualified alloy, which means utilization scales with software and scheduling, not with dedicated tooling. The consolidation opportunity is in becoming the production-scale metal printing service that aerospace and defense primes cannot justify building internally -- high-mix, high-value, and impossible to source from a traditional machine shop.


Dual-use case: Rocket engine components and satellite structures (dual). Turbine blades and heat exchangers for power generation (commercial). Titanium medical implants (commercial). Replacement parts for legacy military platforms where the original tooling no longer exists (defense).


8. Sensors / Optics / Photonics Manufacturing


EC: 4 | VR: 4 | DU: 4 | Total: 12


LiDAR, infrared sensors, optical systems, photonic integrated circuits. This category is the "eyes" of both autonomous systems and precision-guided munitions. The manufacturing is highly specialized, with steep learning curves and significant process IP.


Venture return case: The autonomous vehicle and industrial automation markets create massive commercial demand. The manufacturing processes (thin-film deposition, precision optics grinding, MEMS fabrication) are amenable to software-driven optimization. The premium the market places on vertically integrated sensor manufacturing is real, though the path is treacherous -- Luminar's December 2025 bankruptcy after losing Volvo as a customer shows the risk of single-customer concentration in a capital-intensive sensor play.


Dual-use case: Autonomous vehicles (commercial) and targeting systems (defense). Industrial machine vision (commercial) and ISR payloads (defense). Telecom photonics (commercial) and secure communications (defense).


9. Industrial Robots & Automation Cells


EC: 4 | VR: 4 | DU: 4 | Total: 12


Every factory on this list needs robots. Semiconductors, batteries, munitions, motors, PCBs -- none of them scale without programmable arms, welding cells, and material handling systems on the floor. Industrial automation is the connective tissue of the entire stack. And right now, almost all of it comes from four companies: FANUC, ABB, KUKA (Chinese-owned since 2016), and Yaskawa. All foreign. The U.S. has no top-10 industrial robot OEM. For a country trying to reshore its entire manufacturing base, this is not a gap. It is a structural dependency.


The opportunity is not to build a better six-axis arm. The opportunity is to collapse the integration cost. Today, buying a robot is 30% of the problem. Programming it, fixturing it, integrating it into a production cell, and maintaining it is the other 70%. That integration cost is what keeps small and mid-size manufacturers -- the backbone of any real supply chain ecosystem -- from automating at all. The companies that win here will sell complete automation cells, not components. Robot-as-a-service models that eliminate the $200K+ upfront capital expenditure. AI-native programming that replaces six months of systems integration with a weekend of teach-and-repeat. Modular workcells that reconfigure for HMLV production runs -- the exact profile of defense and aerospace manufacturing.


Venture return case: The global industrial robotics market is north of $55B and growing at 10%+ annually. But the real margin is not in hardware. It is in the software and integration layer, where gross margins look like SaaS, not like metal bending. RaaS (robots-as-a-service) models convert what was a cyclical capex sale into recurring revenue with 80%+ retention. Path Robotics raised $271M to put AI behind welding torches. Formic raised $159M selling robot-hours instead of robots. The playbook is the same one that worked in cloud computing: turn a capital asset into an operating expense and watch adoption explode. The acquirer pool is deep -- every industrial conglomerate, every defense prime, and increasingly every major automaker is a buyer.


Dual-use case: The DoD needs flexible automation more than anyone. Arsenal and depot maintenance facilities are running 1980s-era equipment with a workforce aging out faster than any private sector equivalent. Submarine maintenance, missile assembly, vehicle refurbishment -- all of these are HMLV production environments where reconfigurable automation cells are the only path to surge capacity. A welding cobot that learns a new joint geometry in hours instead of weeks is not a convenience in a defense context. It is the difference between a production rate that matches the threat and one that does not.


## Tier 3: The Enablers (Score 9-10)


10. Power Electronics / GaN-SiC Device Manufacturing


EC: 4 | VR: 3 | DU: 3 | Total: 10


Wide-bandgap semiconductors (gallium nitride, silicon carbide) are the enabling technology for efficient power conversion in EVs, renewable energy, data centers, and directed energy weapons. The manufacturing is specialized and capital-intensive.


Venture return case: Strong learning curves, growing demand, limited domestic capacity. But the capital requirements are high and the timeline to profitability is long.


Dual-use case: EV drivetrains and chargers (commercial). Directed energy weapons and radar systems (defense). Data center power supplies (commercial).


11. Industrial Chemicals and Precursors


EC: 4 | VR: 3 | DU: 3 | Total: 10


Every manufacturing process on this list consumes chemicals that most people never think about. The PCB fab needs etchants and plating solutions. The anodizing shop needs acid baths and sealants. The composite layup needs resin systems and hardeners. The machine shop needs cutting fluids and coolants. The injection molder needs mold release agents. These are not glamorous products, but without domestic supply of them, every factory in the ecosystem is importing consumables on 6-8 week lead times from overseas suppliers -- which means the 2-hour supply chain has a hidden bottleneck at the chemical layer.


Solugen is the proof that this category can be venture-backable. They produce industrial chemicals (hydrogen peroxide, organic acids, chelants) from bio-based processes at their Houston Bioforge, replacing petroleum-derived chemicals with enzymatic manufacturing. The process IP is deep, the margins improve with scale, and the customer base spans water treatment, oil and gas, agriculture, and industrial manufacturing. The model is factory-is-the-product applied to chemistry: proprietary bioprocesses running in purpose-built facilities, with learning curves on yield and throughput.


Venture return case: The industrial chemicals market is enormous but historically commoditized. The venture angle is in process innovation -- companies that can produce the same chemicals through novel processes (bio-based, electrochemical, continuous flow) at lower cost, lower environmental burden, and with domestic supply security. The moats are in the process IP and the qualification timelines -- once a chemical is qualified into a manufacturing process, switching costs are high.


Dual-use case: Plating chemistries for electronics and aerospace (dual). Specialty resins for composite structures in commercial aviation (commercial) and missile bodies (defense). Cleaning and surface preparation chemicals for semiconductor fabs (commercial) and defense optics (defense).


12. Machine Tool Manufacturing


EC: 4 | VR: 3 | DU: 3 | Total: 10


This is the category the policy section already calls out: the U.S. barely makes the machines that its factories run on. CNC mills, lathes, grinders, press brakes, laser cutters, injection molding machines, wire EDMs -- the capital equipment that every other category on this list depends on comes overwhelmingly from Japan (Mazak, Okuma, Makino), Germany (DMG Mori, Trumpf), Taiwan (Tongtai, Fair Friend), and increasingly China. The U.S. share of global machine tool production has been declining for decades. Haas is the largest remaining American builder of CNC machines, and they are an outlier.


This matters for the thesis because every factory buildout on this list is a machine tool purchase order. If the American Shenzhen requires hundreds of new factories, that is billions of dollars in machine tools flowing to foreign manufacturers. The ecosystem is building domestic production capacity while depending entirely on imported production equipment. That is a structural vulnerability -- not just for supply chain reasons, but because the country that builds the machines accumulates the process knowledge about how the machines should work, which feeds back into better machines, which feeds back into better manufacturing. It is a learning curve the U.S. is not on.


Venture return case: Machine tools are a harder venture fit than most categories on this list. The incumbents are entrenched, the capital requirements are high, and the sales cycles are long. But the opportunity is in the same digitization thesis that applies everywhere else: the machine tool of the future is software-defined, sensor-dense, and self-optimizing. A new entrant that builds machines designed from scratch around closed-loop process control, integrated metrology, and AI-driven toolpath optimization would have a structural advantage over incumbents bolting software onto 30-year-old mechanical architectures.


Dual-use case: Every factory on this list -- commercial or defense -- needs machine tools. The dual-use case is inherent. A CNC mill is a CNC mill whether it is cutting parts for an EV motor or a missile guidance system.


Part IV: The 2-Hour Supply Chain -- A Concrete Ecosystem Map


The stack ranking above is not arbitrary. It follows the logic of what makes Shenzhen work: vertical integration through geographic density. But to move from abstraction to actionable blueprint, we need to make this concrete. What does the American Shenzhen actually look like, building by building, capability by capability?


In Shenzhen, a hardware startup can walk to a component market, buy parts, walk to a PCBA shop, get boards assembled, walk to an injection molder, get enclosures made, and walk to a test house -- all within a 2-hour radius. Each of these capabilities reinforces the others. The PCB shop exists because the component market exists because the assembly shops exist because the customers exist.


The American Shenzhen requires the same reinforcing density. Here is the concrete ecosystem, organized into five layers that map to the "2-hour supply chain" -- the cluster of capabilities that must exist within rapid transit distance of each other for the flywheel to spin.


Layer 1: The Electronics Nervous System


PCB fabrication, component assembly, and component stocking -- the categories detailed in the stack ranking's #2 position. The key ecosystem requirement that the ranking does not capture is co-location. A PCBA shop is only as fast as its access to components. The American version of Huaqiangbei is not a bazaar but a network of micro-distribution nodes: small, regionally co-located component warehouses holding the 5,000 most common SKUs for immediate pickup, integrated directly with the PCBA shops' BOMs. DigiKey and Mouser handle long-tail distribution well. What the 2-hour supply chain needs is same-hour access to common passives, connectors, and ICs within the cluster itself.


Layer 2: The Physical Structure -- Metal and Plastic


CNC machining, injection molding, casting, forging, sheet metal -- the categories covered in #3 and #5 of the stack ranking. The ecosystem insight here is sequencing: a machined part often needs surface treatment before it can ship, an injection-molded part needs a mold that was itself machined, and a cast part needs post-machining to hit tolerance. These layers are not independent. They are a workflow, and the 2-hour supply chain only works if the handoffs between them are measured in hours, not weeks. The surface treatment and finishing sub-layer (anodizing, powder coating, electroplating, passivation) is the most overlooked link in this chain. A machined aluminum part is not a finished product until it has been anodized. Every forming process terminates at a finishing process, and domestic finishing capacity is thin, fragmented, and undigitized.


Layer 3: The Material Refiners -- The Chemical Layer


Polymer compounding, specialty materials, and the industrial chemicals detailed in #1 and #11. The ecosystem dependency is simple: without domestically available feedstock and process chemicals, every factory in the cluster is importing consumables on 6-8 week lead times, and the 2-hour supply chain has a hidden bottleneck at the bottom of the stack.


Layer 4: The Battery and Energy Hub


Cell components, cell assembly, pack integration, and power electronics -- the categories covered in #6 and #10. The ecosystem role is straightforward: electrification cuts across every product category, and the cluster needs a domestic battery and power electronics layer within reach.


Layer 5: Testing and Speed Enablers


This layer is not covered in the stack ranking because these are not manufacturing companies per se, but they are load-bearing members of the 2-hour supply chain.


Testing and Certification Labs. UL, FCC, CE, MIL-STD, DO-160, IP ratings. Every product that ships needs to pass regulatory testing. A hardware startup that can get a product tested and certified in 5 days instead of 5 weeks has a compounding time advantage across every product cycle. Fast domestic test labs are a bottleneck that constrains the speed of the entire ecosystem.


Micro-Logistics and Regional Fulfillment. Same-day couriers, regional freight, and co-located warehousing that move parts between layers at the speed the ecosystem requires. This is the difference between a cluster that operates at Shenzhen speed and a collection of factories that happen to be in the same state but still ship parts to each other via 3-day ground.


Full-Stack Design and Engineering Firms. Companies that help hardware startups go from concept to manufacturable design -- mechanical, electrical, industrial design, and DFM in an integrated workflow. These firms are the on-ramp to the ecosystem. They translate a founder's idea into files that the PCB fab, the machine shop, and the mold maker can actually produce.


Temporal Density: The Network Effect That Matters Most


The critical insight is that the American Shenzhen network effect is not merely geographic proximity. It is temporal density -- the propagation of speed through the ecosystem. Each fast supplier makes every downstream customer faster, which generates more demand for fast suppliers.


When the PCB fab turns boards in 24 hours, the PCBA shop can assemble in 48 hours, and the test lab certifies in 5 days, a hardware startup can go from design file to tested prototype in under two weeks. That is competitive with Shenzhen. That speed advantage attracts more startups, which generates more volume, which pushes every supplier further down the learning curve, which makes them faster, which attracts more startups.


The venture opportunity is not in any single layer. It is in building companies at each layer that reinforce the ecosystem, creating the density of capability that makes the next company at the next layer viable. The companies that anchor this flywheel earliest will ride the steepest part of the learning curve, accumulate the most production volume, and build the deepest moats.


The Missing Layer: A Common Manufacturing Protocol


There is one thing Shenzhen has that the American version currently lacks, and it is not a factory or a material or a machine. It is a common language.


In Shenzhen, the density is so extreme that informal standardization happens organically. Everyone knows the file formats, the quoting conventions, the BOM structures, the shipping expectations. The ecosystem is interoperable by default because everyone is within walking distance and has been doing business with each other for decades.


The American version will not have that luxury. The companies in this ecosystem are geographically distributed, newly founded, and building from scratch. Without deliberate effort, each one will build its own proprietary quoting format, its own API, its own way of representing parts, materials, tolerances, and delivery expectations. The result will be a collection of fast, digitized manufacturers that still cannot talk to each other efficiently.


What this ecosystem needs is a common manufacturing protocol -- something analogous to what TCP/IP and HTTP did for the internet. Not a marketplace. Not a platform that extracts rent. A shared, open protocol layer that defines how manufacturing nodes communicate: how a design file moves from a customer to a CNC shop to a surface treatment house to a test lab with full traceability and no manual re-entry. How a BOM propagates across suppliers with real-time availability and pricing. How quality data flows back upstream so that a yield issue at the PCBA shop triggers a design revision at the engineering firm within hours, not weeks.


The internet did not become the internet because one company built a better network. It became the internet because TCP/IP gave every network a common way to interoperate. The result was that each new node made every existing node more valuable. The American Shenzhen needs the same dynamic: each new digitized manufacturer should make every existing manufacturer more capable, more visible, and more accessible. That requires a protocol, not a platform.


The elements of this protocol are not exotic. Standardized file interchange for manufacturing (extending STEP/3MF with process metadata), real-time capacity and quoting APIs, common quality and traceability schemas, and logistics integration for handoffs between suppliers. Some of this exists in fragments -- STEP files for geometry, IPC standards for PCBs, AS9100 for aerospace quality. But no one has stitched it into a coherent, software-native protocol that a new manufacturer can adopt on day one and immediately become interoperable with every other manufacturer in the ecosystem.


The company or consortium that builds this protocol will not capture value the way a marketplace does. It will capture value the way Cisco captured value from TCP/IP: by being the infrastructure that makes the protocol useful. The protocol itself should be open. The tools, visibility layers, and orchestration software that run on top of it are where the business model lives. And the existence of the protocol is what turns a collection of individual fast manufacturers into an actual ecosystem -- one where a customer can submit a multi-part assembly and have it automatically routed, quoted, produced, and assembled across a dozen specialized shops, with full traceability, in days instead of months.


That is the last piece. The factories are the muscles. The protocol is the nervous system.


Part V: The Market Is Catching On


I am not a venture investor™️, but I am an industrialist and therefore equipped with advanced finance spells. I am not going to pretend to derive multiples from first principles. But the data is worth laying out because it shows that the market is independently arriving at the same conclusion this document is built around: tech-enabled manufacturing is not traditional manufacturing, and the repricing is underway.


The Valuation Gap


There is a persistent and widening gap in how the market prices different business models:


The 2025 data point is striking: median EV/EBITDA for industrial strategic acquisitions jumped to 14.7x from 8.0x in 2024. This is not noise. It reflects a market that is beginning to re-price manufacturing companies that exhibit software-like characteristics: recurring revenue from capacity contracts, proprietary process IP protected by learning curves, and margin expansion driven by yield improvement rather than headcount growth.


Why the Gap Is Closing From Both Directions


The repricing is not just manufacturing multiples going up. It is software multiples coming under pressure from a direction most VCs have not fully internalized: AI is eating software alive.


The median SaaS company operates at -6% EBITDA margin. Negative. These are businesses that burn cash by design to collect big bags, and the moats they were supposed to build are dissolving in real time. AI coding agents can now generate, test, and deploy production-quality software. The marginal cost of producing a SaaS competitor is collapsing toward zero. Every vertical SaaS company that justified its multiple on the basis of switching costs and workflow lock-in is now competing against an AI agent that can replicate its core functionality in a weekend. The only software businesses that are safe are the ones nobody actually wants to use but everyone is contractually trapped in -- the Oracles, the SAPs, the Workdays. Enterprise garbage with 7-year contracts and migration costs that exceed the GDP of small countries. That is not a moat. It is a hostage situation. And it is not a category that justifies 20-50x revenue multiples.


Meanwhile, a tech-enabled manufacturer operates at 15-25%+ EBITDA margin with learning curve moats that deepen with every unit produced. You cannot fork a factory. You cannot prompt-engineer your way to a 15% learning curve advantage. You cannot train a model on someone else's cumulative production volume. The process IP lives in the machines, the tooling, the workforce, and the millions of parts that have already been made. Anduril at ~30x revenue and Hadrian at $1.6B are not anomalies. They are the market's first attempt at pricing a category of business whose moats are rooted in physics, not code.


The Deep Tech Return Paradox


There is a data point that most VCs are not aware of: defense, space, and life science companies have 2-5% odds of achieving $250M+ exits, while SaaS, fintech, and AI/ML companies have 1-1.5% odds. The per-company probability of a large exit is roughly twice as high in deep tech as in software. The exits also arrive 6-24 months sooner on average.


The reason this has not historically translated into superior fund-level returns is that deep tech funds have been smaller and the category has been undercapitalized. That constraint is lifting: defense tech VC funding hit $49.1B in 2025, more than doubling from $27.2B the prior year. Equity funding for defense tech startups specifically jumped from $7.3B to $17.9B.


What This Means


The correct mental model is not "manufacturing company valued like software." It is: a new category of business whose value accrues through process IP and learning curves, monetized through a hybrid of capacity contracts and unit economics, defended by capital intensity and real assets, and valued at multiples that reflect the durability and compounding nature of the moat.


The 14.7x EV/EBITDA median for industrial strategic acquisitions in 2025 is the market's first approximation of what this new category is worth. It will go higher as the pattern becomes better understood -- and as the market simultaneously recalibrates what software businesses are actually worth in a world where AI can write code but cannot run a factory.


That is the return thesis. Not "manufacturing, but with software." Rather: the construction of an industrial ecosystem whose network effects compound through learning curves, whose temporal density creates self-reinforcing demand, whose moats deepen with every unit produced, whose downside is bounded by real assets, and whose returns accrue to the companies that moved first -- at the exact moment the asset class that absorbed the majority of venture capital for the last fifteen years is watching its moats get eaten by robots.


American Shenzen: A Company Map


1. Specialty Materials, Advanced Composites & Material Refining

- Axial Composites (axialcomposite.com / axco.industries) — Non-planar carbon fiber/thermoplastic composites. Automated fiber-injection cells, days vs. weeks. YC-backed.
- Layup Parts (layupparts.com) — On-demand composite parts + tooling, no minimums, tech-enabled speed and cost. Huntington Beach, CA
- Fiber Dynamics (@FiberDynamics / fiberdynamics.net) — High-performance aerospace/defense composite structures via proprietary LCRTM tech. Wichita, KS
- Boston Metal (bostonmetal.com) — Green steel via Molten Oxide Electrolysis. Electricity in, steel out, zero CO2. Woburn, MA
- Bethlehem Steel Corp (@BethSteelCorp) — Symbolic domestic steel revival effort repurposing historic sites for new U.S. manufacturing. Bethlehem, PA
- Nox Metals (@noxmetals / noxmetals.co) — AI-powered automated metals supply/processing. Plate, sheet, fast turnaround. YC-backed. Detroit, MI
- Duranium (duranium.co) — Carbon-neutral production of Ti, Mg, Al, Zr, Hf via CO2-recycling carbochlorination. U.S. reshoring focus. Alameda, CA

## 2. Advanced Electronics Manufacturing (PCB/PCBA + Semiconductor Packaging)

- MacroFab (@MacroFab / macrofab.com) — Software-defined PCBA. Digital platform for on-demand PCB assembly, proto to mass production, North American factories. Houston, TX
- Finwave Semiconductor (finwavesemi.com) — GaN-on-Silicon (3DGaN FinFET) for high-performance RF/power in 5G/6G and infrastructure. Waltham, MA
- Sphere Semi (spheresemi.com) — AI-optimized custom analog/RF/mixed-signal chip design and tailored fabrication. Palo Alto, CA

## 3. Precision Parts / Advanced Machining

- Hadrian (@HadrianInc / hadrian.co) — Autonomous CNC factory. AI/robotics-driven precision machining cells for aerospace/defense. Torrance, CA
- SendCutSend (@sendcutsend / sendcutsend.com) — Instant-quote online custom sheet-metal fabrication. Laser cut, bend, fast U.S. delivery. Reno, NV
- OSH Cut (@OSHCutInc / oshcut.com) — Software-defined sheet metal laser cutting and bending. Instant DFM feedback, prices in seconds. Spanish Fork, UT
- RMFG (rmfg.com) — Fast U.S. custom sheet-metal parts, weldments, assemblies. Software-defined contract mfg for hardware startups. Fort Worth, TX
- Forge Automation (@ForgeForgeForge / forgeautomation.com) — Software-enabled fast-turn CNC milling. Parts in ≤4 days, instant pricing. Toronto, ON, Canada
- Emelody (emelodyworldwide.com) — Precision 5-axis CNC in superalloys/aluminum/steels for aerospace, defense, energy, medical. Peachtree Corners, GA

## 4. Robotic Systems / Actuator / Motor Manufacturing

- HLabs (@hlabs_ / hlaboratories.com) — Building a domestic U.S. supply chain for robotics actuators and electronics. Austin, TX
- RISE Robotics (@RiseRobotics / riserobotics.com) — High-efficiency electromechanical linear actuators (Beltdraulic). Hydraulic replacement, 90% less energy. Somerville, MA
- Artimus Robotics (@ArtimusRobotics / artimusrobotics.com) — Soft electrohydraulic artificial muscles (HASEL). Fluidic, compliant actuators for robotics. Boulder, CO
- Atomic Machines (atomicmachines.com) — Micro-scale/MEMS precision manufacturing and assembly automation. Berkeley, CA
- Corvex Systems (@corvexsys / corvexsystems.com) — Domestically sourced drone motor manufacturing at scale. Arlington, VA

## 5. Forming: Mold & Die, Casting, Molding, Stamping, Forging

- Atomic Industries (@atomic_inc / atomic.industries) — AI-native rapid injection-mold design + production. Warren, MI
- Rangeview (rangeview.com) — Digital/on-demand metal casting. El Segundo, CA
- Machina Labs (@MachinaLabs_ / machinalabs.ai) — Robotic forming of sheet metal. Large-scale, flexible, no dies. Chatsworth, CA
- Foundry Lab (@FoundryLab_ / foundrylab.com) — Digital/tooling-free metal casting systems. Wellington, New Zealand
- Digital Metal (@digitalmetalinc / digitalmetal.io) — Instant-quote digital metal casting. Upload STEP, get cast aluminum/zinc parts in days. San Francisco, CA
- Aestus Industries (aestus.industries) — Tech-driven aluminum foundry. Permanent mold and sand castings, prototypes to 50k+ production runs. Loveland, CO / Durham, NC / Pawling, NY

## 6. Battery Cell / Energy Storage Manufacturing

- Ouros Energy (@Ourosenergy / ouros.energy) — Next-gen cathode materials. 10X energy density at 1/100th the cost. Miami, FL
- Forge Nano (@ForgeNano / forgenano.com) — ALD battery coatings at scale. Thornton, CO
- Form Energy (@FormEnergyInc / formenergy.com) — Iron-air long-duration grid storage. Somerville, MA
- Nascent Materials (nascentmaterials.com) — Domestic LFP cathode production. Newark, NJ
- Group1 (group1.ai) — Battery materials. Austin, TX
- Advano (@ADVANOTech / advano.io) — Silicon anode technology. New Orleans, LA

## 7. Industrial Metal Additive Manufacturing

- Freeform (@freeform_future / freeform.co) — AI-first/optimized metal additive + hybrid manufacturing. Hawthorne, CA
- Divergent (@Divergent3D / divergent3d.com) — AI-driven digital manufacturing via 3D printing + robotics for complex structures/vehicles. Torrance, CA
- Vuecason (vuecason.com) — Wire-based metal 3D printing via nozzle deposition + integrated CNC. Metal parts like printing plastic. Santa Monica, CA
- Radian Forge (radianforge.com) — Wire-arc additive manufacturing at large scale. Portsmouth, VA
- Seurat (@SeuratTech / seurat.com) — Area Printing laser metal additive for high-volume industrial production. Contract manufacturer. Wilmington, MA
- VulcanForms (@VulcanForms / vulcanforms.com) — Production-scale laser powder-bed metal 3D printing. High-volume. Devens, MA

## 8. Sensors / Optics / Photonics Manufacturing

- Lumotive (@lumotivelidar / lumotive.com) — Solid-state metasurface beam-steering LiDAR sensors. Redmond, WA
- Ouster (@ousterlidar / ouster.com) — Digital LiDAR sensors for industrial, robotics, and smart infrastructure. High-volume. San Francisco, CA
- Aeva (@aevainc / aeva.com) — FMCW 4D LiDAR-on-chip for automotive and industrial sensing. Mountain View, CA
- Voyant Photonics (@VoyantPhotonics / voyantphotonics.com) — Chip-scale solid-state FMCW LiDAR built on silicon photonics. New York, NY

## 9. Industrial Robots

- Standard Bots (@standardbots / standardbots.com) — U.S.-made AI cobots. Glen Cove, NY
- Path Robotics (@pathrobotics / path-robotics.com) — AI welding cells. Columbus, OH
- Formic (@goformic / formic.co) — Robots-as-a-Service. Chicago, IL
- Forge Robotics (forge-robotics.com) — AI welding intelligence. YC F25. San Francisco, CA
- GrayMatter Robotics (@GrayMatterRobot / graymatter-robotics.com) — AI surface finishing cells. Carson, CA
- Cohesive Robotics (cohesiverobotics.com) — AI high-mix workcells. Brooklyn, NY
- Dexterity (@DexterityRobots / dexterity.ai) — AI depalletizing and kitting. Redwood City, CA
- Ultra (@Ultraroboticsco) — General-purpose factory robots. YC-backed. New York, NY

## 10. Power Electronics / GaN-SiC Device Manufacturing

- Gallox Semiconductors (galloxsemi.com) — Gallium oxide (Ga2O3) ultra-wide-bandgap power semiconductors. Ithaca, NY
- Vertical Semiconductor (verticalsemi.com) — Vertical GaN power devices. Cambridge, MA

## 11. Industrial Chemicals and Precursors

- Solugen (@solugen / solugen.com) — Bio-manufacturing platform for commodity chemicals. Enzymes + fermentation, low-carbon. Houston, TX
- MaverickX (maverickx.com) — Advanced/innovative copper extraction technology. San Antonio, TX

## 12. Machine Tool Manufacturing

- OpenX (@TryOpenX / tryopenx.com) — Mobile prototyping cell in a shipping container. On-demand machine shop, anywhere. Long Beach, CA

## Ecosystem Enablers

- Dirac (diracinc.com) — AI-driven model-based manufacturing platform. Making factories dynamic and adaptive at scale, starting with automating work instructions. New York, NY
- First Resonance (@FirstResonance / firstresonance.io) — Digital-thread MES with full traceability. Los Angeles, CA
- Diode Computers (@diodeinc / diode.com) — AI agents + code-based schematics for rapid custom PCB design and fab. Days vs. months. Brooklyn, NY
- Quilter (@quilterai / quilter.ai) — Physics-driven AI for fully autonomous PCB placement/routing/layout with EM and thermal validation. Los Angeles, CA
- Flux (@BuildWithFlux / flux.ai) — Browser-based AI agent eCAD platform. Natural-language PCB/hardware design workflows. San Francisco, CA
- JITX (@JITXsoftware / jitx.com) — Code-first (Python) platform for requirements-to-optimized PCB designs + AI assistance. Berkeley, CA
- Lambda Function (@lambdafnAI / lambdafn.ai) — ML/AI-assisted CNC programming. Strategy, tool, parameter, and toolpath recommendations from shop data. San Francisco, CA
- Krevera (krevera.com) — AI for real-time closed-loop control and optimization of injection molding. Boston, MA
- Photonium (@Photonium / photonium.com) — AI tools for optics/photonics design and EDA. Palo Alto, CA
- Mbodi AI (@mbodiai / mbodi.ai) — Natural-language robot teaching. New York, NY
- Matter (makematter.co) — AI-powered contract manufacturing marketplace/platform. San Francisco, CA
- Drafter (drafterinc.com) — AI tools for manufacturing engineering. Austin, TX

## Sources

- Reshoring as 2026 Investment Theme
- Six Months In: Tariffs and Manufacturing
- Anduril $30.5B Valuation (CNBC)
- Anduril Revenue Estimates (Sacra)
- Hadrian $1.6B Valuation (Robot Report)
- Hadrian $260M Series C (CNBC)
- Varda $500M Valuation (Caproasia)
- Industrial EBITDA Multiples 14.7x (Clearly Acquired)
- EBITDA Multiples by Industry (Equidam)
- Wright's Law (ARK Invest)
- Deep Tech Exit Rates vs SaaS
- Defense Tech $49.1B in 2025 (Defense News)
- DoD Acquisition Reform / WAS (WilmerHale)
- FY2026 NDAA Nontraditional Contractor Reforms (Crowell)
- Dual-Use Technologies 2025 Report (Mind the Bridge)
- Dual-Use Market Premium (CEPR)
- Palantir Revenue Split (36kr)
- SpaceX Government Contracts (Built In)
- CHIPS Act Advanced Packaging $1.4B (NIST)
- Amkor $7B Arizona Campus
- 98% Advanced Packaging Offshore (Georgetown CSET)
- PCB Reshoring and Tariffs (MacroFab)
- Battery Startups $19.9B in 2024 (Crunchbase)
- Northvolt Bankruptcy (Wikipedia)
- China Battery Export Controls (Forge Nano)
- Robotics $10.3B in 2025 (Crunchbase)
- Shenzhen Ecosystem (Diamandis)
- Shenzhen Supplier Density (itimanufacturing)
- Defense Tech VC Trends Q4 2025 (PitchBook)
- Scaling Nontraditional Defense Innovation (DIB)
- Oliver Hsu, "A Primer on Factory Economics for Startups" (a16z, 2026)
---
layout: post
title: "Isthmus Carshare, sharing a car with the whole block"
description: "The story of founding a cooperative carshare, and why collective ownership is so hard to sell"
type: project
tags:
- urban planning
- sustainability
- politics
image: /assets/images/2026/carshare/flyer.png
---

For about two years, a big chunk of my free time went into trying to start a cooperative carshare in my neighborhood in Madison, Wisconsin. It was called [Isthmus Carshare](https://isthmuscarshare.github.io/isthmuscarshare/), and it got a lot further than most of my ideas do. We incorporated a real co-op, adopted bylaws, elected a board, got a grant to pay a lawyer, built a reservation website, and bought a smart lockbox for the keys. And then, before we ever got a car on the road, I had to shut it down.

I want to write down how it went, partly so the work doesn't just disappear, and partly because I think the idea is still really good. If I ever end up back in Madison, I'll start it up again in a heartbeat.

### The idea

My partner and I went fully car-free in 2021 (I was mostly car-free since 2010), and since then I've used Zipcar and other carshares when I really needed a car. They work, sort of. But the cars are never quite where you are. In Madison, Zipcar basically only exists downtown and around campus, so if you live a mile or two out, "carshare" means a bus ride to go pick up your car. Which kind of defeats the purpose.

So my idea was pretty simple. What if everybody on a city block just shared their cars?

Think about a typical block in a neighborhood like [Tenney-Lapham](https://www.cityofmadison.com/dpced/planning/documents/plans-projects/neighborhood-plans/TenneyLaphamPlan.pdf). There are maybe a dozen or more households, most of them with one or two cars. The average car owner spends something like $10,000 a year on their car, and that car sits parked [about 95% of the time](https://www.reinventingparking.org/2013/02/cars-are-parked-95-of-time-lets-check.html). If even half of those households pooled their cars into a co-op, with shared ownership, shared insurance, and some lightweight tech to reserve them, you'd have something better than Zipcar could ever give you: a handful of cars within a two-minute walk of your front door, almost always available.

And the economics get better the more cars you convert:

1. **You don't need all the cars.** If ten households pool ten cars, the actual demand can probably be met by only five to seven cars. You sell the rest, and that money goes back to the members as a payback for joining.
2. **Fewer cars means less depreciation.** Depreciation is the hidden monster of car ownership. Once you're owning a third fewer cars, the fixed cost per household drops a lot, enough to cover the overhead of insurance, the booking software, and the lockbox.
3. **Maintenance becomes a job, not a chore.** Instead of every household separately dealing with oil changes and tire rotations, one member can take the cars in and get paid in free driving credits.

So the operating budget per household should actually come out *lower* than owning your own car, even after you pay for all the coordination. It's better for the climate too. One Dutch study we cited found that car sharers emit 8 to 13% less CO2 per person per year, about half from driving less and half from owning fewer cars. Nothing about this requires a technological breakthrough. It's just a coordination problem, plus some boring legal paperwork.

### Climatebase and Down the Block Carshare

I first pitched the idea in the fall of 2023 as part of the [Climatebase Fellowship](https://climatebase.org/fellowship), under the name "Down the Block Carshare." I already wrote [a post about that part](/2024/02/climatebase-carshare/), but the short version is that two other fellows, [Chad Bustard](https://www.linkedin.com/in/chad-bustard-phd-20628090) and Carsten Röskes, jumped on board, and we spent the fellowship vetting the idea. Chad and Carsten built geospatial and financial models to figure out where in Madison a carshare would make sense, while I went out and did interviews.

We ended up talking to or surveying over 75 people. In Tenney-Lapham alone, 43 people answered the survey, 38 said they would consider carshare, 19 gave us their email, and 11 said they would actually consider selling their car to the co-op. For a neighborhood pilot that only needed three or four cars, that seemed like plenty. When we asked people what they liked least about owning a car, the answers were pretty consistent: cost, maintenance, parking, and a surprising amount of guilt.

<img class="small_img" title="Carshare Survey wordcloud" src="/assets/images/2024/carshare_survey.png" alt="A word cloud of survey answers about what people like least about owning a car, with words like maintenance, guilt, climate.">

We packaged all of that into a "scrolly-telling" page called [Why Carshare?](https://isthmuscarshare.github.io/whycarshare/), which walks through the cost of owning a car versus Zipcar versus a local co-op. The punchline of the main chart is that owning a new car adds up to nearly $70k over ten years, and the co-op comes in way under both. Our pitch line was that the carshare offers "all the convenience of a car, with none of the cost, maintenance, parking or environmental guilt." It also has a map of where we wanted to roll out compared to where Zipcar actually is, which made the gap pretty obvious.

The pricing we landed on was $2/hour plus $0.45/mile, with a $19/month membership and an optional refundable buy-in. For someone driving 250 miles a month in a dozen two-hour trips, that came out to about $175, versus roughly $266 to own a 2016 Corolla according to the USDOT cost calculator, and it was around half the price of Zipcar for a typical trip around town. Chad built a [trip planner](https://isthmuscarshare.github.io/isthmuscarshare/trip_planner/trip_planner.html) where you can type in a destination and see the cost side by side, which is still fun to play with.

<img class="small_img" title="Trip cost comparison" src="/assets/images/2024/carshare_demo.png" alt="A trip cost comparison tool showing the price of a trip with Zipcar versus Isthmus Carshare.">

I even tried to bootstrap some funding sideways. When I made my [CITY MOTION board game](/2024/10/city-motion-game/), the plan was that any surplus from sales would go toward kickstarting the carshare.

### Making it real

After the fellowship ended, the project kept going, which is honestly a first for me. In January 2024 we put together a steering committee, and that's where it went from being a fellowship project to being a neighborhood project.

The people who joined made all the difference. Janet Murphy had already been running a carshare at [Arboretum Cohousing](https://www.arboretumcohousing.org/) for years, sharing three cars between about 15 neighbors, and she manages an [international group of cohousing carshares](https://lists.cohousing.org/archives/cohousing-l/msg50193.html). She was basically living proof that the idea worked. Will Ochowicz, who I knew through the Tenney-Lapham neighborhood association and who also helps lead [Madison is for People](https://www.madisonisforpeople.org/), signed on as treasurer and started writing code for the website. Chad stayed on as secretary and "source of ground truth," and Ethan Budreau joined as program manager.

Over the spring and summer of 2024 we did a whole lot of grown-up business stuff:

- We decided to be a **cooperative** rather than a 501(c)(3), because a nonprofit can't give a car back to the person who donated it, and we wanted members to be able to leave and take their car (or the rest of its value) with them.
- We incorporated as the **Isthmus Carshare Cooperative** in May 2024 under Wisconsin's Chapter 185 co-op law.
- We got a grant from the **Wisconsin Economic Development Corporation** to cover legal work, and hired Small Axe Cooperative, a worker co-op law firm, to review our articles and bylaws and help draft our contracts.
- We wrote a **membership agreement** and a **car sale contract with loan terms**, which was the core legal trick of the whole thing. Instead of the co-op buying your car outright, you'd sell it to the co-op on a loan, which waived your membership buy-in, and the co-op would pay you back over time or return the car if you left.
- We lined up a parking spot in a neighborhood lot for $50 a month, and a neighbor even offered to put their car in on loan.

On July 25th, 2024, we held our inaugural board meeting. We unanimously adopted the bylaws, elected the first board, and approved a $12,000 startup loan from me to the co-op so we could buy the first few cars. It felt like the real start of something.

<img class="small_img" title="Isthmus Carshare flyer" src="/assets/images/2026/carshare/flyer.png" alt="A flyer titled 'Why Isthmus Carshare is the right choice!' showing pricing of $2/hour, $0.45/mile, $19/month, a map of planned pickup locations in Tenney-Lapham, and a timeline for a summer 2024 pilot launch.">

### The tech

The tech was very deliberately "lightweight." We didn't want to build an app startup, we wanted to share some cars.

Chad built the [first version of the website](https://isthmuscarshare.github.io/isthmuscarshare/) in the spring of 2024 (the [code is on GitHub](https://github.com/isthmuscarshare/isthmuscarshare)), including the trip planner. I refactored it into Jekyll (because of course I did), and Will O added logins. The homepage still shows "our cars," a Honda Civic, a Prius, and a Subaru Forester, with the honest little disclaimer "(We don't own these yet, but these are the types of cars we plan to buy)." The actual reservation system was a [form](https://isthmuscarshare.github.io/isthmuscarshare/new_reservation.html) backed by a shared [Google Calendar](https://isthmuscarshare.github.io/isthmuscarshare/calendar.html). When you booked a car, an Apps Script checked the calendar for conflicts and emailed you a code for an [Igloohome smart lockbox](https://www.igloohome.co/) attached to the car. When you brought it back, you filled out a [return form](https://isthmuscarshare.github.io/isthmuscarshare/return_car.html) with your mileage and got another code to put the keys back.

It wasn't fancy, but it worked, and the whole thing cost about $120 for the lockbox plus a domain name. That's kind of the point. Carshare doesn't need a billion-dollar platform. It needs a calendar and a box for the keys.

### Where it stalled, and then stopped

The note from that first board meeting that I keep coming back to is this one, verbatim:

> We have no actual car signups 🙁

We had interest. We had a lot of interest. But turning "I'd consider it" into "here are the keys to my car" was much harder than any of the survey numbers suggested. There's a chicken-and-egg problem built in, where people don't want to sign up until there are cars, and you can't get cars without people signing up. We had a plan to break through it, with flyering, tabling at events, a membership drive in the fall, and buying the first car ourselves with the startup loan.

But around that time, my partner and I started talking seriously about moving back to California. Once that was decided, there wasn't really a way to keep going. I was the one pushing most of the pieces forward, and a neighborhood carshare kind of needs its founder to live in the neighborhood. We wound things down and kept the leadership in place through the end of 2025 to close things out properly. The website is still up as an archive on GitHub Pages, minus the custom domain.

I don't regret any of it. I'm proud of how far we got, and I'm really grateful to Janet, Will O, Chad, Ethan, and Carsten for putting so much of their own time into it. And all the founding documents still exist, along with the [FAQ](https://isthmuscarshare.github.io/isthmuscarshare/FAQ.html) explaining how the whole thing was supposed to work. Somebody could pick them up and start a co-op carshare in their neighborhood tomorrow (if that's you, please reach out).

---

## Why is this so hard?

I've been thinking a lot about why something that is so clearly good for the people involved is so hard to get off the ground. And it really comes down to just a couple core problems:

### Nobody knows what their car costs

When I did the one-on-one interviews, I would walk people through the actual cost of owning their car: depreciation, insurance, registration, maintenance, gas, parking. Every single person underestimated their cost per mile. Not by a little, but often by half or more. People think of the cost of a car as gas money, because gas is the only part you pay every time you drive. Everything else is paid in big lumps, or never shows up as a bill at all, like depreciation, and so it just kind of vanishes from people's mental accounting. Somehow everyone thinks of their car purchase like an investment, even though it is mostly a money pit.

One interview really stuck with me. A younger guy who used his car *extremely* rarely (exactly the person a carshare is designed for). Because he barely drove, all those fixed costs got spread over very few miles, so his real cost per mile was enormous. We went through the whole calculation together, and the carshare would have cost him roughly half as much per mile as his own car.

But when I told him the carshare's price per mile, he said that was too expensive and he wouldn't do it. Even though his own car was already costing him about twice that. Even though it was cheaper. Even though we had just laid it all out 5 minutes prior.

I don't think he was being dumb (well maybe a little). I think he was being normal. The cost of his own car was invisible, and the cost of the carshare was a number on a screen every time he drove. Owning a thing feels free once you've paid for it, and sharing a thing feels like a fee.

### Collective goods only ever look like costs

I think that interview is a pretty good little model of how a lot of Americans think about collective ownership in general. We've been trained to see anything shared as a cost, something you pay into and lose, rather than something you own a piece of. Taxes are a cost. Public transit is a cost. A co-op membership is a cost. Meanwhile the car in the driveway, slowly losing thousands of dollars a year, feels like an asset.

But the whole logic of collective ownership is that it's how normal people get access to things they couldn't afford alone, or could only afford wastefully. I've [written before](/2022/12/radical-entrepreneurialism/) about how worker co-ops are really just a radical version of entrepreneurship, where everyone gets to be an owner. A carshare co-op is the same idea applied to consumption. You aren't paying a fee to use someone else's car. You own a fraction of four cars instead of all of one.

### The car is also a closet

There's one hurdle I understand a lot better now that I have a baby. A car isn't just a way to get around, it's also a place where your stuff lives. The stroller, the diaper bag, the emergency snacks, and most importantly the car seat. Anyone who has wrestled a car seat in and out of a back seat knows it's not a thirty-second job, and if you had to do it every time you borrowed a car, you'd start to hate carsharing pretty fast.

We actually did think about this. One idea was to let families keep major items like a car seat in one dedicated car. That makes that car a little less fungible for everybody else, since you'd have to work around a car seat if you borrowed it, but it seemed like a reasonable tradeoff. A co-op can make that kind of exception because the members get to decide what's fair.

The trouble is that it runs right into another problem, which is liability. No fleet insurance program we found had a box to check for "this car has a car seat installed in it that is owned and maintained by Family X." If something goes wrong, who's responsible? The co-op? The family? The insurance company? The member who was driving? It was uncharted territory, and in a country as litigious as the US, uncharted territory is scary. Every time we walked through the logistics in detail with some of the more cautious folks, that was often the point where they started to balk. Not because the idea was bad, but because nobody could promise them it would be fine if something went wrong.

A lot of what makes private car ownership feel easy is that all of those questions are already answered for you, by default, by a giant system of insurance and law designed around one family owning one car. Sharing means answering them yourself, and most people would rather not.

### You can't VC your way to non-extraction

A lot of the advice we got, both during the fellowship and after, was really about how to scale. And I get it, that's how startups are supposed to work. But a cooperative carshare is intentionally non-extractive. The whole point is that the savings go back to the members instead of to investors. There's no 10x return hiding in there, because the "profit" is just people paying less for transportation.

That means it can't be scaled the way the startup world scales things. Zipcar is owned by Avis Budget Group, and it has to make money for Avis. A neighborhood co-op only has to make the cars available and pay the insurance. Those are fundamentally different businesses, even though they kind of feel the same to the person using the car. The way something like this grows isn't by raising a Series A, it's by one neighborhood copying another neighborhood's bylaws. Which is slower, but it's also how Janet's cohousing carshare network ended up spanning five countries.

### The people who get it are often the people who can't organize it

Here's the somber part. A lot of the people I talked to who were most enthusiastically on board were folks who were intrinsically anti-establishment. They loved the idea of a co-op, they hated car companies, and they were totally down to share. But many of them (with the notable exception of Janet Murphy) were also, frankly, pretty disorganized. Showing up to meetings, signing contracts, keeping a car clean and returning it on time, those things matter a lot when you're sharing something with your neighbors.

Meanwhile the people who were organized and business-like mostly wanted the kind of business they already understood, where somebody makes money. It's really hard to find people who are both organized enough to run something like a business and also don't want it to be extractive. I'll admit I'm not as organized as I wish I was either. A lot of this project was me remembering at 11pm that I'd promised to send someone a draft. But honestly, part of the reason that everyone seems disorganized is because they are all doing this at 11 pm after a hard day working for an extractive business elsewhere.

### Still hopeful

I don't think this is a dead end. The fact that we got as far as we did, with a handful of volunteers and a $120 lockbox, says a lot. Janet's carshare has been quietly working for years. Co-op carshares like [Modo](https://www.modo.coop/) in Vancouver have been running for decades with thousands of members. The idea works when it gets a foothold.

What I think needs to happen is for this to move out of the counterculture and into the boring middle class. Not as a protest, but as the obvious financially sensible thing to do, the same way credit unions are just a normal place to get a car loan now. If enough regular households on a regular block figure out that they're spending thousands of dollars a year on a car that mostly sits in the driveway, and that their neighbors are doing the same, then maybe sharing will stop feeling like a cost and start feeling like what it is: owning more, together, for less.

And if we ever move back to Madison, I'll be knocking on doors again.

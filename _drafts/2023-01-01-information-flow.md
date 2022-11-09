---
layout: post
title: "Information flow and social structure"
subtitle: "the Hierarchical to Egalitarian Phase Transition"
author: "Will Stedden"
category: commentary
---
<br/>

I know social media has a bad reputation and is generally regarded as something that's on the verge of destroying the world. But at the same time, it might just be the one thing that gives me hope that a society-wide change is possible in my lifetime. I was listening to @hydroponictrash being interviewed on the Solarpunk Now podcast, and they were discussing why the sixties counterculture and the internet failed to transition the US away from late stage capitalism and toward a healthy, well-functioning society?

Most of the egalitarian, anarchist, socialist, progressive ideas have been practiced for decades now, but they were often misunderstood in their time and failed to spread.  My thesis is that easily publishable social media was the key missing ingredient in spreading and solidifying the ideas needed for an egalitarian world.  And my theory for how all this works is something I'm calling the Hierarchical to Egalitarian Information Phase Transition.


### What is the Hierarchical to Egalitarian Information Phase Transition?

There's this idea[^2] that one of the pillars of oppressive hierarchies is the control of information, meaning that information hierarchies are one of the principle means by which any other oppression is maintained. My theory takes that principle as a starting point, but adds that such control of information isn't intentionally constructed by a society, but instead, is just an organic outgrowth of the technologies that exist at a given time and place[^3].

In other words, my theory is that hierarchical systems evolve due to technology that enables centralized information flow to be much more economical than decentralized information flow.  My theory is that when available technology changes so that peer-to-peer communication becomes a more economical mechanism than hierarchical systems for information propogation, we will begin to experience a phase transition from predominantly hierarchical systems to predominantly egalitarian ones.  This is because equality inducing information propagates better through such a system than hierarchy inducing information, and, therefore, the greater abundance of equality inducing information in our society will propel people into supporting equality.

#### Examples

At one extreme this becomes obvious.  The first "technology" that humans developed was essentially the ability to communicate complex thoughts about each other's actions to one another. This essentially enables gossip, and with gossip as the predominant technology in a small tribe, it's much harder to assert hierarchical control of information.  Without controlling information it's hard to enslave, hoard resources, or enact violence, and get away with it.

But as you get agriculture and larger interconnected urban centers, the technology that was developed was smaller networks and councils that could act as information bottlenecks.  That made it much more economical to pass information through those networks, but that allows information assymetries that naturally establish hierarchies.

And there's been a tug-of-war between centralized and decentralized communication technology ever since, with centralized always maintaining a slight economic advantage.  As kings wrote laws and built networks of enforcement, most of the communication of information was pretty centralized around a small group of people acting as communication nodes. When personal letters (and later the telephone) became accessible to most people, this allowed much easier peer-to-peer communciation, but this was shortly followed by larger centralized media sources (radio, TV) so the balance never crossed the threshold. So from Hamurabi to colonialism to Rupert Murdoch, our most efficient communication has relied on a central hierarchical system.  And at this point, it's been heavily locked into our current corporate, governmental, and even academic structures.  Even the early internet worked in this way, as the ability to spread messages quickly had bottlenecks like search engine indexing and the small number of highly paid professionals who could optimize search results.

#### Interlude

Now imagine, as a layman, I wanted to share this very idea in the 1990s. I could try to give a talk on it, which would be seen by 10-50 people.  That would entail applying to established venues or flyering around town for my own.  I could be part of a club, but that takes a lot of effort to keep organized as well. If I wanted even 100s of people to read it, I'd probably have to write a whole book, get a press to print it, and maybe go on tour to promote it.  The cost would be so high, I'd basically have to build a career around it. Of course, with so much at stake, I'm only willing to even discuss ideas that offer me some value in return. It's a lot of effort to reach only a few people, and even more effort to reach a lot of people.  But there are economies of scale for people already connected to the dominant hierarchical system.

Now contrast this with social media. I only have to invest a few hours clarifying my idea, and then I can get it out to at least 10 people.  And with certain types of media, like TikTok, the idea could be seen by hundreds of people.  Now I'm just one voice in many so the payoff is smaller, but the cost is so low it doesn't matter too much. The economics of my small independent idea or little piece of information has materially shifted. And what's really amazing is that the cost is that low for my audience too so they can give their take on the idea too.  That means that we can efficiently spread whatever information we want collectively even if we aren't super invested or talented.  In that information economy, every person is exposed to many ideas that offer modest rewards to a bunch of regular people rather than ideas that offer huge rewards to a select few.  Ultimately, I believe this new information landscape will shift attitudes to accepting a more egalitarian society.

And this is the point that I'm calling the Hierarchical to Egalitarian Information Phase Transition.

### A model of information flow

While the above gives a decent intuition about what I'm trying to say, I thought it would be helpful to make the idea a lot more explicit. I'm wanting to come up with a simple model of information flow that will show me where exactly this phase transition occurs based on the simplest formulation of some assumptions I have about humanity.

Particularly, what I'm assuming above is that:


1. Most people have a bias to accept ideas that they hear repeated more often.
2. People repeat ideas that they've come to accept.
3. At least some people are capable of discerning ideas that are good for them if they are exposed to them. (eg, people in hierarchical positions would think ideas that promote hierarchy are better, and regular people would think that eqalitarian ideas are better)
4. People get most of their ideas from the information system that they are embedded in.

While I feel like understanding this on an intuitive level is pretty simple, it isn't entirely clear when we'll reach this new state or why it didn't happen when the internet came online.  We still have a mixture of "mainstream" hierarchical information systems, and a "distributed" peer-to-peer information flow.  I was very interested in seeing if there are any _phase transitions_, where our information system would flip from supporting the status quo to supporting new egalitarian ideas.

Towards this end, I tried develping a simple simulation of the spread of information under various assumptions.

The rest of this post is going to weave mathematical simulations with philosophical ideas.  I'm going to do my best to limit the details of the simulation to just the important details, but for those who are interested in this type of analysis and want to see the nitty-gritty, I've also written a more hands-on blog post as well as a paper describing the methods and results with a bit more rigor.



#### Encoding assumptions in math

The key to building mathematical models is finding ways to encapsulate your assumptions into specific formula.  There are many ways to do this, but I'll be using a method called cellular automata.  This is the basic setup of the classic "Game of Life," where cells have specific state and then other connected cells change state in response.  In this simulation cells will represent people and their state will represent the beliefs held by those people.
I'll write specific rules by which one cell can update another, basically simulating an idea being passed on.  There will be parameters that determine how likely an idea is to be accepted based on how often they hear it and how useful it is.  To keep things simple in the beginning, I'll focus on just two ideas: one hierarchical and the other egalitarian.

The core difference between models will be the degree of interconnectivity between cells in the simulation.  In other words, in the hierarchical models, cells will mostly communicate through central corridors, while in the egalitarian models there will be much more cross connectivity.

I'm going to be interested in which conditions cause the system to stick with the hierarchical idea and which conditions allow the system to switch to the egalitarian idea.  I'll be paying attention to all these encoded parameters:

1. degree of interconnectivity between cells
2. likelihood of accepting an idea from peer pressure
3. likelihood of accepting an idea from its usefulness to you

To see exactly how those parameters are inserted into the equations you can check out my technical blog here or read the short paper I wrote on the subject.


### Results

### The phase transition

A phase transition is when a system moves between two qualitatively different states.  A typical example is the phase transition of water between the liquid form and ice.  When the temprature of the water crosses a critical threshold, the molecules switch from being tightly packed to loosely associated and flow past each other.

In this model I was most interested in where a transition would occur between a network that was filled with hierarchical ideas to one filled with egalitarian ideas.






### Takeaway

The basic finding is that if everybody can repeat the ideas that resonate with them, then egalitarian ideas will be able to take over.  What does this mean?  It means that the failure of the internet thus far is NOT due to the uneducated philistines being given the ability to post their thoughts.  The issue with the internet is that it can be co-opted by money and algorithms.

The takeaway is this, if the internet can ever become a force for good, then it will happen when everybody has roughly equal ability to share information on it.  This has interesting implications for what the internet should look like in the future.




### wadabout "web3"

I'm going to be straight here, I think web3 (in it's recent crypto iteration) violates an equality principle in some of the most violent ways possible.  Lets be clear. Web3 is a mechanism for paying for the existence of new web services through issuing securities with the intent of selling to users so they can resell later.

I understand the appeal: early adopters are financing startups, and then early adopters get paid back later.  It certainly sounds better than venture capitalists funding startups and then forcing startups to monetize their users later to generate profits forever.

But both of these systems are flawed in light of my analysis above.  The flaw in both cases is using money as an arbiter of who gets to have a say.  And whether you do it by giving preference to whoever drives more ad revenue or whoever ponies up for more "tokens," the system is going to give preference to dollars in the end.

The simplest way to get equity of speech is to transfer our systems of common communication to common ownership.

In my humble opinion, once the "trustless" crypto hype market fails again, we're going to start seeing people recognize the flaws of building a whole new tech stack again, this time integrated with money.  By building a new and more complicated version of the web, we're making it less democratic (yet again), and continuing to concentrate power inthe hands a tiny sliver of the technically capable population. I believe this is intentional--to keep it hard to build something new.

The truth is we need trust.  We need a commonly owned open-source forum where there are well-understood limitations to the power of small groups.  I suspect that will be what web3 actually becomes.


[^2]: Dawn of Everything

[^3]: More specifically, my theory is that egalitarian and hierarchical trends constantly coexist in any society, with subsets of people favoring one over the other. The dominant trend is not set by any intentional decision, but instead, whichever technology is most economical is the one that wins out.
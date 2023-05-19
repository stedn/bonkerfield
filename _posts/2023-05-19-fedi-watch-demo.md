---
layout: post
title: 'FEDI-WATCH demo'
date: '2023-05-19'
author: will stedden
type: project
description: 'running decentralized detoxify monitoring for Mastodon'
tags:
- web
- code
- data science
top:
image: /assets/images/2023/fediwatch_2.png
---

A few months back I worked on a very lightweight prototype for a decentralized moderation app for the fediverse.  I stalled out on the project when I couldn't find collaborators who wanted to actually volunteer for moderation, but I had built a fairly interesting set of infrastructure to work on it.

# The Problem

After the recent migration from Twitter to [Mastodon](https://joinmastodon.org/), with more people of color migrating to that platform there were [proven difficult](https://www.fastcompany.com/90817452/can-mastodon-be-a-twitter-refuge-for-marginalized-groups).  Online harassment, spam and other generally harmful interactions have weren't being dealt with properly. On the one hand, the issues on Mastodon have been described as reflecting general issues of its [inherent whiteness](https://techpolicy.press/the-whiteness-of-mastodon/) and not necessarily a technical problem.  On the other hand the specific nature of a decentralized service without a single accountable moderation team does present [unique technology challenges](https://www.webpurify.com/blog/moderating-mastodon-and-the-fediverse/) to that community that need to be overcome hand-in-hand with the work of [dismantling internalized white supremacy](https://www.npr.org/2020/07/06/887646740/me-and-white-supremacy-helps-you-do-the-work-of-dismantling-racism).

The nature of Mastodon (and the [fediverse](https://www.lawfareblog.com/what-earth-fediverse) in general) is that it is [decentralized](https://www.theregister.com/2023/01/01/mastodon_activitypub/), which means that it isn't just one monolithic website but actually entails a bunch of smaller web communities all speaking a common language so that content can be shared between them. This offers benefits and downsides. One downside is that some people can join "Mastodon," but end up on specific servers where moderation is non-existent.  Because there isn't a centralized reporting system to help those people, they can end up having a really harmful experience.

There have been [other](https://www.fedi.watch/) [initiatives](https://joinfediverse.wiki/FediBlock) to start tackling this problem, and I'm honestly not sure whether there needed to be another approach.  But along with [umm-maybe](https://github.com/umm-maybe), another AI interested mastodon user, I contemplated a specific solution that could scale out moderation to more people than just the local administration of one server.

## Citizen Moderators

One idea that I've explored in [my writing previously](/2022/07/algorithmologists/) is that the information landscape could be moderator by a jury of impartial observers.  While we're a long way off from a well-managed citizen's assembly for disinformation and content moderation, I thought it would be interesting to explore this subject area beyond my hypothetical fictional musings and put it into a practical application.

Specifically, I wanted to employ a user-centric approach that could allow a group of moderators to intervene and report toxic content as well as offer help moving instances or just generally supporting those who are being harassed online.  While this is possible with net-citizens just focusing,

To make this form of moderation work in practice, Mastodon users sign up to allow us to perform API access on their behalf to their local server.  We then employ automated scripts to scout their local timelines and replies. We then pass that content through automated filters to search for offensive posts, and create a large centralized list of aggressive and caustic comments.  With that information we can then send moderators out to specific Mastodon servers help anyone who is being targeted for harassment.

It's a different approach, and one that I hadn't seen mentioned anywhere else. I had trouble getting any feedback, positive or negative, about the idea, but I decided I'd try to flesh out a prototype to help others think through the concept.

# How It Works

The general architecture of the decentralized moderation is that moderators login with their credentials to their own personal servers, which then allows for open polling of their server's community feed.

<figure>
  <img alt="login screen for fediwatch" src="/assets/images/2023/fediwatch_1.png" />
</figure>

After picking up the community feed, I then poll each post for a period of time to watch if any replies are posted.  From that point, all of the replies are monitored in a centralized queue and they are prioritized for review using the detoxify algorithm for detecting offensive and toxic content.

<figure>
  <img alt="Fediwatch reply cue showing results of detoxify algorithm" src="/assets/images/2023/fediwatch_2.png" />
</figure>


I built all of this on Google App Engine predominantly because I already had experience with the Mastodon OAuth flow from working with my friend [Ryan](https://snarfed.org/) on the [Bridgy](https://brid.gy/) open source project, which made it easier to get started. The UI is rudimentary at this point and really just spits out a long list of all the results that I'm picking up, along with their results from detoxify.  In a future release I could imagine sprucing up the UI somewhat, but it wasn't as important as getting the algorithm running on the backend so I focused on that.

The most interesting part of the project was getting UnitaryAI's [detoxify](https://github.com/unitaryai/detoxify) up and running.  I hadn't used it before, but it was a very easy package to get in place.  Under the hood, I believe it's just a BERT classifier trained on a dataset of toxic content.  The output is just a probability score for each of the following classes:

- toxicity
- severe_toxicity
- obscene
- identity_attack
- insult
- threat
- sexual_explicit

You can view the [detoxify repo](https://github.com/unitaryai/detoxify) for more information.

For ops, I originally, used App Engine's cron feature to call an endpoint that would load and run detoxify on the most recent batch and then do cleanup on old messages.  However, that turned out to be really really expensive so to reduce cost I rearchitected it with a cheap standalone Cloud Compute instance that would just continually run a script to process batches with a stored model.  Even with no usage this still costs me about $0.50/month, but that isn't too much of an issue at the moment.

As usual, all my code is [up on github](https://github.com/stedn/fedi-watch) in case someone else finds that they'd want to use this as a starting point for their own similar project.


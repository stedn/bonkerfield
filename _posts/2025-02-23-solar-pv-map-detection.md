---
layout: post
title: "Detecting Solar Panels from Satellite Imagery"
description: "Building a Real-Time Feedback Tool for PV Mapping"
type: project
tags:
- data science
- analysis
- sustainability
- energy
- computer vision
image: /assets/images/2025/solarscan_app1.png
---

After moving back to California last month I have been very excited to see the massive quantity of solar PV rooftop installations in the areas I've visited.  California is the [largest producer of solar power](https://www.axios.com/local/san-diego/2024/04/12/california-solar-power-leader-how-much) in the US, and last year even went [100 straight days](https://calmatters.org/environment/climate-change/2024/08/california-clean-power-progress-grid/) where renewables satisfied 100% of demand for at least part of the day.  As you can see in this graph from 2024, during the daylight hours a huge chunk of our power comes from solar, with wind and hydro staying more consistent throughout the day.

<img class="small_img" title="Electric Generation Sources in California 2024" src="/assets/images/2025/electric_generation_ca.png" alt="graph showing breakdown of energy sources throughout the day with a large yellow patch in the middle for solar when other forms are being shut off">

In fact, you might notice that there is even a negative hump below the graph, which is extra energy from the surplus of solar that goes into battery storage.  That stored energy is then used a little later in the day after the sun sets to extend the use of solar even after the sun is gone.

I've been interested in the idea of small-scall storage to take in that solar closer to the homes that generate it since that's more efficient and would allow us to have more isolated battery systems, hopefully mitigating the risk of huge [battery fires](https://www.npr.org/2025/01/17/g-s1-43268/fire-battery-storage-plant-california-moss-landing).  To do that, I was interested in seeing if I could measure the density of rooftop solar installations and correlate that with other features to find good opportunities for [small battery](https://www.poshenergy.com/product-station) or even my dream of [small pumped-hydro](https://www.renewableenergyworld.com/energy-storage/pumped-storage/small-pumped-storage-at-core-of-neighborhood-project-combining-solar-wind-battery/) storage systems.  I figured it would be cool to build this dataset and put it online as a tool to demonstrate locations where such projects might be feasible.

### Challenges in Solar Panel Detection

Detecting solar photovoltaic (PV) panels from satellite imagery for better understanding solar energy adoption is an active area of research, and a [whole](https://www.tandfonline.com/doi/full/10.1080/15481603.2022.2036056) [bunch](https://cs231n.stanford.edu/2024/papers/solar-panel-detection-on-satellite-images-from-faster-r-cnn-to-y.pdf) of [people](https://www.sciencedirect.com/science/article/pii/S0306261924006251) have [explored](https://github.com/A-Stangeland/SolarDetection) this problem for many [years](https://alexhalcomb.github.io/).

However, I didn't find many projects that were sharing models that worked well, and I wasn't that interested in training yet another one. Eventually I stumbled on one particularly valuable resource: the [BDAPPV dataset](https://zenodo.org/records/7476598) and associated [pretrained models](https://zenodo.org/records/14673918) collected and developed by [Gabriel Kasmi](https://gabrielkasmi.github.io/) at Mines Paris. It was a collection of [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) models all in one place that were publicly available for use by others and seemed to work pretty well.  I started working with these models, but as the researchers highlighted in [this paper](https://arxiv.org/pdf/2309.12214), each of these models has its limitations, and no single model excels in every scenario.

I wanted to combine these individual models into a more robust solution, but I needed **calibration/validation data** that closely aligned with the way I planned to use these models in real-world applications. Specifically, I wanted to deploy them over larger areas by querying Google Maps imagery. Since I would be working with Google Maps extracts, I also wanted a smooth way to view and label the data.

To achieve this, I built an [online tool](https://solarscan.appspot.com) that would help me pass data to the models, grade their performance, and integrate all the models into a [stacked model](https://medium.com/@brijesh_soni/stacking-to-improve-model-performance-a-comprehensive-guide-on-ensemble-learning-in-python-9ed53c93ce28) that would combine the prediction probabilities from each individual CNN model to improve the overall accuracy.

## Features

There are two standout aspects of the app that I find particularly compelling:

#### 1. Interactive Real-Time Detection

By integrating the Google Maps API, the app allows users to interact with a map and click on locations to detect solar panels in real-time. The app then sends an image from Google Maps to the backend, where it interacts with the models deployed on GCP to predict whether solar panels are present at that location. This makes the app highly scalable, as users can explore large areas and continuously add to the dataset. I also included some cool usability features like centering the map on the user's approximate location at startup using [ipinfo.io](https://ipinfo.io) and allowing search with the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview).

<img title="Zoomed out view of many detections in a neighborhood showing the pattern of usage" src="/assets/images/2025/solarscan_app1.png" alt="Zoomed out map display of solarscan app green/red based on the models detection result">
<div style="text-align:center;margin-bottom:20px;margin-top:5px;font-size:0.9em;">Zoomed out view of many detections in a neighborhood</div>

If you look closely in the above image, you can see that a few tiles in this region had solar panels that weren't detected.  The underlying detection models had non-zero predictions probabilities, but they didn't cross the probability threshold needed for classification.  That was why I started storing the dynamic feedback discussed in the next section to learn from the results and improve the model predictions.

#### 2. Dynamic Feedback Loop for Model Refinement

But what really sets this app apart is its built-in feedback system. After users detect solar panels, they can confirm or deny the presence of panels. This feedback is stored and displayed in a [dashboard](https://solarscan.appspot.com/dashboard), where users can see the performance of each model over the full feedback dataset.

<img title="Figures with True Positive and True Negative rates for each CNN model on the feedback dataset" src="/assets/images/2025/solarscan_dash1.png" alt="True Positive and True Negative Curves for each CNN model used for classification">
<div style="text-align:center;margin-bottom:20px;margin-top:5px;font-size:0.9em;">Figures with True Positive and True Negative rates for each CNN model on the feedback dataset</div>

If the user decides to they can trigger a function that feeds the dataset of prediction probabilities as input features to a [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) "stacked" model, which then finds the optimal combination of models to best predict.  This routine also stores the stacked model parameters for use in the main app's classifier.

<img class='small_img' title="Table of weights used to combine the different models in a logistic regression" src="/assets/images/2025/solarscan_dash2.png" alt="Model Weights for optimal prediction">
<div style="text-align:center;margin-bottom:20px;margin-top:5px;font-size:0.9em;">Table of weights used to combine the different models in a logistic regression</div>


Each time the stacked model is retrained I store the results so we can view the change in model [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score), [balanced accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score), and [F1 score](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-and-f-measures) as new training data comes in.

<img title="Figure showing model performance metrics on the training dataset over time as model is retrained on newly acquired data" src="/assets/images/2025/solarscan_dash3.png" alt="Figure showing model performance metrics on the training dataset over time as model is retrained on newly acquired data">
<div style="text-align:center;margin-bottom:20px;margin-top:5px;font-size:0.9em;">Figure showing model performance metrics on the training dataset over time as model is retrained on newly acquired data</div>

If you want to try it out you can check out the live demo on [solarscan.appspot.com](https://solarscan.appspot.com).  If you're curious you can read on below to see what goes into making a tool like this.

## How its made

This project required bits of web frontend development, computer vision research, and machine learning model platform arcitecting. The web development and computer vision aspects of this were already familiar, but this project gave me some brand new experience with building the closed-loop feedback model evaluation and stacked model training and serving production models.

#### Closed-loop Stacked Model training on Feedback

One of the most important features of this app is its ability to collect user feedback on model predictions. I stored the feedback results in Google Datastore and then built the `/dashboard` endpoint with [dash](https://plotly.com/examples/), which pulls in all the feedback data and aggregates to generate metrics and a dataset of model prediction probabilities vs the true presence/absence of a solar panel as reported by the user.

When the user triggers the stacked model retraining, the training occurs on the frontend server and a new `metamodel` entity is stored in Datastore.  The most recently saved parameters of the `metamodel` are then dynamically pulled into the main app to calculate the decision function and display the results.

#### Deploying Inference Models

Even though I'm a professional data scientist, most of my work as been on R&D and early prototyping so .  This was a fun opportunity to learn more and to figure out how to cost optimize between a few options.

1. **Vertex AI**:

I originally chose Google Cloud’s [Vertex AI](https://cloud.google.com/vertex-ai?hl=en) for deploying the models since part of this project was about learning to use a _fancy newfangled_ ML Ops system, and I'd heard people talk about Vertex before. Vertex let me package up the PyTorch models and a data ingestion script and deploy that at a named endpoint, accessible from within my Flask app on App Engine.

For usability, Vertex was a bit of a mess.  Deploying models involved several steps that weren't well-documented for PyTorch, and I had to figure out how to test with `torchserve` locally to get the handler to work before deployment.

Also, while Vertex allowed for easy scalable hosting, it turned out that Vertex AI doesn't allow deployments to shut down when not in use, which made it more expensive than I wanted. With Vertex, I'd end up spending about $3/day every day even if nobody even used the app at all.

I have free trial credits now, but there's no way I'm spending $1000/year just for an app that isn't being used at all. I'm glad to have the chance to learn how Vertex works, but I needed to look for other options.

2. **Cloud Functions**:

A second option I looked into was Google Cloud Functions which runs short running tasks without dedicated infrastructure.  Because the models were on the scale of 100 MB, it would have been tricky to use Cloud Functions though because it would spin up a new machine for _every_ request of the model. That would mean downloading and then loading each 100 MB model into memory before the inference even started.  I estimated that would make it so every request took about 10-20 seconds, which isn't a fun application to use in an interactive way.

In the end, I didn't even try to implement with Cloud Functions since it wouldn't be a usable application.

3. **App Engine Instance**:

Finally, I decided to package them up and deploy with another App Engine instance.  I have a small 700 MB instance running the frontend, but I used a separate 1500 MB instance to host all 5 CNNs in memory.  I set that instance up with "[scaling to 0](https://stackoverflow.com/questions/51272392/how-to-scale-down-to-0-instances-in-gae-standard-go)" so if there's no requests for 10 minutes it shuts that machine down.  This saves a lot of money for a rarely used app like this.

Since it has to restart from cold next time its used, that does make it so that the first response will be a little slower.  Fortunately, I came up with a neat hack that sends a dummy request to wake up the machine as soon as the frontend webpage is loaded.  That way, by the time someone has selected an area and is requesting a result from the model the backend instance will already have a few seconds headstart.

You can view the whole [solarscan codebase](https://github.com/lots-of-things/solarscan) on github to see the details of development and to build a clone for yourself if you'd like.


## Looking Ahead: Future Goals

As useful as the app is now, there are still plenty of opportunities for improvement and expansion. I've reached out to try to collaborate with the [original author](https://gabrielkasmi.github.io/) of the BDAPPV dataset to use my tool to gather more data and improve future models. One area I’m particularly interested in is tackling the [image segmentation](https://en.wikipedia.org/wiki/Image_segmentation) task next, which would help to more accurately assess the total capacity in an area rather than the coarse approximation from the current large scale detector I'm using.

Ultimately, it'd be cool to compile this information to larger and larger scales and create something similar to the [USPVDB map](https://energy.usgs.gov/uspvdb/viewer/#4.64/37.16/-120.37) of grid-scale solar. Scaling the model to that level would be a very expensive task though, but it would be wonderful to collaborate with an energy company or someone who has a marketable use for something like that. If you know anyone who'd be interested to collaborate be sure to [reach out](https://will.stedden.org).

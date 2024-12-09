---
layout: post
title: "Analyzing Housing Data in Madison"
description: "Estimating the Costs of Building a New Cohousing Complex"
type: project
tags:
- data science
- analysis
- urban planning
- sustainability
image: assets/images/2024/madison_house_prices.png
---

As part of [Isthmus Cohousing](https://isthmuscohousing.org)'s **Buy & Build Committee** in Madison, Wisconsin, my friend [Will Ochowicz](https://madisonisforpeople.org/about/will-ochowicz/) and I undertook a deep dive into the local housing market to estimate the costs associated with building a new cohousing complex. Our research involved analyzing recent housing sales, creating cost models for construction, and identifying undervalued land in the city.

### Preliminary Research on Housing Costs in Madison

The analysis began by pulling **Spring/Summer 2024 housing sales data** from **Redfin**. Redfin lets you pull sale data pretty easily, including lat/lon coordinates, which allowed us to plot the


<img class="small_img" title="Madison Housing Prices Spring.Summer 2024" src="/assets/images/2024/madison_house_prices.png" alt="Figure showing Madison with dots indicating house prices. Mainly the isthmus has higher prices and it gets cheaper going outward">
<div style="text-align:center;margin-bottom:20px;margin-top:5px;">Price per square foot of housing sold in Madison in 2024</div>

While this gave us a sense of the recent pricing trends in the Madison housing market, we needed to break it down by a number of characteristics to get a better sense of what the market rate for various types of housing looked like. One important thing was that the distribution of different types of housing varied greatly by area in the city, and that the price per square foot was different between the different types.

<img title="Madison Housing Prices broken out by housing type" src="/assets/images/2024/madison_house_prices_bytype.png" alt="3 figures showing the price and distirbution of condos, single family homes, and townhomes">


The key takeaway was that condos on the isthmus were priced in the $400-$500/sqft range while condos on the outskirts were more like $200-$300/sqft. Meanwhile, single-family homes varied from $400/sqft to $200/sqft as we moved from the isthmus outward.

Building on this, we expanded our analysis to include data from **2019-2024**. This allowed us to develop a more robust model for estimating housing prices based on property characteristics. The model incorporated **size** (square footage), **age** of the property, and **number of bedrooms** to estimate costs. We found that **newer homes**, **larger homes**, and those with more bedrooms generally commanded a higher premium. In addition, **location** played a major role in pricing, with homes located closer to downtown or the university fetching significantly higher prices than those further out.

Overall we ended up with a fairly robust and well-performing price explaination model that could accurately predict how much a unit could expect to sell for throughout the city.  You can explore the detailed calculations and code used in this analysis in our [**Jupyter notebook**](https://github.com/stedn/isthmuscohousing/blob/main/research.ipynb). This notebook contains all the data processing and housing cost modeling steps that we performed.

### Building a Simple Pro-Forma Calculator for Construction Costs

Once we had a better understanding of the local housing market, we moved on to estimating the cost of constructing a new cohousing complex. To do this, we built a simple **comparative build cost calculator**, (somewhat similar to a [pro forma](https://www.procore.com/library/construction-pro-forma)). The idea was to estimate the total costs involved in building on a given lot, taking into account various factors like **land cost**, **construction costs**, **soft costs** (such as legal fees and financing), and **parking costs** (which can be a major expense, especially in urban areas).

<img title="Madison Housing Build Cost Estimator" src="/assets/images/2024/housing_build_cost_estimator.png" alt="screenshot from spreadhseet">


Our pro-forma calculator provided estimates for total construction costs, the **cost per unit**, and the **cost per square foot** based on inputs like lot size and expected building height. It helped us assess how much it would cost to build a cohousing project on different types of properties throughout Madison. This tool also allowed us to break down the cost per unit and per square foot, which can be crucial for budgeting and securing financing.

You can check out the comparative cost calculators used in this phase of the project in our [**Google Spreadsheet**](https://docs.google.com/spreadsheets/d/1TtQ2JAtsHY10p2qyAIj3GrdY1GO239JsO1JqY6EAtQ0/edit?usp=sharing). The spreadsheet contains all the assumptions and input values we used to estimate construction costs and per-unit expenses.

### Combining Lot Data with Zoning Information

With the initial cost models in place, we wanted to take the next step and analyze the **build potential** of different lots throughout Madison. This is where we enlisted the help of Will Ochowicz, who helped us combine **lot assessment data** with **zoning and use codes** from the city. By doing this, we were able to compute the maximum number of units that could be built on each lot, based on zoning restrictions, lot size, and allowed building height.

Using this combined dataset, we ran the information through our comparative build cost calculator. This allowed us to estimate how large a building could be constructed on each lot, how much it would cost to build, and what the **cost per unit** would be for a potential cohousing development. Our goal was to identify **undervalued lots**—those that might offer a good opportunity for a cohousing project based on their **build potential** and cost-efficiency.

<a href="https://docs.google.com/spreadsheets/d/1TtQ2JAtsHY10p2qyAIj3GrdY1GO239JsO1JqY6EAtQ0/edit?usp=sharing"><img title="Madison Housing Prices broken out by housing type" src="/assets/images/2024/housing_build_cost_estimator_plus.png" alt="another spreadsheet">
</a>

This step was particularly useful in finding lots where we could get the most out of the land and achieve a higher number of units at a lower cost, which is a crucial factor when trying to build an affordable housing project. The data we gathered provided a clearer picture of where the **best opportunities for development** might lie.

### The Reality of the Madison Housing Market

Despite the promising analysis and our identification of potentially undervalued land, the reality of the Madison housing market quickly became apparent. While we were able to identify several lots with good build potential, the availability of land for sale was **extremely limited**. Out of all the parcels we analyzed, only a **small handful** were on the market at the time, and none of these made good financial sense for our cohousing project.

What we discovered was that developers are snatching up any land that appears to be priced reasonably, leaving little room for new, affordable developments. In Madison, if a piece of land is reasonably priced and has potential for development, developers are quick to act, making it difficult for new cohousing projects to compete in this market.

In the end, it became clear that the best approach in Madison is to make connections to know what is available before it makes its way to Redfin or Zillow. The housing market is highly competitive, and developers are already moving quickly on any parcels that make financial sense. While our analysis was insightful and gave us a better understanding of the costs and potential for building a cohousing complex in Madison, it also reinforced the reality that finding affordable land in the right locations is incredibly challenging.

### Conclusion

This research exercise was a valuable opportunity to better understand the costs of building and the zoning potential of different properties in Madison. The process helped us gain insights into land availability, housing pricing trends, and how to model construction costs for a cohousing project. However, the biggest takeaway was that in Madison, the availability of land is a major barrier to new affordable housing projects.

We're still continuing with the dream of cohousing in Madison, but we now know just how challenging it will be to turn that dream into reality.

---

You can explore our **full analysis and data** from this research through the following resources:
- [**Jupyter notebook for housing cost calculations**](https://github.com/stedn/isthmuscohousing/blob/main/research.ipynb)
- [**Google Spreadsheet for comparative cost calculators**](https://docs.google.com/spreadsheets/d/1TtQ2JAtsHY10p2qyAIj3GrdY1GO239JsO1JqY6EAtQ0/edit?usp=sharing)

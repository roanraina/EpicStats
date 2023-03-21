# EpicStats Project Proposal

## Motivation and Purpose

Our role: Data enthusiast

Target audience: Data-keen skier and snowboarders

Sport data can be a useful tool in providing insights about our workouts, fitness, and progress. Currently, [Vail Resorts](http://www.vailresorts.com), which owns [Whistler Blackcomb](https://www.whistlerblackcomb.com) a local mountain to us here in Vancouver, provides [EpicMix](https://www.epicpass.com/benefits/epicmix) a phone app based interface for viewing these statistics. However, the UI is cumbersome to extract valuable information from and a web-based interface is not available. To address this challenge, we propose building a data visualization app that allows skiers and snowboarders to visually explore their own data. Our app will show plots of vertical distance and allow users to explore different aspects of this data by filtering based on different variables. This will allow riders to better understand their time on the mountain. 

## Description of the Data

Since we are using each individuals personal dataset, the data will vary between user, however since we are pulling the data from Vail's EpicMix we can expect a standard structure.
For each user, summary statistics for the `lifetime`, `season`, and `day` are available in addition to the `daily lift history`.
The summary statistics include metrics such as 'total vertical feet', 'number of lift rides', and 'number of days on mountain'.
The lift history include the resort name, chair name, and time the lift was ridden.
We can expect to see any number of entries for these statistics as different riders will have spent varying amounts of time in resort.
However, we would expect the typical user to have skied for more than one season, for more than 10 days, taking around 10 lifts per day, therefore having sufficient data for valuable visualizations.

> Disclaimer:
>
> This project is not associated with or endorsed by Vail.

## Research Questions

This dashboard will focus on the following research questions:

1. Is there a trend for number of days skiied (between seasons)?
2. Is there a trend for total vertical distance skiied (over a season, between seasons)?
3. What are a riders most ridden lifts?

## Usage Scenario

Say you skier curious about your time spent on Whistler. You go to the EpicMix app and find you total elevation for each day and a list of the lifts you took. Excited by this information, you want to graph the change over the course of a season, or compare seasons. Currently, this would require you shifting between multiple pages on your phone and copying the information manually if you wanted manipulate it further. This app will allow you to view plots of your elevation, lifts, and days skied with the option of downloading all your own raw data as a csv. You can then use this information to learn more about how you spend your time on the mountain.

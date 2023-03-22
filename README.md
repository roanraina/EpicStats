# EpicStats

A simple Dash app to view your EpicMix stats online.

## EpicMix Statistics

Sport data can be a useful tool in providing insights about our workouts, fitness, and progress. Currently, [Vail Resorts](http://www.vailresorts.com), which owns [Whistler Blackcomb](https://www.whistlerblackcomb.com) a local mountain to us here in Vancouver, provides [EpicMix](https://www.epicpass.com/benefits/epicmix) a phone app based interface for viewing these statistics. However, the UI is cumbersome to extract valuable information from and a web-based interface is not available. To address this challenge, we propose building a data visualization app that allows skiers and snowboarders to visually explore their own data. Our app will show plots of vertical distance and allow users to explore different aspects of this data by filtering based on different variables. This will allow riders to better understand their time on the mountain.

## Use the App

To use the app, you can find it here, at the [EpicStats](https://epicstats.onrender.com/) site!

## About the Data

Since we are using each individuals personal dataset, the data will vary between user, however since we are pulling the data from Vail's EpicMix we can expect a standard structure.
For each user, summary statistics for the `lifetime`, `season`, and `day` are available in addition to the `daily lift history`.
The summary statistics include metrics such as 'total vertical feet', 'number of lift rides', and 'number of days on mountain'.
The Data is pulled using the `EpicMix` python package which can be found [here](https://github.com/roanraina/EpicMix).

A more in-depth explanation can be found in [the proposal](docs/proposal.md).

## Description of the Dashboard

This dashboard entails a two step process:

1. Login
    - users must enter their EpicMix username and password to gain entry to the visualizations

2. Visualizations
    - A plot of `Vertical (Meters)` vs Date is presented for the most recent ski season.
    - Dropdowns for seasons and metric presented (`Vertical Distance` of `Lifts`) which automatically update the plot.
    - A `Download CSV` button to download a *.csv file of the raw data currently plotted.

## Contribute

Interested in contributing? Check out the [Contributing](CONTRIBUTING.md) guidelines.
By contributing to this project, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

There is substantial room to continue development of the project. If you have an idea, please let us know by opening an issue in the repository!

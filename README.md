# Stress Testing: Predicting Loss under Adverse Economic Conditions

This repository includes the code used to perform stress testing based on economic scenarios using loan portfolio. The application was originally done on [```MATLAB```](https://www.mathworks.com/matlabcentral/fileexchange/67771-stress-testing-predicting-loss-under-adverse-economic-conditions) and we extended it to the open-source ```Python``` programming language.

## Prerequisites

The ```Python``` programming language, version 3.7.13, and its statistical libraries were used to build all applied models. The ```Python``` script _stress_test.py_ in the _python_ folder contains the script necessary to reproduce the results.

All operations, from data preprocessing to model estimation, were carried out on the Google Colaboratory platform.

## Theoretical Background

Bank stress testing is a framework for analyzing the impact of simulated extreme, but plausible, economic and financial conditions to ensure that banks have sufficient capital to maintain operations during such situations. Banking stress tests were introduced by central banks and authorities in charge of banking supervision in the late 1990s. From that time, the more frequent banking and financial crises, and in particular the Asian crisis of 1997, had highlighted the role of the deterioration of macroeconomic factors in the triggering of banking crises which  were not sufficiently taken into account in other methods of banking regulation and supervision.

## Application and Results

The applied generalized linear model takes into account, in addition to loan information, economic data in order to predict the probability of default. An adverse economic setting is then defined in order to assess and analyze the rates of default under such conditions.

## Code Structure

### About The Data

The _data_ folder contains the portfolio of outstanding, ane historical, loans as well as economic and financial time series under normal and stressed conditions.

### Model Building and Estimation

The generalized linear model in this application was built and estimaed using the ```statsmodels``` library.

# Stress Testing: Predicting Loss under Adverse Economic Conditions

This repository includes the code used to perform stress testing based on economic scenarios using loan portfolio. The application was originally done on [```MATLAB```](https://www.mathworks.com/matlabcentral/fileexchange/67771-stress-testing-predicting-loss-under-adverse-economic-conditions) and we extended it to the open-source ```Python``` programming language.

## Prerequisites

The ```Python``` programming language, version 3.7.13, and its statistical libraries were used to build all applied models. The ```Python``` script _stress_test.py_ in the _python_ folder contains the script necessary to reproduce the results.

All operations, from data preprocessing to model estimation, were carried out on the Google Colaboratory platform.

## Theoretical Background

Bank stress testing is a framework for analyzing the impact of simulated extreme, but plausible, economic and financial conditions to ensure that banks have sufficient capital to maintain operations during such situations. Banking stress tests were introduced by central banks and authorities in charge of banking supervision in the late 1990s. From that time, the more frequent banking and financial crises, and in particular the Asian crisis of 1997, had highlighted the role of the deterioration of macroeconomic factors in the triggering of banking crises which  were not sufficiently taken into account in other methods of banking regulation and supervision.

## Application and Results

We note that, for all volatility and distribution specifications, the Markov regime-switching models offer a better trade-off between goodness-of-fit and model complexity than their single-regime counterparts. Furthermore, we note that for all regime specifications, asymmetric and fat-tailed distributions are widely preferred. The three-regime GARCH model with a Student-t distribution is found to be the best fit to our data based on Akaike's information criterion, 9232.1672. While the standard single-regime GARCH model with a Student-t distribution was found to be the best based on the Bayesian information criterion, 9306.0622. A point raised by several researchers is that Akaike and Bayesian information criteria are appropriate for different tasks. In particular, the Bayesian information criterion is considered appropriate to select the so-called true model among the set of candidate models, while Akaike's information criterion is not appropriate. Proponents of Akaike's information criterion argue that this problem is negligible, since the true model is almost never in the candidate set. In a simulation study by Scott I. Vrieze, Akaike's information criterion was shown to sometimes select a much better model than its Bayesian counterpart even when the true model is in the candidate set. The reason is that, for finite n, the Bayesian information criterion may have a substantial risk of selecting a very bad model from the candidate set. With Akaike's information criterion, the risk of selecting a very bad model is minimized. The volatility of MASI returns is separated into three regimes: a high volatility regime, a medium volatility regime, and a low volatility regime. The high volatility regime is linked to significantly high return spreads, the medium volatility regime is linked to moderately high return spreads, and the low volatility regime is linked to low return fluctuation. The parameter estimates indicate that the evolution of the volatility process is heterogeneous between the three regimes. Indeed, the three regimes report different levels of unconditional volatility: 9.0437% in the first regime, 9.7334% in the second regime and 20.8600% in the third. Moreover, the persistence of volatility in each of the regimes is different. The first regime yields 0.8046, the second regime yields 0.5605, while the third yields 0.8960. The stable probabilities indicate that the probability of being in the first regime is 0.4330, while being in the second or third is 0.4049 and 0.1621, respectively. Additionally, the estimated probability of staying in the same market conditions over the next period is high for all three regimes, exceeding 95%. While the probabilities associated with switching from one regime to another are very low. Finally, the results from backtesting VaR at 5% risk show that the two-regime Markov-switching GARCH model with a Student-t distribution outperforms its single-regime and three-regime counterparts. 

## Code Structure

### About The Data

The _data_ folder contains the portfolio of outstanding, ane historical, loans as well as economic and financial time series under normal and stressed conditions.

### Model Building and Estimation


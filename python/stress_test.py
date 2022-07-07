# SUPPLEMENTARY CODE FOR THE MASTER PROJECT: 
# Stress Testing: Predicting Loss under Adverse Economic Conditions

# This script demonstrates a basic work flow for stress testing in banking portfolio.

# Loading Python libraries.
% matplotlib inline
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Read credit portfolio.
myPortfolio = pd.read_excel("OutstandingLoans.xlsx")

# Read historical loans.
myLoanHistory = pd.read_excel("OldLoans.xlsx")

# Read economic and financial data from the Fed.
FedHistory = pd.read_csv("Simplified_FedHistory.csv")

# Combine both datasets.
combinedHistory = pd.merge(myLoanHistory, FedHistory, on = "Year")

# Model Building.
model = smf.glm(formula = "Default ~ RiskLevel + YOB + DJX_Return + GDP", 
                data = combinedHistory, 
                family = sm.families.Binomial())

# Model fitting.
result = model.fit()

# Display results.
print(result.summary())

# Estimated default probabilities.
predictions = result.predict()

# Compute historical portfolio default rates.
Default = []
for i in range(np.shape(combinedHistory["YOB"].unique())[0]):
  YOB = combinedHistory.loc[combinedHistory["YOB"] == i + 1]
  DefaultFreq = YOB["Default"].value_counts()
  DefaultRate = (DefaultFreq.values[1]/(DefaultFreq.values[0] + DefaultFreq.values[1]))*100
  Default.append(DefaultRate)

# Dataframe containing years on books and predictive model probabilities.
myModel = pd.DataFrame({"YOB": np.array(combinedHistory["YOB"]), "estDefault": predictions})

# Compute estimated default rates.
estDefault = []
for i in range(np.shape(myModel["YOB"].unique())[0]):
  YOB = myModel.loc[myModel["YOB"] == i + 1]
  estDefaultFreq = YOB["estDefault"].mean()*100
  estDefault.append(estDefaultFreq)

# Adverse economic scenario.
AdverseScenario = pd.read_csv("Simplified_Adverse.csv")

# Portfolio under adverse economic conditions.
AdversePortfolio = myPortfolio.assign(Year = AdverseScenario.iloc[0, 0], 
                                      DJX_Return = AdverseScenario.iloc[0, 1], 
                                      GDP = AdverseScenario.iloc[0, 2])

# Predicted default probabilities under adverse economic conditions.
PD = result.predict(AdversePortfolio)

# Dataframe containing years on books and predictive model probabilities under adverse economic conditions.
predPD = pd.DataFrame({"YOB": np.array(myPortfolio["YOB"]), "PD": PD})

# Compute predicted default rates.
predDefault = []
for i in range(np.shape(predPD["YOB"].unique())[0]):
  YOB = predPD.loc[predPD["YOB"] == i + 1]
  predDefaultFreq = YOB["PD"].mean()*100
  predDefault.append(predDefaultFreq)

# Compute the expected loss of the loan portfolio under adverse economic conditions.
ExpectedLoss = sum(AdversePortfolio["EAD"]*AdversePortfolio["LGD"]*PD)

# Visualization with matplotlib.
plt.subplot(2, 1, 1)
plt.plot(combinedHistory["YOB"].unique(), Default, "o-", color = "blue", label = "Histotical Portfolio")
plt.title("Defaul Rate (%)")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(myModel["YOB"].unique(), estDefault, "o-", color = "green", label = "Fitted Model")
plt.xlabel("YOB")
plt.legend()

plt.plot(predPD["YOB"].unique(), predDefault, "o-", color = "red", label = "Predicted Adverse Portfolio")
plt.title("Defaul Rate (%)")
plt.xlabel("YOB")
plt.legend()

plt.show()
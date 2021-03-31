# Sepsis early detection: Project Overview 
* Created a tool that predicts Sepsis six hours befor onset with six vital signs.
* The data obtained is a 40.336 patient strong dataset from the Beth Israel Deaconess Medical Center and Emory University Hospital, collected from 2001 and 20012.
* Using the six most common ED vital signs (Heart rate, O2Sat, Temperature, Systolic BP, MAP, and Respiration rate) as features.
* Ada Boost, Gradient Boosting, Linear Regression, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a patient facing Web APP using Streamlit. 

# Sepsis
###### Sepsis is a life-threatening condition caused by your body’s response to an infection (bacterial, viral or fungal) and damages its own tissues.
Sepsis is the leading cause of global mortality, around 20% of annual global death. Eraly detection is vital in the survival of the patient. Every 10 min death risk increases by significantly (1%-3%).

## Code and Resources Used 
**Python Version:** 3.9
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**PhysioNet Challenge 2019:** https://physionet.org/content/challenge-2019/1.0.0/

## Data Cleaning
Data cleaning:

*	Drop adolecets data because of there different physiology.
*	Drop excess features.
*	First fills in missing values by carrying forward, then fills backwards. The backwards method takes care of the


## EDA
I looked at the distributions of the data and the value counts for the six variables. Below are a few highlights. 

![Heatmap](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/heatmap.png "Heatmap")
![Missing values](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/missingValues.png "Missing Values in percentage")
![Patient 1216](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/patient1216.png "Patient 1216")

## Model Building 

First, I also split the data into train and tests sets with a test size of 20%.   

I tried  different models and evaluated them using the area under the receiver operating characteristic curve. I chose AU ROC to compare it to the existing algorithms like InSight(0.91) of the Sepsis risk indicators like SIRS, SOFA or MEWS (0.61, 0.73 and 0.80, respectively). 
InSight was trained on different Datasets and more Freatures, the common risk indicator all take other fearutes into account, the best inditicator to compare our model is to qSOFA.

I tried six different models:
*	**Multiple Linear Regression**, **Gaussian Naive Bayes**,	**Decision Tree** – Baseline for the model 
*	**Random Forest** **Ada Boost**, **Gradient Boosting** - Good collection of models to train this data on
*	**XGBoost** -- Is an exceptionally useful machine learning method when you don't want to sacrifice the ability to correctly classify observations but you still want a model that is fairly easy to understand and interpret.

## Model performance
The Random Forest model and XGBoost outperformed the other approaches on the test and validation sets. 
* **XGBoost**: `AUROC = 0.72`
*	**Random Forest**: `AUROC = 0.72` 
*	**GradientBoostingClassifiern**: `AUROC = 0.69` 
*	**AdaBoostClassifier**: `AUROC = 0.69`

## XGBoost 
We use the XGBoost model since it is more senible to the sepsis positiv patients.

### Optimize Parameters using Cross Validation and GridSearch()

**XGBoost** has a lot of *hyperparameters*, parameters that we have to manually configure and are not determined by **XGBoost** itself, including `max_depth`, the maximum tree depth, `learning_rate`, the learning rate, or "eta", `gamma`, the parameter that encourages pruning, and `reg_lambda`, the regularization parameter lambda. 
##### Result:con
* `gamma=0`
* `learn_rate=0.1`
* `max_depth=8`
* `scale_pos_weight=60`
* `reg_lambda=10`

#### Confusion matrix:
![Confusion Matrix](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/descarga.png "Confusion matrix")
#### First XGBoost Tree:
`weight:  {'HR': 25, 'Resp': 19, 'O2Sat': 17}
gain:  {'HR': 2722.8444263319993, 'Resp': 2403.9058481052634, 'O2Sat': 665.0437755764705}
cover:  {'HR': 49814.29, 'Resp': 66938.6447368421, 'O2Sat': 42674.92647058824}
total_gain:  {'HR': 68071.11065829998, 'Resp': 45674.211114000005, 'O2Sat': 11305.744184799998}
total_cover:  {'HR': 1245357.25, 'Resp': 1271834.25, 'O2Sat': 725473.75}`
![Tree](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/tree.png "Tree")

## Productionization 
In this step, I built a web App, which takes in the six vitals of a patient and returns a sepsis prediction:

https://earlydetectionapp.herokuapp.com/

![App](https://github.com/JonasGrabbe/SepsisApp/blob/main/images/sepsisAppSS.png "App")

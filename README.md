# Sepsis early detection: Project Overview 
* Created a tool that predicts Sepsis six hours befor onset with six vital signs.
* The data otained is a 40.336 patient strong dataset from the Beth Israel Deaconess Medical Center and Emory University Hospital, collected from 2001 and 20012.
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

![alt text](https://github.com/JonasGrabbe/SepsisApp/blob/main/heatmap.png "Heatmap")
![alt text](https://github.com/JonasGrabbe/SepsisApp/blob/main/missingValues.png "Missing Values in percentage")
![alt text](https://github.com/JonasGrabbe/SepsisApp/blob/main/patient1216.png "Patient 1216")

## Model Building 

First, I also split the data into train and tests sets with a test size of 20%.   

I tried  different models and evaluated them using the area under the receiver operating characteristic curve. I chose AU ROC to compare it to the existing algorithms like InSight(0.91) of the Sepsis risk indicators like SIRS, SOFA or MEWS (0.61, 0.73 and 0.80, respectively). 
InSight was trained on different Datasets and more Freatures, the common risk indicator all take other fearutes into account, the best inditicator to compare our model is to qSOFA.

I tried six different models:
*	**Multiple Linear Regression**, **Gaussian Naive Bayes**  – Baseline for the model
*	**Decision Tree**, **Random Forest** 
*	**Ada Boost**, **Gradient Boosting** 


## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : AUROC = 0.72 
*	**GradientBoostingClassifiern**: AUROC = 0.69 
*	**AdaBoostClassifier**: AUROC = 0.69 

## Productionization 
In this step, I built a web App, which takes in the six vitals of a patient and returns a sepsis prediction. 


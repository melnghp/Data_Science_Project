# Network Intrusion Detection System


## Background

With increasing cases of cyber attacks, it is important to identity irregular or abnormal network traffic. A network-based intrusion detection system (NIDS) is usually in place after the firewall to analyse inbound and outbound network packets for patterns of malicious behavior.

The NIDS passively collects data and analyse to determine whether the information falls outside normal activity based on a knowledge base. If so, an alert is sent ([source](https://ukdiss.com/examples/intrusion-prevention-security.php)).

As such, it is important for NIDS to be accurate in classifying network traffic as high false positive (classifying normal traffic as attacks) may result in operational overhead whereas high false negative (classifying attacks as normal traffic) may lead to prolonged attack continue to go undetected and further conpromising the environment.

## Problem Statement
The main object of this project is aiming to increase reduce both false positive and negative.

## Dataset

The [dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset) is created by the IXIA PerfectStorm tool in the Cyber Range Lab of UNSW Canberra, generating a hybrid of real modern normal activities and synthetic contemporary attack behaviours. 

The raw dataset is made up of 4 CSV files with a total of 2,540,044 records. The datasets have 49 features including the class label.

| File Name|Number of records|
| ---| ---|
|[UNSW\_NB15_1.csv](../dataset/UNSW_NB15_1.csv)|700000|
|[UNSW\_NB15_2.csv](../dataset/UNSW_NB15_2.csv)| 700000|
|[UNSW\_NB15_3.csv](../dataset/UNSW_NB15_3.csv)| 700000|
|[UNSW\_NB15_4.csv](../dataset/UNSW_NB15_4.csv)| 440044|

## Data Dictionary
Data dictionary of the default features are documented in [UNSW\_NB15_features.csv](../dataset/UNSW_NB15_features.csv)


## Data Selection
Due to the large amount of data and limition of the laptop used, we have selected to work on data dated 18-02-2015 as it has a less servere data imbalance among the 3.

|Date|Total records|Normal Traffic (%)|Attack (%)|
|---| ---| ---| ---|
|18-02-2015| 1035294| 91.8|8.22|
|22-01-2015| 989104| 98.6| 1.44|
|23-01-2015| 33930| 100| 0|

## Preprocessing

1. Dummfy categorical features.
2. Apply SMOTE on train data to handle severe data imbalance where 95% of the records were  without WNV and 5% detected with WNV.  
3. Apply minmax scaling on train data.


## Model Evaluation

|Model|Train F1|Test F1|Generalise|Precision|Recall|AUC_ROC|
| ---| ---| ---|---| ---|---| ---|
|---| ---| ---|---| ---|
|---| ---| ---|---| ---|


The models were created using Logistic Regression, Decision Trees, Random Forest, Gradient Boost and XG Boost. All models except the Decision Trees model perform better than the baseline model which has an AUC_ROC score of 0.941.

Among the remaining 4 models, the gradient boost model has the best test accuracy and F1 score of 0.956 while XGboost model has the best sensitivity score of 0.958.

The final selection was gradient boost model as it has the best AUC_ROC score while still maintaining relevatiely good sensitivity score of 0.950.

![](../image/AUC_ROC.png)
![](../image/confusionmatrix.png)


## Business Case
Without a model, for every 100 network 

|Feature|Type|Description|
| ---| ---| ---|
|Without model| ---| ---|
|With model| ---| ---|



## Conclusion



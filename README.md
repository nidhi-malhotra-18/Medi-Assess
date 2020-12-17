# Emergency Department Triage Prediction of Clinical Outcomes using Machine Learning Models

Our work focuses on predicting the clinical outcome of patient from the triaging data collected. 

Triaging is a process in which using some basic questions and vital information of a patient is collected and a score is provided which tells the urgency to act and stabilize the patient. This is important in prioritizing patients and providing services first to those who need them the earliest. Some standard triaging systems are:

* ESI Protocol
* Canadian Triaging Index
* Australasian Severity Index
* SATS Protocol

These systems help to give a score for Traiging and tell us how fast to act. But often due to resource scarcity, resource allocation of hospital services is based on who is going to be benefitted the most. This work is based on using Machine Learning Strategies for Predictive Analysis of patients outcome. 

# Data Preprocessing

Pre-Processing

The NHAMCS i.e. the National Hospital Ambulatory Medical Care Survey -ED data from years 2007- 2017 is used. This data is coded into numbers and a reference guide is attached corresponding to each year. Data can be accessed from the website https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm. The data extraction code for each year's data can be found in the CodeFiles folder. Emergency_Data.csv contains the combined csv extracted for all years.


# Model Development


<img src="https://github.com/nidhi-malhotra-18/Medi-Assess/blob/main/model.png" width="400" height="400"/>
model.py file contains the code for a LightGBM model used the predict the emergency outcomes.


# Results

We obtain the AUC-ROC score of 0.7611 using the Light GBM model. The multi-class one vs. all AUCROC of very critical - Class 0 is 0.95, Critical - Class 1 is
0.72, Hospitalized - Class 2 is 0.67, and Discharge - Class 3 is 0.70.

<p>
  <img src="https://github.com/nidhi-malhotra-18/Medi-Assess/blob/main/LightGBM.png" width="400" height="400"/>
</p>



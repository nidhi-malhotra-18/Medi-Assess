import numpy as np
import pandas as pd
import lightgbm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

data=pd.read_csv('AAI_Data.csv')
data=data.drop('Unnamed: 0',1)

X=data.drop("Result",1)
y=data['Result']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train_data = lightgbm.Dataset(x_train, label=y_train)
params={}
params['learning_rate']=0.03
params['boosting_type']='gbdt' #GradientBoostingDecisionTree
params['objective']='multiclass' #Multi-class target feature
params['metric']='multi_logloss' #metric for multi-class
params['max_depth']=10
params['num_class']=4

model = lightgbm.train(params,train_data)
y_pred = model.predict(x_test)

from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
pred = a
pred_prob = y_pred
y_test = np.array(y_test)

# roc curve for classes
fpr = {}
tpr = {}
thresh ={}
n_class = 4
roc_auc = dict()
for i in range(n_class):    
    fpr[i], tpr[i], thresh[i] = roc_curve(y_test, pred_prob[:,i], pos_label=i)
    roc_auc[i] = auc(fpr[i], tpr[i])
    
# plotting    
plt.plot(fpr[0], tpr[0], linestyle='--',color='orange', label='Class 0 vs Rest')
plt.plot(fpr[1], tpr[1], linestyle='--',color='green', label='Class 1 vs Rest')
plt.plot(fpr[2], tpr[2], linestyle='--',color='blue', label='Class 2 vs Rest')
plt.plot(fpr[3], tpr[3], linestyle='--',color='red', label='Class 3 vs Rest')
plt.title('Multiclass ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive rate')
plt.legend(loc='best')
plt.savefig('LightGBM.png',dpi=300)


from sklearn.metrics import classification_report
print(classification_report(y_test,a))

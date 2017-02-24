'''
Created on Feb 14, 2017

@author: Inthuch Therdchanakul
'''
from Data.Datasets import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from Data.Datasets import pre_processing

df = pd.read_excel("Data.xlsx")
df = df[["AREA", "LDP","PROPWET", "RMED-1D", "SAAR", "Index flood"]]
df = pre_processing(df)
features = np.array(df.drop("Index flood", axis=1)) 
ds = datasets(df, features, "Index flood")
print(ds.feature_names)

X = ds.features
y = ds.label
X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
predictions = clf.predict(X_test)
print(accuracy)
'''
Created on Feb 14, 2017

@author: Inthuch Therdchanakul
'''
import numpy as np

class datasets():
    def __init__(self, df, features, label, max_label, min_label):
        self.features = features
        self.label = np.array(df[label])
        self.feature_names = df.drop(label, axis=1).columns.values
        self.label_name = label
        self.max_label = max_label
        self.min_label = min_label
    
    def de_standardise(self, label):
        for i in range(0, len(label)):
            label[i] = (((label[i] - 0.1)/(0.8)) * (self.max_label - self.min_label)) 
            + self.min_label
        return label
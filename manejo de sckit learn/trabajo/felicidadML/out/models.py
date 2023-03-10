import numpy as np 

from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

from utils import Utils 

class Models:
    
    def __init__(self):
        #diccionario de modelos a utilzar
        self.reg = {
            'SVR' : SVR(),
            'Gradient' : GradientBoostingRegressor()
        }
        
        self.params = {
            'SVR' : {
                'kernel' : ['linear','poly','rbg'],
                'gamma' : ['auto','scale'],
                'C' : [1,5,10]
            },
            'Gradient' : {
                'loss' : ['ls','lad'],
                'learning_rate' : [0.01,0.05, 0.1]
            }
        }
    
    def grid_training(self, features, target):
        
        best_score = 999
        best_model = None 
        
        for name,reg in self.reg.items():
            
            grid_reg = GridSearchCV(reg, self.params[name]).fit(features,target.values.ravel())
            score = np.abs(grid_reg.best_score_)
            
            if score < best_score:
                best_score = score
                best_model = grid_reg.best_estimator_
            
        utils = Utils()
        utils.model_export(best_model,best_score)
        
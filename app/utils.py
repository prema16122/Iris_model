import json
import pickle
import numpy as np
import os
from flask import render_template,request
import CONFIG

class Prediction():
    def __init__(self):  
        print(os.getcwd())

    def load_raw(self):
        with open(CONFIG.MODEL_PATH,'rb') as model_file: 
            self.model = pickle.load(model_file)
        
        with open(CONFIG.ASSET_PATH,'r') as col_file: 
            self.column_names = json.load(col_file)


    def predict_species(self,data):  

        self.load_raw() 
        self.data=data
        user_input = np.zeros(len(self.column_names['Column Names']))
        sepal_length = self.data['html_sl'] 
        sepal_width = self.data['html_sw']
        petal_length = self.data['html_pl']
        petal_width = self.data['html_pw']

        user_input[0] = sepal_length
        user_input[1] = sepal_width
        user_input[2] = petal_length
        user_input[3] = petal_width

        print(f"{user_input=}")
        result= self.model.predict([user_input])

        if result[0] == 0:
            Species = "SETOSA"
        if result[0] == 1:
            Species = "VERSICOLOR"
        if result[0] == 2:
            Species = "VIRGINICA"
        
        print(f"Predicted Speices of Iris = {Species[result[0]]}")      

        return render_template("iris.html",PREDICT_VALUE=Species)
    
    if __name__ == "__main__":
        
        pred_obj = Prediction()
        pred_obj.load_raw()

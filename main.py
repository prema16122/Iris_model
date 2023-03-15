from flask import Flask ,render_template,request
from app.utils import Prediction

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('iris.html')

@app.route('/predict',methods = ["POST","GET"])
def predict_species():
    data =request.form
    pred_obj = Prediction()
    predicted_Species = pred_obj.predict_species(data)
    
    print(predicted_Species)
    return str(predicted_Species)
  

if __name__ == "__main__":
    app.run(debug=True)
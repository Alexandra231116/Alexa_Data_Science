# prediction function
from flask import Flask, request, render_template
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 16)
    loaded_model = pickle.load(open("model_final.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
    #return 1
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)                   
        return render_template("result.html", prediction ="The predicted price is {}".format(result))
    
if __name__ == '__main__':
    app.run(debug=True)
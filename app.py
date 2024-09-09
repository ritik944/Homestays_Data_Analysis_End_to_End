from flask import Flask , render_template, request
import os 
import numpy as np
import pandas as pd
from Homestayes_data.pipeline.prediction import PredictionPipline


app= Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "training successfull"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            
            accommodates=float(request.form['accommodates'])
            bathrooms=float(request.form['bathrooms'])
            cleaning_fee=float(request.form['cleaning_fee'])
            latitude=float(request.form['latitude'])
            longitude=float(request.form['longitude'])
            number_of_reviews=float(request.form['number_of_reviews'])
            review_scores_rating=float(request.form['review_scores_rating'])
            bedrooms=float(request.form['bedrooms'])
            beds=float(request.form['beds'])
            
            
            
            # #  reading the inputs given by the user
            # fixed_acidity =float(request.form['fixed_acidity'])
            # volatile_acidity =float(request.form['volatile_acidity'])
            # citric_acid =float(request.form['citric_acid'])
            # residual_sugar =float(request.form['residual_sugar'])
            # chlorides =float(request.form['chlorides'])
            # free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            # total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            # density =float(request.form['density'])
            # pH =float(request.form['pH'])
            # sulphates =float(request.form['sulphates'])
            # alcohol =float(request.form['alcohol'])
       
         
            data = [accommodates, bathrooms, cleaning_fee,latitude, longitude, number_of_reviews, review_scores_rating,bedrooms, beds]
            data = np.array(data).reshape(1, 9)
            
            obj = PredictionPipline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8080)
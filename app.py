from flask import Flask , render_template, request
import os 
import numpy as np
import pandas as pd
from Homestayes_data.pipeline.prediction import PredictionPipline


app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "training successfull"




if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8080)
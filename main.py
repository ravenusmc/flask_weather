#This is the main file for the project.

import pandas as pd
import numpy as np
from basic import *

#importing all files
from flask import Flask, render_template, request

#Setting up flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/basic')
def basic_page():
    weather = Weather()
    #data.top_part()
    top = weather._Weather__data.head()
    # data = pd.read_csv('weather.csv')
    # test = data.head()
    return render_template('basic.html', title='Basic Info Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About Me')

#This line will actually run the app.
app.run(debug=True)

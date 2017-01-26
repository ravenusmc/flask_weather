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

@app.route('/basic_weather')
def basic_page():
    weather = Weather()
    mean = weather.get_mean_temp()
    high_mean = weather.get_mean_high_temp()
    low_mean = weather.get_mean_low_temp()
    rain_mean = weather.get_mean_rain()
    return render_template('basic_weather.html', title='Basic Weather Page', one = mean, two = high_mean,
    three = low_mean, four = rain_mean)

@app.route('/about')
def about():
    return render_template('about.html', title='About Me')

#This line will actually run the app.
app.run(debug=True)

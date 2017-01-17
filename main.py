#This is the main file for the project.

#importing all files
from flask import Flask, render_template, request

#Setting up flask
app = Flask(__name__)



#This line will actually run the app. 
app.run(debug=True)

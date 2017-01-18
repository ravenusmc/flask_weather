#This is the main file for the project.

#importing all files
from flask import Flask, render_template, request

#Setting up flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')
    
#This line will actually run the app.
app.run(debug=True)

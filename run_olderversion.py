#This is the older version of the run file
#The final version of the run file is "run.py"
import os
from flask import Flask, flash, request, redirect, url_for, render_template
import news as nf
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home(): # Home page for project 
    return render_template('index.html')

@app.route("/newsfeed", methods=['GET','POST'])
def newsfeed():
    if request.method == 'POST':
        publisher = request.form['publisher']
        keyword = request.form['keyword']
        results =  nf.getNews(publisher, keyword) # Call the API and get articles
        return render_template('result.html', results=results)
    else: # GET request, do nothing here
        return "Go back to the home page to search for articles!"
if __name__ == '__main__':
    	app.run(debug=True)

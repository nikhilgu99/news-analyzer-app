import flask
from flask import render_template, request

app = flask.Flask(__name__, template_folder="html")
app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home(): # Home page for project 
    return render_template('index.html')

@app.route("/newsfeed", methods=['GET','POST'])
def newsfeed():
    if request.method == 'POST':
        publisher = request.form['publisher']
        keyword = request.form['keyword']
        return publisher + " | " + keyword # Call the API and get articles
    else: # GET request, do nothing here
        return "Go back to the home page to search for articles!"

app.run()
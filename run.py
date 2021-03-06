import flask
import news as nf
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
        results = nf.getNews(publisher, keyword) # Call the API and get articles
        if results == "none":
            return "No articles found!"
        else:
            return render_template('result.html', results=results[0], os=results[1])
    else: # GET request, do nothing here
        return "Go back to the home page to search for articles!"

app.run(host="0.0.0.0", port=5000)
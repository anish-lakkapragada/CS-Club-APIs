from flask import Flask, request 
import requests 

app = Flask(__name__)

@app.route("/")
def default(): 
    return "hello APIs"

@app.route("/resource1")
def resource1(): 
    name = request.args.get("name")
    return f"hello {name}"

@app.route("/wikipediaWrap")
def wrap(): 
    titles = request.args.get("title")
    response = requests.get("http://en.wikipedia.org/w/api.php", {"action" : "query", "titles": titles, "format": "json"})
    if (response.status_code != 200): 
        return "bozo"
    return response.json()


app.run(debug=True)
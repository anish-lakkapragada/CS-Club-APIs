from flask import Flask, request 
import requests

app = Flask(__name__)

@app.route("/")
def default(): 
    return "Hello APIs"

@app.route("/pageid")
def pageid(): 
    page = request.args.get("page")
    response = requests.get("http://en.wikipedia.org/w/api.php", {"format": "json", "action": "query", "titles": page})
    json = response.json()
    return json

app.run(debug=True)
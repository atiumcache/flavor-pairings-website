from flask import Flask, render_template
from csvToDict import csvToDict

app = Flask(__name__)

ingredientPairings = csvToDict('flavor_bible_full.csv')

@app.route("/")
def index():
    pairings = ingredientPairings.get('CINNAMON')
    return render_template("index.html", pairings=pairings)
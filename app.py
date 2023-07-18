from flask import Flask, render_template
import csvToDict

app = Flask(__name__)

ingredientPairings = csvToDict('flavor_bible_full.csv')

@app.route("/")
def index():
    return render_template("index.html")
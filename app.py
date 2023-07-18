from flask import Flask, render_template, request
from csvToDict import csvToDict

app = Flask(__name__)

ingredientPairings = csvToDict('flavor_bible_full.csv')


@app.route("/")
def index():
    main = 'blackberries'
    pairings = ingredientPairings.get(main)
    allMains = list(ingredientPairings.keys())
    return render_template("index.html", pairings=pairings, main=main.capitalize(), allMains=allMains)


@app.route("/results")
def results():
    main = request.args.get("choice")
    pairings = ingredientPairings.get(main.lower())
    allMains = list(ingredientPairings.keys())
    return render_template("results.html", pairings=pairings, main=main, allMains=allMains)
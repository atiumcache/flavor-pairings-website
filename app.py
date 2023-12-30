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

@app.errorhandler(500)
def internalServiceError(error):
    return render_template("error-index.html")

@app.route("/results")
def results():
    try:
        main = request.args.get("choice")
        pairings = ingredientPairings.get(main.lower()) 
        allMains = ingredientPairings.keys()
        return render_template("results.html", pairings=pairings, main=main.capitalize(), allMains=allMains)
    except TypeError:
        return render_template("error-index.html")
    

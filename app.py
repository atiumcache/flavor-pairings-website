from flask import Flask, render_template, request
from csvToDict import csvToDict
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# app.wsgi_app = ProxyFix(
#    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
#)

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
    main = request.args.get("choice")
    pairings = ingredientPairings.get(main.lower())
    allMains = ingredientPairings.keys()
    return render_template("results.html", pairings=pairings, main=main.capitalize(), allMains=allMains)
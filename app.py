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
        pairings_in_fours = convert_pairings_to_list_of_fours(pairings)  
        allMains = ingredientPairings.keys()
        return render_template("results.html", pairings=pairings, main=main.capitalize(), allMains=allMains, pairings_in_fours=pairings_in_fours)
    except TypeError:
        return render_template("error-index.html")
    

def convert_pairings_to_list_of_fours(pairings):
    list_of_fours = [[]]
    counter = 0
    index = 0
    for ing in pairings:
        if counter % 4 == 0:
            list_of_fours.append([])
            index += 1
        
        list_of_fours[index].append(ing)
        counter += 1
    
    return list_of_fours

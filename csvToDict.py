import csv 

def csvToDict(pairingsCSV): 
    """
    Takes in a CSV file of ingredient pairings, and returns
    a dictionary where {'MAIN INGREDIENT': [List of Pairings]}.
    
    CSV file should be in string format.
    """

    ingredientMatches = {}
    with open(pairingsCSV, newline='', encoding='utf8') as csvfile:
        ingredientReader = csv.reader(csvfile)
        pairingList = []
        prevKey = 'ACHIOTE SEEDS'
        badKeywords = ('Season:', 'Techniques:', 'Taste:', 'Volume:', 'Weight:', 'Flavor Aff', 'Botanical rel', 'Tips:', 'Function:')
        for row in ingredientReader: # for each row in the file
            if row[0] != prevKey: # if current main is a new ingredient
                ingredientMatches.update({prevKey.lower(): pairingList}) # update the dictionary with {main: pairing list}
                pairingList = [] # clear the list for new pairings
            if row[1].startswith(badKeywords):
                pass
            else:
                pairingList.append(row[1].lower()) # add the pairing to the pairingList
            prevKey = row[0] # update prevKey to the current main

    return ingredientMatches
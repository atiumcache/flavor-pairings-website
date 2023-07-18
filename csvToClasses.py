"""Take in a CSV file and output a list of ingredient classes."""

class Ingredient:
    """A cooking ingredient."""

    def __init__(self, name, taste, weight, volume, techniques):
        self._name = name
        self._taste = taste
        self._weight = weight
        self._volume = volume
        self._techniques = techniques
        self._pairings = []

    def getPairings(self):
        return self._pairings
    
    
def csvToListOfClasses(): 

    allIngredients = []

    with open(pairingsCSV, newline='', encoding='utf8') as csvfile:
        ingredientReader = csv.reader(csvfile)
        for row in ingredientReader:
            if row[0] not in allIngredients:
                row[0] = Ingredient(row[0], )

            for item in row[1]:
                if item.startswith('Season'):
                    

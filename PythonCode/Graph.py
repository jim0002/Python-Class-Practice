colors = ['Red', 'Green', 'Blue']
colorOfCountries = {}
Countries = ['WA', 'NT', 'SA', 'Q','NSW', 'V', 'T']
MAP = {
  'WA' : ['NT', 'SA'],
  'NT' : ['WA', 'Q' , 'SA'],
  'SA' : ['WA', 'NT','Q', 'NSW', 'V'],
  'Q' : ['NT','SA','NSW'],
  'NSW' : ['Q', 'SA', 'V'],
  'V' : ['NSW', 'SA'],
  'T' : []
}

def check(country , color):
    for neighbour in MAP.get(country):
        colorOfNeighbour = colorOfCountries.get(neighbour)
        if colorOfNeighbour == color:
            return False

    return True

def getColor(country):
    for color in colors:
        if check(country, color):
            return color

for country in Countries:
        colorOfCountries[country] = getColor(country)

print (colorOfCountries)

import json
lista=[('Scrabble0',00),('Scrabble1',00),('Scrabble2',00),('Scrabble3',00),('Scrabble4',00),('Scrabble5',00),('Scrabble6',00),('Scrabble7',00),('Scrabble8',00),('Scrabble9',00)]
archivo = open('TopJugadores.json','w')
json.dump(lista,archivo)
archivo.close()

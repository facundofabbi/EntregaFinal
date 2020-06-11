import PySimpleGUI as sg
from pattern.es import verbs
from random import choice
import json
import remi.gui as gui
from remi import start, App
import remi.server

def Configuracion():
    sg.theme('DarkAmber')
    #self.main_container = gui.VBox(width=300, height=300)

    frame_layout = [
                  [sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],
                  [sg.Radio('FACIL', "ELEGIR", default=True,size=(10,1)), sg.Radio('MEDIO', "ELEGIR",size=(10,1)), sg.Radio('DIFICIL', "ELEGIR",size=(10,1))]
                  ,[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Button('Iniciar',size=(10,1)),sg.Button('Salir',size=(10,1))]
               ]
    columna1 = [
             [sg.Frame('Configuración', frame_layout, font='Any 12', title_color='yellow')],
             ]
    columna2 = [
     [sg.Image(r'foto.gif')]
    ]
    layout = [
[sg.Column(columna1), sg.Column(columna2)]
]


    windows = sg.Window("Scrabble").Layout(layout)
    event, values = windows.Read()
    tupla=()
    if event != None or event != 'Salir':
        if(event =='Iniciar'):
            if values[0] == True:
                tupla = ("Facil", 20)
            if values[1] == True:
                tupla = ("Medio",15)
            if values[2] == True:
                lista = [("VB",10),("JJ",10)]
                tupla = choice(lista)
    windows.close()
    puntaje =  {        "A":[1],
                        "E":[1],
                        "O":[1],
                        "S":[1],
                        "I":[1],
                        "U":[1],
                        "N":[1],
                        "L":[1],
                        "R":[1],
                        "T":[1],
                        "C":[2],
                        "D":[2],
                        "G":[2],
                        "M":[3],
                        "B":[3],
                        "P":[3],
                        "F":[4],
                        "H":[4],
                        "V":[4],
                        "Y":[4],
                        "J":[6],
                        "K":[8],
                        "LL":[8],
                        "Ñ":[8],
                        "Q":[8],
                        "RR":[8],
                        "W":[8],
                        "X":[8],
                        "Z":[10]
                }

    archivo = open ('puntaje_letras.json','w')
    json.dump(puntaje,archivo)
    archivo.close()
    Cant_Letras={   "A": [11],
                    "E": [11],
                    "O": [8],
                    "S": [7],
                    "I": [6],
                    "U": [6],
                    "N": [5],
                    "L": [4],
                    "R": [4],
                    "T": [4],
                    "C": [4],
                    "D": [4],
                    "G": [2],
                    "M": [3],
                    "B": [3],
                    "P": [2],
                    "F": [2],
                    "H": [2],
                    "V": [2],
                    "Y": [1],
                    "J": [5],
                    "K": [1],
                    "LL": [1],
                    # "\u00d1": [1],
                    "Q": [1],
                    "RR": [1],
                    "W": [1],
                    "X": [1],
                    "Z": [1]
                }

    archivo1 = open ('bolsa.json','w')
    json.dump(Cant_Letras,archivo1,indent=1)
    archivo.close()
    return tupla

if __name__ == '__main__':
     Configuracion()

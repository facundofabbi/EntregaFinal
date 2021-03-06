import PySimpleGUI as sg
from pattern.es import verbs
from random import choice
import json
import ActualziarVentana as av

def Configuracion():
    '''Crea la interfaz grafica de la configuracion y retorna los valores elegidos por el jugador. Ademas cofigura la cantidad de fichas en el juego y puntaje de las mismas'''
    sg.theme('DarkAmber')
    #self.main_container = gui.VBox(width=300, height=300)

    frame_layout = [
                  [sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('Usuario:'),sg.Input("Jugador",key='nombre')],[sg.Text('')],
                  [sg.Radio('FACIL', "ELEGIR", default=True,size=(14,1)), sg.Radio('MEDIO', "ELEGIR",size=(14,1)), sg.Radio('DIFICIL', "ELEGIR",size=(14,1))],[sg.Text(' ◦ 10 minutos',size=(17,1)),sg.Text('◦ 7 minutos',size=(17,1)),sg.Text('◦ 5 minutos')],[sg.Text(' ◦ Cualquier palabra',size=(17,1)),sg.Text('◦ Adjetivos y Verbos',size=(17,1)),sg.Text('◦ Adjetivos o Verbos')],
                  [sg.Radio('TABLERO 1', "elegir_tablero", default=True,size=(14,1)), sg.Radio('TABLERO 2', "elegir_tablero",size=(14,1)), sg.Radio('TABLERO 3', "elegir_tablero",size=(14,1))],
                  [sg.Image(r'Imagenes/Tablero_1.png'),sg.Image(r'Imagenes/Tablero_2.png'),sg.Image(r'Imagenes/Tablero_3.png')]
                  ,[sg.Text('')],[sg.Button('Iniciar',size=(10,1)),sg.Button('Salir',size=(10,1)),sg.Button("Reanudar partida"),sg.Button('Top10',size=(10,1))]
               ]
    columna1 = [
             [sg.Frame('Imagenes/Configuración', frame_layout, font='Any 12', title_color='yellow')],
             ]
    columna2 = [
        [sg.Image(r'Imagenes/inicio.png')]    #Referencia a la imagen: https://www.freepik.es/foto-gratis/palabra-inicio-deletrea-letras-madera_4974651.htm#page=1&query=scrabble&position=4
    ]
    layout = [
[sg.Column(columna1), sg.Column(columna2)]
]


    nom=""
    windows = sg.Window("Scrabble").Layout(layout)
    while True:
        event, values = windows.Read()
        tupla=()
        ok=False
        if event=="Reanudar partida":
            ok=True
            archivo11 = open('Almacenamiento/posponerPartida.json','r')
            lista_posponer=json.load(archivo11)
            archivo11.close()
            if lista_posponer !=-1:
                if lista_posponer[14][0]=="Facil":
                    tupla = ("Facil", 20)
                if lista_posponer[14][0]=="Medio":
                    tupla = ("Facil", 20)
                if lista_posponer[14][0]=="Facil":
                    lista = [("VB",10),("JJ",10)]
                    tupla = choice(lista)
                if lista_posponer[13]=="TAB1":
                    nom="TAB1"
                if lista_posponer[13]=="TAB2":
                    nom="TAB2"
                if lista_posponer[13]=="TAB3":
                    nom="TAB3"
            break

        if event == 'Top10':
            av.Top10()
            print(values['nombre'])
            continue

        if event != None or event != 'Salir' and event!="Reanudar partida":
            if(event =='Iniciar'):
                if values[0] == True:
                    tupla = ("Facil", 20)
                if values[1] == True:
                    tupla = ("Medio",15)
                if values[2] == True:
                    lista = [("VB",10),("JJ",10)]
                    tupla = choice(lista)
                if values[3] == True:
                    nom="TAB1"
                if values[4] == True:
                    nom="TAB2"
                if values[5] == True:
                    nom="TAB3"
                break

        if event =='Salir' or event==None:
            return tupla,ok,False


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

    archivo = open ('Almacenamiento/puntaje_letras.json','w')
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

    archivo1 = open ('Almacenamiento/bolsa.json','w')
    json.dump(Cant_Letras,archivo1,indent=1)
    archivo.close()
    windows.close()
    return tupla,ok,True,values['nombre'],nom
if __name__ == '__main__':
     Configuracion()

import PySimpleGUI as sg
from string import ascii_uppercase as up
from random import choice
import json

tam1=8,2
tam=3,2
tamm=9,2
tamanio=4,2
Check_delete = lambda x,y,g : g.TKCanvas.delete(x * tam_celda + 12, y * tam_celda + 11)
Check_box = lambda x,y,g,matriz : g.TKCanvas.itemconfig(matriz[y][x],fill="red")
Uncheck_box = lambda x,y,g,matriz: g.TKCanvas.itemconfig(matriz[y][x],fill="#1D8F64")
despintar = lambda x,g: g.TKCanvas.itemconfig(x, fill="brown")

def Check_button(x,window):
    window.FindElement(x).Update(button_color=('black','#2C3E50 '))
def Uncheck_button(x,window):
    window.FindElement(x).Update(button_color=('black','#ABB2B9'))
def Check_boton(x,window):
    window.FindElement(x).Update(button_color=('black','#FF8453'))
def Uncheck_boton(x,window):
    window.FindElement(x).Update(button_color=('black','#FEEFBA'))
botonMaquina = lambda name,key : sg.Button(button_text=name,button_color=('black','#FEEFBA'),size=tamanio,key=key,disabled = True)
botonb = lambda name,key : sg.Button(button_text=name,button_color=('black','#FEEFBA'),size=tamanio,key=key)
botonc = lambda name,key,booleanito : sg.Button(button_text=name,button_color=('black','#044880'),size=tam,disabled=booleanito,key=key)


def tablero(jugador,tab_Ejecucuon):
    '''creamos el tablero
    es importante tener en cuenta q las 3 matrices son fundamentales'''
    a=jugador.get_atril()
    tam_celda =tab_Ejecucuon.get_tam_Celda()
    color_button = ('black','#FEEFBA')
    tam_button = 17,5
    tamanio=4,2
    button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
    sg.theme('Darkbrown5')
    columna_2 = [ [botonMaquina('','-7'),botonMaquina('','-1'),botonMaquina('','-2'),botonMaquina('','-3'),botonMaquina('','-4'),botonMaquina('','-5'),botonMaquina('','-6')],
    [sg.Graph((550,550),(0,240),(240,0), key='_GRAPH_', background_color='#1D8F64',change_submits=True, drag_submits=False)],


    [botonb(a[0],"boton0"),botonb(a[1],"boton1"),botonb(a[2],"boton2"),botonb(a[3],"boton3"),botonb(a[4],"boton4"),botonb(a[5],"boton5"),botonb(a[6],"boton6"),sg.Text("                               "),sg.Button("Paso Turno",button_color=('black','#ABB2B9'),size=tamm,key="paso")],
    [sg.Button("Evaluar",button_color=('black','#ABB2B9'),key='ev'),sg.Button("Cambio Letras",button_color=('black','#ABB2B9'))]]
    columna_1 = [ [sg.Text('TIEMPO')],[sg.Text(size=(8,2), font=('Helvetica', 20), key ='tiempo')],
    [ sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_1', background_color="#727CF0",change_submits=True, drag_submits=False),sg.Text("Triplica Letra"),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_2', background_color="#FFA07A",change_submits=True, drag_submits=False),sg.Text("Duplica Letra") ],
    [sg.Text('MAQUINA',size=(10,0)),sg.Text(size=(4,0),key="puntaje_maquina")],[sg.Listbox([''],key='lista_maquina',size=(20,10))],
    [sg.Text(jugador.get_nombre(),key="n_j",size=(10,0)),sg.Text(size=(4,0),key="puntaje_persona")],[sg.Listbox([''],key='lista_persona',size=(20,10))]]
    columna_3 = [[sg.Text('FICHAS')],
                 [botonc("¿?","1",True),botonc("¿?","2",True),botonc("¿?","3",True),botonc("¿?","4",True),botonc("¿?","5",True),botonc("¿?","6",True),botonc("¿?","7",True),botonc("¿?","8",True),botonc("¿?","9",True)],
                [botonc("¿?","10",True),botonc("¿?","11",True),botonc("¿?","12",True),botonc("¿?","13",True),botonc("¿?","14",True),botonc("¿?","15",True),botonc("¿?","16",True),botonc("¿?","17",True),botonc("¿?","18",True)],
                 [botonc("¿?","19",True),botonc("¿?","20",True),botonc("¿?","21",True),botonc("¿?","22",True),botonc("¿?","23",True),botonc("¿?","24",True),botonc("¿?","25",True),botonc("¿?","26",True),botonc("¿?","27",True)],
                [botonc("¿?","28",True),botonc("¿?","29",True),botonc("¿?","30",True),botonc("¿?","31",True),botonc("¿?","32",True),botonc("¿?","33",True),botonc("¿?","34",True),botonc("¿?","35",True),botonc("¿?","36",True)],
                [botonc("¿?","37",True),botonc("¿?","38",True),botonc("¿?","39",True),botonc("¿?","40",True),botonc("¿?","41",True),botonc("¿?","42",True),botonc("¿?","43",True),botonc("¿?","44",True),botonc("¿?","45",True)],
                [botonc("¿?","46",True),botonc("¿?","47",True),botonc("¿?","48",True),botonc("¿?","49",True),botonc("¿?","50",True),botonc("¿?","51",True),botonc("¿?","52",True),botonc("¿?","53",True),botonc("¿?","54",True)],
                [botonc("¿?","55",True),botonc("¿?","56",True),botonc("¿?","57",True),botonc("¿?","58",True),botonc("¿?","59",True),botonc("¿?","60",True),botonc("¿?","61",True),botonc("¿?","62",True),botonc("¿?","63",True)],
                [botonc("¿?","64",True),botonc("¿?","65",True),botonc("¿?","66",True),botonc("¿?","67",True),botonc("¿?","68",True),botonc("¿?","69",True),botonc("¿?","70",True),botonc("¿?","71",True),botonc("¿?","72",True)],
                [botonc("¿?","73",True),botonc("¿?","74",True),botonc("¿?","75",True),botonc("¿?","76",True),botonc("¿?","77",True),botonc("¿?","78",True),botonc("¿?","79",True),botonc("¿?","80",True),botonc("¿?","81",True)],
                [botonc("¿?","82",True),botonc("¿?","83",True),botonc("¿?","84",True),botonc("¿?","85",True),botonc("¿?","86",True),botonc("¿?","87",True),botonc("¿?","88",True),botonc("¿?","89",True)],
                [sg.Text('')],
                [sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_6', background_color="#092F50",change_submits=True, drag_submits=False),sg.Text('Fichas usadas.')],
                [sg.Text('')],
                [sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_6', background_color="#044880",change_submits=True, drag_submits=False),sg.Text('Fichas disponibles.'),sg.Text('')],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Instrucciones",button_color=("white","#0D4E83"),key="inst")],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Posponer",button_color=("white","#0D4E83"))],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Fin del Juego",button_color=("white","#0D4E83"))]]




    #Armo el diseño de la interface
    diseño = [
    [sg.Column(columna_1), sg.Column(columna_2),sg.Column(columna_3)]
    ]




    # layout=[columna1,columna2]
    window = sg.Window('pruebaagus', ).Layout(diseño).Finalize()
    g = window.FindElement('_GRAPH_')
    matriz=tab_Ejecucuon.get_matriz()
    for row in range(15):
            for col in range(15):
                matriz[row][col]=g.DrawRectangle((col * tam_celda + 6, row * tam_celda + 6),                     #hacemos las lineas negras de cada rectangulo
                                                (col * tam_celda + tam_celda +6, row * tam_celda + tam_celda + 6),
                                                line_color='black')

    text_box=tab_Ejecucuon.get_text_box()
    dicc=__pintar(g,matriz,text_box)
    tab_Ejecucuon.set_matriz(matriz)
    tab_Ejecucuon.set_text_box(text_box)
    tab_Ejecucuon.set_Casilleros_Especiales(dicc)
    return window,g


def __pintar(g,matriz,text_box):
    ''' esto pinta los cuadrados'''
    grupo=[]
    grupo1=[]
    tam_celda =15
    for i in range(0,15):
        grupo.append((i,i))
    num=14
    for i in range (0,15):
        grupo1.append((i,num))
        num=num-1

    for i in range(len(grupo)):
        g.TKCanvas.itemconfig(matriz[grupo[i][0]][grupo[i][1]], fill="#FFA07A")
        text_box[grupo[i][0]][grupo[i][1]]= g.DrawText("", (grupo[i][1] * tam_celda + 12, grupo[i][0]* tam_celda + 11))
    for i in range(len(grupo1)):
        g.TKCanvas.itemconfig(matriz[grupo1[i][1]][grupo1[i][0]], fill="#FFA07A")
        text_box[grupo1[i][0]][grupo1[i][1]]= g.DrawText("", (grupo1[i][1] * tam_celda + 12, grupo1[i][0]* tam_celda + 11))
    dicc={}
    for i in grupo:
        dicc[i]="DP"
    for i in grupo1:
        dicc[i]="DP"

    g.TKCanvas.itemconfig(matriz[4][0], fill="#727CF0")
    dicc[(4,0)]="TP"
    g.TKCanvas.itemconfig(matriz[5][1], fill="#727CF0")
    dicc[(5,1)]="TP"
    g.TKCanvas.itemconfig(matriz[6][2], fill="#727CF0")
    dicc[(6,2)]="TP"
    g.TKCanvas.itemconfig(matriz[7][3], fill="#727CF0")
    dicc[(7,3)]="TP"
    g.TKCanvas.itemconfig(matriz[8][2], fill="#727CF0")
    dicc[(8,2)]="TP"
    g.TKCanvas.itemconfig(matriz[9][1], fill="#727CF0")
    dicc[(9,1)]="TP"
    g.TKCanvas.itemconfig(matriz[10][0], fill="#727CF0")
    dicc[(10,0)]="TP"
    g.TKCanvas.itemconfig(matriz[0][4], fill="#727CF0")
    dicc[(0,4)]="TP"
    g.TKCanvas.itemconfig(matriz[1][5], fill="#727CF0")
    dicc[(1,5)]="TP"
    g.TKCanvas.itemconfig(matriz[2][6], fill="#727CF0")
    dicc[(2,6)]="TP"
    g.TKCanvas.itemconfig(matriz[3][7], fill="#727CF0")
    dicc[(3,7)]="TP"
    g.TKCanvas.itemconfig(matriz[2][8], fill="#727CF0")
    dicc[(2,8)]="TP"
    g.TKCanvas.itemconfig(matriz[1][9], fill="#727CF0")
    dicc[(1,9)]="TP"
    g.TKCanvas.itemconfig(matriz[0][10], fill="#727CF0")
    dicc[(0,10)]="TP"
    # Otra Flecha
    g.TKCanvas.itemconfig(matriz[14][4], fill="#727CF0")
    dicc[(14,4)]="TP"
    g.TKCanvas.itemconfig(matriz[13][5], fill="#727CF0")
    dicc[(13,5)]="TP"
    g.TKCanvas.itemconfig(matriz[12][6], fill="#727CF0")
    dicc[(12,6)]="TP"
    g.TKCanvas.itemconfig(matriz[11][7], fill="#727CF0")
    dicc[(11,7)]="TP"
    g.TKCanvas.itemconfig(matriz[12][8], fill="#727CF0")
    dicc[(12,8)]="TP"
    g.TKCanvas.itemconfig(matriz[13][9], fill="#727CF0")
    dicc[(13,9)]="TP"
    g.TKCanvas.itemconfig(matriz[14][10], fill="#727CF0")
    dicc[(14,10)]="TP"
    #  otra fleacha
    g.TKCanvas.itemconfig(matriz[4][14], fill="#727CF0")
    dicc[(4,14)]="TP"
    g.TKCanvas.itemconfig(matriz[5][13], fill="#727CF0")
    dicc[(5,13)]="TP"
    g.TKCanvas.itemconfig(matriz[6][12], fill="#727CF0")
    dicc[(6,12)]="TP"

    g.TKCanvas.itemconfig(matriz[7][11], fill="#727CF0")
    dicc[(7,11)]="TP"

    dicc[(8,12)]="TP"
    g.TKCanvas.itemconfig(matriz[8][12], fill="#727CF0")
    g.TKCanvas.itemconfig(matriz[9][13], fill="#727CF0")
    dicc[(9,13)]="TP"
    g.TKCanvas.itemconfig(matriz[10][14], fill="#727CF0")
    dicc[(10,14)]="TP"
    return dicc

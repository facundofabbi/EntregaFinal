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
botonMaquina = lambda name,key : sg.Button(button_text=name,button_color=('black','#044880'),size=tamanio,key=key,disabled = True)
botonb = lambda name,key : sg.Button(button_text=name,button_color=('black','#FEEFBA'),size=tamanio,key=key)
botonc = lambda name,key,booleanito : sg.Button(button_text=name,button_color=('black','#044880'),size=tam,disabled=booleanito,key=key)


def tablero(jugador,tab_Ejecucuon,tablero):
    '''Creamos la iterfaz grafica del tablero y todos los componentes necesarios para el funcionamiento del mismo'''
    a=jugador.get_atril()
    tam_celda =tab_Ejecucuon.get_tam_Celda()
    color_button = ('black','#FEEFBA')
    tam_button = 17,5
    tamanio=4,2
    button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
    sg.theme('DarkGreen3')   #verde Dark Green 3    , DarkBlue13   ,DarkBlue14   , DarkBrown1 , DarkBrown2  , DarkGrey4 Kayak , Topanga


    columna_2 = [ [botonMaquina('','m1'),botonMaquina('','m2'),botonMaquina('','m3'),botonMaquina('','m4'),botonMaquina('','m5'),botonMaquina('','m6'),botonMaquina('','m7')],
    [sg.Graph((550,550),(0,240),(240,0), key='_GRAPH_', background_color='#1D8F64',change_submits=True, drag_submits=False)],


    [botonb(a[0],"boton0"),botonb(a[1],"boton1"),botonb(a[2],"boton2"),botonb(a[3],"boton3"),botonb(a[4],"boton4"),botonb(a[5],"boton5"),botonb(a[6],"boton6"),sg.Text("                               "),sg.Button("Paso Turno",button_color=('black','#ABB2B9'),size=tamm,key="paso")],
    [sg.Button("Evaluar",button_color=('black','#ABB2B9'),key='ev'),sg.Button("Cambio Letras",button_color=('black','#ABB2B9'),key="Cambio Letras")]]
    columna_1 = [ [sg.Text('TIEMPO')],[sg.Text(size=(8,2), font=('Helvetica', 20), key ='tiempo')],
    [ sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_6', background_color="#727CF0",change_submits=True, drag_submits=False),sg.Text("Triplica Letra"),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_7', background_color="#FFA07A",change_submits=True, drag_submits=False),sg.Text("Duplica Letra")],
    [sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_10', background_color="#E33A3A",change_submits=True, drag_submits=False),sg.Text("Resta puntos"),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_10', background_color="#CA4982",change_submits=True, drag_submits=False),sg.Text("Inicio") ],#"#CA4982"
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
                [sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_8', background_color="#092F50",change_submits=True, drag_submits=False),sg.Text('Fichas usadas.')],
                [sg.Text('')],
                [sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_9', background_color="#044880",change_submits=True, drag_submits=False),sg.Text('Fichas disponibles.'),sg.Text('')],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Instrucciones",button_color=("white","#0D4E83"),key="inst")],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Posponer",button_color=("white","#0D4E83"))],
                [sg.Text('                                                       '),sg.Text(''),sg.Text(''),sg.Text(''),sg.Button("Fin del Juego",button_color=("white","#0D4E83"))]]




    #Armo el diseño de la interface
    diseño = [
    [sg.Column(columna_1), sg.Column(columna_2),sg.Column(columna_3)]
    ]




    # layout=[columna1,columna2]
    window = sg.Window('Scrabble', ).Layout(diseño).Finalize()
    g = window.FindElement('_GRAPH_')
    matriz=tab_Ejecucuon.get_matriz()
    for row in range(15):
            for col in range(15):
                matriz[row][col]=g.DrawRectangle((col * tam_celda + 6, row * tam_celda + 6),                     #hacemos las lineas negras de cada rectangulo
                                                (col * tam_celda + tam_celda +6, row * tam_celda + tam_celda + 6),
                                                line_color='black')

    text_box=tab_Ejecucuon.get_text_box()
    dicc={}
    if tablero=="TAB1":
        dicc=__pintar1(g,matriz,text_box)
    if tablero=="TAB2":
        dicc=__pintar2(g,matriz,text_box)
    if tablero=="TAB3":
        dicc=__pintar3(g,matriz,text_box)
    tab_Ejecucuon.set_matriz(matriz)
    tab_Ejecucuon.set_text_box(text_box)
    tab_Ejecucuon.set_Casilleros_Especiales(dicc)
    return window,g

def poner_tp(x,y,g,matriz,dicc):
    g.TKCanvas.itemconfig(matriz[x][y], fill="#727CF0")
    dicc[(x,y)]="TP"

def poer_rs(x,y,g,matriz,dicc):
    g.TKCanvas.itemconfig(matriz[x][y], fill="#E33A3A")
    dicc[(x,y)]="RS"

def poner_duplica(x,y,g,matriz,dicc):
    g.TKCanvas.itemconfig(matriz[x][y], fill="#FFA07A")
    dicc[(x,y)]="DP"

def __pintar1(g,matriz,text_box):
    ''' Pinta los cuadros de los casilleros especiales'''
    dicc={}
    g.TKCanvas.itemconfig(matriz[7][7], fill="#CA4982")

    poner_duplica(0,0,g,matriz,dicc)
    poner_duplica(1,1,g,matriz,dicc)
    poner_duplica(2,2,g,matriz,dicc)
    poner_duplica(3,3,g,matriz,dicc)
    poner_duplica(4,4,g,matriz,dicc)
    poner_duplica(5,5,g,matriz,dicc)
    poner_duplica(6,6,g,matriz,dicc)
    poner_duplica(8,8,g,matriz,dicc)
    poner_duplica(9,9,g,matriz,dicc)
    poner_duplica(10,10,g,matriz,dicc)
    poner_duplica(11,11,g,matriz,dicc)
    poner_duplica(12,12,g,matriz,dicc)
    poner_duplica(13,13,g,matriz,dicc)
    poner_duplica(14,14,g,matriz,dicc)
    poner_duplica(14,0,g,matriz,dicc)
    poner_duplica(13,1,g,matriz,dicc)
    poner_duplica(12,2,g,matriz,dicc)
    poner_duplica(11,3,g,matriz,dicc)
    poner_duplica(10,4,g,matriz,dicc)
    poner_duplica(9,5,g,matriz,dicc)
    poner_duplica(8,6,g,matriz,dicc)
    poner_duplica(6,8,g,matriz,dicc)
    poner_duplica(5,9,g,matriz,dicc)
    poner_duplica(4,10,g,matriz,dicc)
    poner_duplica(3,11,g,matriz,dicc)
    poner_duplica(2,12,g,matriz,dicc)
    poner_duplica(1,13,g,matriz,dicc)
    poner_duplica(0,14,g,matriz,dicc)


    poer_rs(7,0,g,matriz,dicc)
    poer_rs(0,7,g,matriz,dicc)
    poer_rs(14,7,g,matriz,dicc)
    poer_rs(7,14,g,matriz,dicc)


    poner_tp(4,0,g,matriz,dicc)
    poner_tp(5,1,g,matriz,dicc)
    poner_tp(6,2,g,matriz,dicc)
    poner_tp(7,3,g,matriz,dicc)
    poner_tp(8,2,g,matriz,dicc)
    poner_tp(9,1,g,matriz,dicc)
    poner_tp(10,0,g,matriz,dicc)
    poner_tp(0,4,g,matriz,dicc)
    poner_tp(1,5,g,matriz,dicc)
    poner_tp(2,6,g,matriz,dicc)
    poner_tp(3,7,g,matriz,dicc)
    poner_tp(2,8,g,matriz,dicc)
    poner_tp(1,9,g,matriz,dicc)
    poner_tp(0,10,g,matriz,dicc)
    poner_tp(14,4,g,matriz,dicc)
    poner_tp(13,5,g,matriz,dicc)
    poner_tp(12,6,g,matriz,dicc)
    poner_tp(11,7,g,matriz,dicc)
    poner_tp(12,8,g,matriz,dicc)
    poner_tp(13,9,g,matriz,dicc)
    poner_tp(14,10,g,matriz,dicc)
    poner_tp(4,14,g,matriz,dicc)
    poner_tp(5,13,g,matriz,dicc)
    poner_tp(6,12,g,matriz,dicc)
    poner_tp(7,11,g,matriz,dicc)
    poner_tp(8,12,g,matriz,dicc)
    poner_tp(9,13,g,matriz,dicc)
    poner_tp(10,14,g,matriz,dicc)
    return dicc


def __pintar2(g,matriz,text_box):
    ''' Pinta los cuadros de los casilleros especiales'''
    dicc={}

    g.TKCanvas.itemconfig(matriz[7][7], fill="#CA4982")

    poner_duplica(3,0,g,matriz,dicc)
    poner_duplica(2,1,g,matriz,dicc)
    poner_duplica(4,1,g,matriz,dicc)
    poner_duplica(1,2,g,matriz,dicc)
    poner_duplica(5,2,g,matriz,dicc)
    poner_duplica(0,3,g,matriz,dicc)
    poner_duplica(6,3,g,matriz,dicc)
    poner_duplica(1,4,g,matriz,dicc)
    poner_duplica(5,4,g,matriz,dicc)
    poner_duplica(2,5,g,matriz,dicc)
    poner_duplica(4,5,g,matriz,dicc)
    poner_duplica(3,6,g,matriz,dicc)
    poner_duplica(11,8,g,matriz,dicc)
    poner_duplica(10,9,g,matriz,dicc)
    poner_duplica(12,9,g,matriz,dicc)
    poner_duplica(9,10,g,matriz,dicc)
    poner_duplica(13,10,g,matriz,dicc)
    poner_duplica(8,11,g,matriz,dicc)
    poner_duplica(14,11,g,matriz,dicc)
    poner_duplica(9,12,g,matriz,dicc)
    poner_duplica(13,12,g,matriz,dicc)
    poner_duplica(10,13,g,matriz,dicc)
    poner_duplica(12,13,g,matriz,dicc)
    poner_duplica(11,14,g,matriz,dicc)

    poer_rs(7,0,g,matriz,dicc)
    poer_rs(0,7,g,matriz,dicc)
    poer_rs(14,7,g,matriz,dicc)
    poer_rs(7,14,g,matriz,dicc)
    poer_rs(3,3,g,matriz,dicc)
    poer_rs(11,3,g,matriz,dicc)
    poer_rs(11,11,g,matriz,dicc)
    poer_rs(3,11,g,matriz,dicc)


    poner_tp(11,0,g,matriz,dicc)
    poner_tp(10,1,g,matriz,dicc)
    poner_tp(12,1,g,matriz,dicc)
    poner_tp(9,2,g,matriz,dicc)
    poner_tp(13,2,g,matriz,dicc)
    poner_tp(8,3,g,matriz,dicc)
    poner_tp(14,3,g,matriz,dicc)
    poner_tp(9,4,g,matriz,dicc)
    poner_tp(13,4,g,matriz,dicc)
    poner_tp(10,5,g,matriz,dicc)
    poner_tp(12,5,g,matriz,dicc)
    poner_tp(11,6,g,matriz,dicc)
    poner_tp(3,8,g,matriz,dicc)
    poner_tp(2,9,g,matriz,dicc)
    poner_tp(4,9,g,matriz,dicc)
    poner_tp(1,10,g,matriz,dicc)
    poner_tp(5,10,g,matriz,dicc)
    poner_tp(6,11,g,matriz,dicc)
    poner_tp(0,11,g,matriz,dicc)
    poner_tp(5,12,g,matriz,dicc)
    poner_tp(1,12,g,matriz,dicc)
    poner_tp(4,13,g,matriz,dicc)
    poner_tp(2,13,g,matriz,dicc)
    poner_tp(3,14,g,matriz,dicc)
    return dicc

def __pintar3(g,matriz,text_box):
    ''' Pinta los cuadros de los casilleros especiales'''
    dicc={}
    g.TKCanvas.itemconfig(matriz[7][7], fill="#CA4982")

    poner_duplica(8,5,g,matriz,dicc)
    poner_duplica(9,6,g,matriz,dicc)
    poner_duplica(13,8,g,matriz,dicc)
    poner_duplica(12,9,g,matriz,dicc)
    poner_duplica(11,10,g,matriz,dicc)
    poner_duplica(10,11,g,matriz,dicc)
    poner_duplica(9,12,g,matriz,dicc)
    poner_duplica(8,13,g,matriz,dicc)
    poner_duplica(7,14,g,matriz,dicc)
    poner_duplica(6,13,g,matriz,dicc)
    poner_duplica(5,12,g,matriz,dicc)
    poner_duplica(4,11,g,matriz,dicc)
    poner_duplica(3,10,g,matriz,dicc)
    poner_duplica(2,9,g,matriz,dicc)
    poner_duplica(1,8,g,matriz,dicc)
    poner_duplica(7,4,g,matriz,dicc)
    poner_duplica(10,7,g,matriz,dicc)

    poer_rs(2,0,g,matriz,dicc)
    poer_rs(1,1,g,matriz,dicc)
    poer_rs(0,2,g,matriz,dicc)
    poer_rs(12,0,g,matriz,dicc)
    poer_rs(13,1,g,matriz,dicc)
    poer_rs(14,2,g,matriz,dicc)
    poer_rs(14,12,g,matriz,dicc)
    poer_rs(13,13,g,matriz,dicc)
    poer_rs(12,14,g,matriz,dicc)
    poer_rs(0,12,g,matriz,dicc)
    poer_rs(1,13,g,matriz,dicc)
    poer_rs(2,14,g,matriz,dicc)
    poer_rs(6,5,g,matriz,dicc)
    poer_rs(5,6,g,matriz,dicc)
    poer_rs(9,8,g,matriz,dicc)
    poer_rs(8,9,g,matriz,dicc)

    poner_tp(4,7,g,matriz,dicc)
    poner_tp(7,10,g,matriz,dicc)
    poner_tp(14,7,g,matriz,dicc)
    poner_tp(13,6,g,matriz,dicc)
    poner_tp(12,5,g,matriz,dicc)
    poner_tp(11,4,g,matriz,dicc)
    poner_tp(10,3,g,matriz,dicc)
    poner_tp(9,2,g,matriz,dicc)
    poner_tp(8,1,g,matriz,dicc)
    poner_tp(6,1,g,matriz,dicc)
    poner_tp(5,2,g,matriz,dicc)
    poner_tp(4,3,g,matriz,dicc)
    poner_tp(3,4,g,matriz,dicc)
    poner_tp(2,5,g,matriz,dicc)
    poner_tp(1,6,g,matriz,dicc)
    poner_tp(0,7,g,matriz,dicc)
    poner_tp(5,8,g,matriz,dicc)
    poner_tp(6,9,g,matriz,dicc)
    poner_tp(7,0,g,matriz,dicc)
    return dicc

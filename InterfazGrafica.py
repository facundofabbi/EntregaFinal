import PySimpleGUI as sg
from string import ascii_uppercase as up
from random import choice
import json

tamanio=4,2
Check_delete = lambda x,y,g : g.TKCanvas.delete(x * tam_celda + 12, y * tam_celda + 11)
Check_box = lambda x,y,g,matriz : g.TKCanvas.itemconfig(matriz[y][x])
Uncheck_box = lambda x,y,g,matriz: g.TKCanvas.itemconfig(matriz[y][x])
despintar = lambda x,g: g.TKCanvas.itemconfig(x, fill="brown")

Check_button = lambda x: window.FindElement(x).Update(button_color=('white','blue'))
Uncheck_button = lambda x: window.FindElement(x).Update(button_color=('black','grey'))
Check_buttonRed = lambda x,window: window.FindElement(x).Update(button_color=('white','green'))
botonb = lambda name,key : sg.Button(button_text=name,button_color=('white','green'),size=tamanio,key=key)

def tablero(jugador,tab_Ejecucuon):
    '''creamos el tablero
    es importante tener en cuenta q las 3 matrices son fundamentales'''
    a=jugador.get_atril()
    tam_celda =tab_Ejecucuon.get_tam_Celda()
    color_button = ('white','green')
    tam_button = 17,5
    tamanio=4,2
    button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
    sg.theme('DarkBrown2')
    layout = [
            [sg.Graph((550,550),(0,240),(240,0), key='_GRAPH_', background_color='brown',change_submits=True, drag_submits=False),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_1', background_color="#2E8B57",change_submits=True, drag_submits=False),sg.Text("Triplica Letra"),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_2', background_color="#66CDAA",change_submits=True, drag_submits=False),sg.Text("Duplica Letra")],


            [botonb(a[0],"boton0"),botonb(a[1],"boton1"),botonb(a[2],"boton2"),botonb(a[3],"boton3"),botonb(a[4],"boton4"),botonb(a[5],"boton5"),botonb(a[6],"boton6")],
            [sg.Button("Evaluar",button_color=('black','grey')),sg.Button("Cambio Letras",button_color=('black','grey'))]]



    # layout=[columna1,columna2]
    window = sg.Window('pruebaagus', ).Layout(layout).Finalize()
    g = window.FindElement('_GRAPH_')
    matriz=tab_Ejecucuon.get_matriz()
    for row in range(15):
            for col in range(15):
                matriz[row][col]=g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3),                     #hacemos las lineas negras de cada rectangulo
                                                (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3),
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
        g.TKCanvas.itemconfig(matriz[grupo[i][0]][grupo[i][1]], fill="#66CDAA")
        text_box[grupo[i][0]][grupo[i][1]]= g.DrawText("", (grupo[i][1] * tam_celda + 12, grupo[i][0]* tam_celda + 11))
    for i in range(len(grupo1)):
        g.TKCanvas.itemconfig(matriz[grupo1[i][1]][grupo1[i][0]], fill="#66CDAA")
        text_box[grupo1[i][0]][grupo1[i][1]]= g.DrawText("", (grupo1[i][1] * tam_celda + 12, grupo1[i][0]* tam_celda + 11))
    dicc={}
    for i in grupo:
        dicc[i]="DP"
    for i in grupo1:
        dicc[i]="DP"

    g.TKCanvas.itemconfig(matriz[4][0], fill="#2E8B57")
    dicc[(4,0)]="TP"
    g.TKCanvas.itemconfig(matriz[5][1], fill="#2E8B57")
    dicc[(5,1)]="TP"
    g.TKCanvas.itemconfig(matriz[6][2], fill="#2E8B57")
    dicc[(6,2)]="TP"
    g.TKCanvas.itemconfig(matriz[7][3], fill="#2E8B57")
    dicc[(7,3)]="TP"
    g.TKCanvas.itemconfig(matriz[8][2], fill="#2E8B57")
    dicc[(8,2)]="TP"
    g.TKCanvas.itemconfig(matriz[9][1], fill="#2E8B57")
    dicc[(9,1)]="TP"
    g.TKCanvas.itemconfig(matriz[10][0], fill="#2E8B57")
    dicc[(10,0)]="TP"
    g.TKCanvas.itemconfig(matriz[0][4], fill="#2E8B57")
    dicc[(0,4)]="TP"
    g.TKCanvas.itemconfig(matriz[1][5], fill="#2E8B57")
    dicc[(1,5)]="TP"
    g.TKCanvas.itemconfig(matriz[2][6], fill="#2E8B57")
    dicc[(2,6)]="TP"
    g.TKCanvas.itemconfig(matriz[3][7], fill="#2E8B57")
    dicc[(3,7)]="TP"
    g.TKCanvas.itemconfig(matriz[2][8], fill="#2E8B57")
    dicc[(2,8)]="TP"
    g.TKCanvas.itemconfig(matriz[1][9], fill="#2E8B57")
    dicc[(1,9)]="TP"
    g.TKCanvas.itemconfig(matriz[0][10], fill="#2E8B57")
    dicc[(0,10)]="TP"
    # Otra Flecha
    g.TKCanvas.itemconfig(matriz[14][4], fill="#2E8B57")
    dicc[(14,4)]="TP"
    g.TKCanvas.itemconfig(matriz[13][5], fill="#2E8B57")
    dicc[(13,5)]="TP"
    g.TKCanvas.itemconfig(matriz[12][6], fill="#2E8B57")
    dicc[(12,6)]="TP"
    g.TKCanvas.itemconfig(matriz[11][7], fill="#2E8B57")
    dicc[(11,7)]="TP"
    g.TKCanvas.itemconfig(matriz[12][8], fill="#2E8B57")
    dicc[(12,8)]="TP"
    g.TKCanvas.itemconfig(matriz[13][9], fill="#2E8B57")
    dicc[(13,9)]="TP"
    g.TKCanvas.itemconfig(matriz[14][10], fill="#2E8B57")
    dicc[(14,10)]="TP"
    #  otra fleacha
    g.TKCanvas.itemconfig(matriz[4][14], fill="#2E8B57")
    dicc[(4,14)]="TP"
    g.TKCanvas.itemconfig(matriz[5][13], fill="#2E8B57")
    dicc[(5,13)]="TP"
    g.TKCanvas.itemconfig(matriz[6][12], fill="#2E8B57")
    dicc[(6,12)]="TP"

    g.TKCanvas.itemconfig(matriz[7][11], fill="#2E8B57")
    dicc[(7,11)]="TP"

    dicc[(8,12)]="TP"
    g.TKCanvas.itemconfig(matriz[8][12], fill="#2E8B57")
    g.TKCanvas.itemconfig(matriz[9][13], fill="#2E8B57")
    dicc[(9,13)]="TP"
    g.TKCanvas.itemconfig(matriz[10][14], fill="#2E8B57")
    dicc[(10,14)]="TP"
    return dicc

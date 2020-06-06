import PySimpleGUI as sg
from string import ascii_uppercase as up
from random import choice
import json


tam_celda =15
tamanio=4,2
Check_delete = lambda x,y,g : g.TKCanvas.delete(x * tam_celda + 12, y * tam_celda + 11)
Check_box = lambda x,y,g,matriz : g.TKCanvas.itemconfig(matriz[y][x])
Uncheck_box = lambda x,y,g,matriz: g.TKCanvas.itemconfig(matriz[y][x])
despintar = lambda x,g: g.TKCanvas.itemconfig(x, fill="brown")

Check_button = lambda x: window.FindElement(x).Update(button_color=('white','blue'))
Uncheck_button = lambda x: window.FindElement(x).Update(button_color=('black','grey'))
Check_buttonRed = lambda x,window: window.FindElement(x).Update(button_color=('white','green'))
botonb = lambda name,key : sg.Button(button_text=name,button_color=('white','green'),size=tamanio,key=key)


def tablero(jugador):
    '''creamos el tablero
    es importante tener en cuenta q las 3 matrices son fundamentales'''
    a=jugador.get_Tablero_Actual()
    tam_celda =15
    color_button = ('white','green')
    tam_button = 17,5
    button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
    sg.theme('DarkBrown2')
    layout = [
            [sg.Graph((550,550),(0,240),(240,0), key='_GRAPH_', background_color='brown',change_submits=True, drag_submits=False),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_1', background_color="#2E8B57",change_submits=True, drag_submits=False),sg.Text("Triplica Letra"),sg.Graph((25,25),(0,10),(10,0), key='_GRAPH_2', background_color="#66CDAA",change_submits=True, drag_submits=False),sg.Text("Duplica Letra")],


            [botonb(a[0],"boton0"),botonb(a[1],"boton1"),botonb(a[2],"boton2"),botonb(a[3],"boton3"),botonb(a[4],"boton4"),botonb(a[5],"boton5"),botonb(a[6],"boton6")],
            [sg.Button("Evaluar",button_color=('black','grey')),sg.Button("Cambio Letras",button_color=('black','grey'))]]



    # layout=[columna1,columna2]
    window = sg.Window('pruebaagus', ).Layout(layout).Finalize()
    g = window.FindElement('_GRAPH_')
    matriz=[]
    selected=[]
    text_box=[]
    for i in range(0,15):
        matriz.append([0]*15)    #dentro del for configuramos todos los cuadrados a usar en el tabero
        selected.append([False]*15)
        text_box.append([""]*15)

    for row in range(15):
            for col in range(15):
                matriz[row][col]=g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3),                     #hacemos las lineas negras de cada rectangulo
                                                (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3),
                                                line_color='black')

    dicc=__pintar(g,matriz,text_box)
    return window,g,matriz,selected,text_box,dicc


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
    text_box[6][2] = g.DrawText("", (2 * tam_celda + 12, 6 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[7][3], fill="#2E8B57")
    dicc[(7,3)]="TP"
    text_box[7][3] = g.DrawText("", (3 * tam_celda + 12, 7* tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[8][2], fill="#2E8B57")
    dicc[(8,2)]="TP"
    text_box[8][2] = g.DrawText("", (2 * tam_celda + 12, 8 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[9][1], fill="#2E8B57")
    dicc[(9,1)]="TP"
    text_box[9][1] = g.DrawText("", (1 * tam_celda + 12, 9 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[10][0], fill="#2E8B57")
    dicc[(10,0)]="TP"
    text_box[10][0] = g.DrawText("", (0 * tam_celda + 12, 10 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[0][4], fill="#2E8B57")
    dicc[(0,4)]="TP"
    text_box[0][4] = g.DrawText("", (4 * tam_celda + 12, 0 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[1][5], fill="#2E8B57")
    dicc[(1,5)]="TP"
    text_box[1][5] = g.DrawText("", (5 * tam_celda + 12, 1 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[2][6], fill="#2E8B57")
    dicc[(2,6)]="TP"
    text_box[2][6] = g.DrawText("", (6 * tam_celda + 12, 2 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[3][7], fill="#2E8B57")
    dicc[(3,7)]="TP"
    text_box[3][7] = g.DrawText("", (7 * tam_celda + 12, 3 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[2][8], fill="#2E8B57")
    dicc[(2,8)]="TP"
    text_box[2][8] = g.DrawText("", (8 * tam_celda + 12, 2 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[1][9], fill="#2E8B57")
    dicc[(1,9)]="TP"
    text_box[1][9] = g.DrawText("", (9 * tam_celda + 12, 1 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[0][10], fill="#2E8B57")
    dicc[(0,10)]="TP"
    text_box[0][10] = g.DrawText("", (10 * tam_celda + 12, 0 * tam_celda + 11))
    # Otra Flecha
    g.TKCanvas.itemconfig(matriz[14][4], fill="#2E8B57")
    dicc[(14,4)]="TP"
    text_box[14][4] = g.DrawText("", (4 * tam_celda + 12, 14* tam_celda + 11))

    g.TKCanvas.itemconfig(matriz[13][5], fill="#2E8B57")
    dicc[(13,5)]="TP"
    text_box[13][5] = g.DrawText("", (5 * tam_celda + 12, 13 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[12][6], fill="#2E8B57")
    dicc[(12,6)]="TP"
    text_box[12][6] = g.DrawText("", (6 * tam_celda + 12, 12 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[11][7], fill="#2E8B57")
    dicc[(11,7)]="TP"
    text_box[11][7] = g.DrawText("", (7 * tam_celda + 12, 11 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[12][8], fill="#2E8B57")
    dicc[(12,8)]="TP"
    text_box[12][8] = g.DrawText("", (8 * tam_celda + 12, 12 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[13][9], fill="#2E8B57")
    dicc[(13,9)]="TP"
    text_box[13][9] = g.DrawText("", (9 * tam_celda + 12, 13 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[14][10], fill="#2E8B57")
    dicc[(14,10)]="TP"
    text_box[14][10] = g.DrawText("", (10 * tam_celda + 12, 14 * tam_celda + 11))
    #  otra fleacha
    g.TKCanvas.itemconfig(matriz[4][14], fill="#2E8B57")
    dicc[(4,14)]="TP"
    text_box[4][14] = g.DrawText("", (14 * tam_celda + 12, 4* tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[5][13], fill="#2E8B57")
    dicc[(5,13)]="TP"
    text_box[5][13] = g.DrawText("", (13 * tam_celda + 12, 5 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[6][12], fill="#2E8B57")
    dicc[(6,12)]="TP"
    text_box[6][12] = g.DrawText("", (12 * tam_celda + 12, 6 * tam_celda + 11))

    g.TKCanvas.itemconfig(matriz[7][11], fill="#2E8B57")
    dicc[(7,11)]="TP"

    text_box[7][11] = g.DrawText("", (11 * tam_celda + 12, 7 * tam_celda + 11))
    dicc[(8,12)]="TP"
    g.TKCanvas.itemconfig(matriz[8][12], fill="#2E8B57")
    text_box[8][12] = g.DrawText("", (12 * tam_celda + 12, 8 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[9][13], fill="#2E8B57")
    dicc[(9,13)]="TP"
    text_box[9][13] = g.DrawText("", (13 * tam_celda + 12, 9 * tam_celda + 11))
    g.TKCanvas.itemconfig(matriz[10][14], fill="#2E8B57")
    dicc[(10,14)]="TP"
    text_box[10][14] = g.DrawText("", (14 * tam_celda + 12, 10 * tam_celda + 11))
    return dicc

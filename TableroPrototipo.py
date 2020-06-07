import PySimpleGUI as sg
import Configuracion as c
import json
from JugadorScrabble import Jugador
import modulito
import ActualizacionDeVentanaPrototico as av
import LetrasTablero


c.Configuracion()
Llaves=["boton0","boton1","boton2","boton3","boton4","boton5","boton6",]
Jugador1=Jugador(True)
lista=Jugador1.BuscarEnLaBolsa(7)
Jugador1.set_Atril(lista)
tupla=modulito.tablero(Jugador1)
window=tupla[0]
g=tupla[1]
selected=tupla[3]
matriz=tupla[2]
text_box=tupla[4]
dicc=tupla[5]
letra=""
word=""
Antes_usadas=[]
button_selected = False
tam_celda =15
nivel="JJ"
segundaletra=False
DL=LetrasTablero.DireccionLetra()
posicionLetra1=(-20,-20)
while True:
    event, values = window.Read()
    print(values)
    print(event)
    if event is None :
        break
    if event == "Evaluar":
        # if av.EvaluarPalabra(word,"facil"):
        if True:
            Jugador1.Actualizar_Puntaje(av.PuntosPalabra(word,DL))
            av.Post_Evaluamos(window,Jugador1)
        else:
            av.palabra_Invalida(text_box,selected,g,Jugador1,window)
        Jugador1.FinTurno()
        DL.FinTurno()
        word=''
        segundaletra=False
        continue
    if event == "Cambio Letras":
        av.cambiamosLetras(window,Jugador1,event,Llaves)
        continue
    if event == '_GRAPH_':
        if values['_GRAPH_'] == (None,None):
            continue
        mouse = values["_GRAPH_"]
        box_x = mouse[0]//tam_celda
        box_y = mouse[1]//tam_celda
        if  box_x > 14 or box_y > 14:
            continue
        if button_selected: # logica de boton
            if not segundaletra  and selected[box_x][box_y]==False:
                av.EscribirEnTablero(box_x,box_y,g,matriz,selected,text_box,letra,tam_celda,Jugador1)
                DL.chequeroDuplica(box_x,box_y,dicc,letra)
                segundaletra=True
                posicionLetra1=(box_x,box_y)
                word+=letra
                letra=""
                button_selected=False
                continue
            if av.posicionValida(box_x,box_y,posicionLetra1,DL) and segundaletra and selected[box_x][box_y]==False:
                av.EscribirEnTablero(box_x,box_y,g,matriz,selected,text_box,letra,tam_celda,Jugador1)
                DL.chequeroDuplica(box_x,box_y,dicc,letra)
                segundaletra=True
                posicionLetra1=(box_x,box_y)
                word+=letra
                letra=""
                button_selected=False
                continue
            else :
                continue
    else:
        if button_selected:
            continue
        else:
            button_selected=True
            letra=av.tocoBoton(window,Jugador1,event)
            if letra=="":
                button_selected=False
                continue

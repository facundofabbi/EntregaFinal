import PySimpleGUI as sg
import Configuracion as c
import json
from JugadorScrabble import Jugador
import InterfazGrafica as IG
import ActualziarVentana as AV
import TableroEnEjecucion as TE


nivel=c.Configuracion()
Jugador1=Jugador(True)
lista=Jugador1.BuscarEnLaBolsa(7)
Jugador1.set_Atril(lista)
tab_Ejecucuon=TE.Turno()
tupla=IG.tablero(Jugador1,tab_Ejecucuon)
window=tupla[0]
g=tupla[1]
segundaletra=False


while True:
    event, values = window.Read()
    print(values)
    print(event)
    if event is None :
        break
    if event == "Evaluar":
        if tab_Ejecucuon.get_palabra()=="":
            continue
        if AV.EvaluarPalabra(tab_Ejecucuon.get_palabra(),nivel[0])==True:
        #if True:
            Jugador1.Actualizar_Puntaje(AV.PuntosPalabra(tab_Ejecucuon))
            AV.Post_Evaluamos(window,Jugador1,tab_Ejecucuon)
            print(Jugador1.get_puntos_jugador())
        else:
            AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
        Jugador1.FinTurno()
        tab_Ejecucuon.FinTurno()
        segundaletra=False
        continue
    if event == "Cambio Letras":
        AV.cambiamosLetras(window,Jugador1,event,tab_Ejecucuon)
        segundaletra=False
        continue
    if event == '_GRAPH_':
        if values['_GRAPH_'] == (None,None):
            continue
        mouse = values["_GRAPH_"]
        mouse1=mouse[0]-5
        mouse2=mouse[1]-7
        box_x = mouse1//tab_Ejecucuon.get_tam_Celda()
        box_y = mouse2//tab_Ejecucuon.get_tam_Celda()
        if  box_x > 14 or box_y > 14:
            continue
        if Jugador1.get_boton_seleccionado(): # logica de boton
            if not segundaletra  and tab_Ejecucuon.get_selected_posicion(box_x,box_y)==False:
                tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra,Jugador1)
                tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                segundaletra=True
                tab_Ejecucuon.set_posicionLetra1((box_x,box_y))
                tab_Ejecucuon.set_palabra(letra)
                Jugador1.set_letra("")
                Jugador1.set_boton_seleccionado(False)
                continue
            if AV.posicionValida(box_x,box_y,tab_Ejecucuon) and segundaletra and tab_Ejecucuon.get_selected_posicion(box_x,box_y)==False:
                tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra,Jugador1)
                tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                segundaletra=True
                tab_Ejecucuon.set_posicionLetra1((box_x,box_y))
                tab_Ejecucuon.set_palabra(letra)
                Jugador1.set_letra("")
                Jugador1.set_boton_seleccionado(False)
                continue
            else :
                continue
    else:
        if Jugador1.get_boton_seleccionado():
            continue
        else:
            Jugador1.set_boton_seleccionado(True)
            letra=AV.tocoBoton(window,Jugador1,tab_Ejecucuon,event)
            if letra=="":
                button_selected=False
                continue

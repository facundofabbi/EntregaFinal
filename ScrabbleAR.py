import PySimpleGUI as sg
import Configuracion as c
import json
from JugadorScrabble import Jugador
import InterfazGrafica as IG
import ActualziarVentana as AV
import TableroEnEjecucion as TE
from JugadorMaquina import Maquinola


nivel=c.Configuracion()
Jugador1=Jugador(True)
maquina = Maquinola(True)
lista=Jugador1.BuscarEnLaBolsa(7)
Jugador1.set_Atril(lista)


lista=maquina.BuscarEnLaBolsa(7)
maquina.set_Atril(lista)


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
        #if AV.EvaluarPalabra(tab_Ejecucuon.get_palabra(),nivel[0]):
        if True:
            Jugador1.Actualizar_Puntaje(AV.PuntosPalabra(tab_Ejecucuon))
            AV.Post_Evaluamos(window,Jugador1,tab_Ejecucuon)
            print(Jugador1.get_puntos_jugador())
        else:
            AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
        Jugador1.FinTurno()
        window.FindElement("texto").Update(Jugador1.get_puntos_jugador())
        tab_Ejecucuon.FinTurno()
        segundaletra=False
        letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon.get_lista_de_letras_en_tablero())
        print(maquina.get_palabra())
        maquina.evaluar_donde(tab_Ejecucuon,g,letrita)
        maquina.fin_turno()
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
            if not segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y):
                tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra)
                tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                segundaletra=True
                tab_Ejecucuon.set_posicionLetra1((box_x,box_y))
                tab_Ejecucuon.set_palabra(letra)
                Jugador1.set_letra("")
                Jugador1.set_boton_seleccionado(False)
                continue
            if AV.posicionValida(box_x,box_y,tab_Ejecucuon) and segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y):
                tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra)
                tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
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
                Jugador1.set_boton_seleccionado(False)
                continue

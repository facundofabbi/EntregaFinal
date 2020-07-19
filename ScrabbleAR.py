import PySimpleGUI as sg
import Configuracion as c
import json
from JugadorScrabble import Jugador
import InterfazGrafica as IG
import ActualziarVentana as AV
import TableroEnEjecucion as TE
from JugadorMaquina import Maquinola
import Actualizacion_Bolsa as actualizar_columna
import time


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
ab=actualizar_columna.columna(window)
num=1
paso=True
start_time = int(round(time.time()*100))
tiempo_actual = 0
lista_total_persona=[]
lista_total_maquina=[]
while True:
    event, values = window.Read()
    tiempo_actual=int(round(time.time() * 100)) - start_time
    window['tiempo'].update('{:02d}:{:02d}.{:02d}'.format((tiempo_actual // 100) // 60,
                                                        (tiempo_actual // 100) % 60,
                                                        tiempo_actual%100))
    print(values)
    print(event)
    if event=="paso":
        paso=False
        letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
        print("encotnre esta letra:   "+letrita[0])
        print(maquina.get_palabra())
        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
        maquina.fin_turno()
        puntos_maquina = maquina.get_puntos_jugador()
        palabra_y_puntaje_maquina = letrita[1] + ' ' +str(puntos_maquina)
        lista_total_maquina.append(letrita[1])
        window['lista_maquina'].update(values = lista_total_maquina)
        continue


    else :
        paso=True
    if event is None :
        break
    if event == "ev" and paso  and tab_Ejecucuon.get_palabra()!="":
        # if AV.EvaluarPalabra(tab_Ejecucuon.get_palabra(),nivel[0]):
        if True:
            puntos = AV.PuntosPalabra(tab_Ejecucuon)
            palabra = tab_Ejecucuon.get_palabra()
            total = (palabra + ' ' + str(puntos))
            lista_total_persona.append(total)

            Jugador1.Actualizar_Puntaje(puntos)
            AV.Post_Evaluamos(window,Jugador1,tab_Ejecucuon)
            print(Jugador1.get_puntos_jugador())
            window['lista_persona'].update(values = lista_total_persona)
        else:
            AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
        Jugador1.FinTurno()
        window.FindElement("texto").Update(Jugador1.get_puntos_jugador())
        tab_Ejecucuon.FinTurno()
        segundaletra=False
        letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
        print("encotnre esta letra:   "+letrita[0])
        print(maquina.get_palabra())
        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
        maquina.fin_turno()
        print("no quede en bucle infinito")
        puntos_maquina = maquina.get_puntos_jugador()
        palabra_y_puntaje_maquina = letrita[1] + ' ' +str(puntos_maquina)
        lista_total_maquina.append(letrita[1])
        window['lista_maquina'].update(values = lista_total_maquina)
        continue
    if event == 'ev' and tab_Ejecucuon.get_palabra()=='':
        continue
    if event=="inst":
        layout = [
            [sg.Image(r'giphy.gif')],
            [sg.Button("ok",key="ok")]
         ]
        win=sg.Window("Instrucciones").Layout(layout)
        while True :

            e,v=win.read()
            # sg.Image.update_animation_no_buffering(r'giphy.gif')
            # win.FindElement("lu").update_animation_no_buffering('giphy.gif')
            if e== None:
                break
            if e=="ok":
                break
        win.close()
        # sg.popup_animated("giphy.gif",
        # message=None,
        # background_color=None,
        # text_color=None,
        # font=None,
        # no_titlebar=True,
        # grab_anywhere=True,
        # keep_on_top=True,
        # location=(None, None),
        # alpha_channel=None,
        # time_between_frames=0,
        # transparent_color=None,
        # title="",
        # icon=None)
        continue
    if event == "Cambio Letras":
        window.FindElement(event).Update("¡Presioname luego de selecionar todas tus letras a cambiar!.")
        window.FindElement(event).Update(button_color=('white','black'))
        AV.cambiamosLetras(window,Jugador1,event,tab_Ejecucuon,ab)
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

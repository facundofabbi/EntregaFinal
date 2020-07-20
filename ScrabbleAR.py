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


todo=c.Configuracion()
nivel=todo[0]
ok_posponer=todo[1]
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
if ok_posponer:
    lista_posponer=[]
    print("cargando partidda.......")
    archivo1 = open('posponerPartida.json','r')
    lista_posponer=json.load(archivo1)
    archivo1.close()
    tab_Ejecucuon.set_coordenadas_en_tablero_lista(lista_posponer[1])
    tab_Ejecucuon.set_selected(lista_posponer[2])
    tab_Ejecucuon.set_matriz(lista_posponer[3])
    tab_Ejecucuon.set_matrizMultiplica(lista_posponer[4])
    tab_Ejecucuon.set_text_box(lista_posponer[0])
    for x in range(0,15):
        for y in range(0,15):
            tab_Ejecucuon.EscribirEnTableroPosponer(x,y,g)
segundaletra=False
ab=actualizar_columna.columna(window)
start_time = int(round(time.time()*100))
tiempo_actual = 0
lista_total_persona=[]
lista_total_maquina=[]
agrego_letra_del_tablero=   True
while True:
    event, values = window.Read()
    tiempo_actual=int(round(time.time() * 100)) - start_time
    window['tiempo'].update('{:02d}:{:02d}.{:02d}'.format((tiempo_actual // 100) // 60,
                                                        (tiempo_actual // 100) % 60,
                                                        tiempo_actual%100))
    print(values)
    print(event)
    if event=="paso":
        letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
        print("encotnre esta letra:   "+letrita[0])

        print(maquina.get_palabra())
        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
        AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
        ab.set_cant(len(letrita[1]))
        maquina.fin_turno()
        tab_Ejecucuon.FinTurno()
        lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
        AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
        agrego_letra_del_tablero=   True
        continue
    if event is None :
        break
    if event == "ev" and tab_Ejecucuon.get_palabra()!="":
        agrego_letra_del_tablero=   True
        #if AV.EvaluarPalabra(tab_Ejecucuon.get_palabra(),nivel[0]):
        if True:
            palabra = tab_Ejecucuon.get_palabra()
            lista_total_persona.append(Jugador1.Actualizar_Puntaje(AV,tab_Ejecucuon))
            AV.Post_Evaluamos(window,Jugador1,tab_Ejecucuon)
            tab_Ejecucuon.FinTurno()
            AV.roleo_random_fichas(ab.get_keys(),window,len(palabra),ab)
            ab.set_cant(len(palabra))
            AV.VerPuntajeNuevo(lista_total_persona,window,Jugador1)
        else:
            AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
        Jugador1.FinTurno()
        tab_Ejecucuon.FinTurno()
        segundaletra=False
        letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
        print("encotnre esta letra:   "+letrita[0])
        print(maquina.get_palabra())
        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
        maquina.fin_turno()
        puntos_maquina = maquina.get_puntos_jugador()
        lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
        AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
        tab_Ejecucuon.FinTurno()
        AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
        ab.set_cant(len(letrita[1]))
        continue
    if event == 'ev' and tab_Ejecucuon.get_palabra()=='':
        continue
    if event == "Posponer":
        lista_posponer=[]
        archivo = open ('posponerPartida.json','w')
        lista_posponer.append(tab_Ejecucuon.get_text_box())
        lista_posponer.append(tab_Ejecucuon.get_coordenadas_en_tablero_lista())
        lista_posponer.append(tab_Ejecucuon.get_selected())
        lista_posponer.append(tab_Ejecucuon.get_matriz())
        lista_posponer.append(tab_Ejecucuon.get_matrizMultiplica())
        json.dump(lista_posponer,archivo)
        archivo.close()
        sg.popup("La partida sera pospueta para un futuro no muy lejano :D, anda a descansar y veni fresquito para seguire jugando")
        window.close()
    if event=="inst":
        layout = [
            [sg.Image(r'giphy.gif')],
            [sg.Button("ok",key="ok")]
         ]
        win=sg.Window("Instrucciones").Layout(layout)
        while True :

            e,v=win.read()
            if e== None:
                break
            if e=="ok":
                break
        win.close()
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
        print(box_x)
        print(box_y)
        if  box_x > 14 or box_y > 14:
            continue
        if Jugador1.get_boton_seleccionado(): # logica de boton
            if not segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y):
                agrego_letra_del_tablero=AV.CrucePrimerLetra(letra,(box_x,box_y),tab_Ejecucuon)
                tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra)
                tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                segundaletra=True
                tab_Ejecucuon.set_posicionLetra1((box_x,box_y))
                tab_Ejecucuon.set_palabra(letra)
                Jugador1.set_letra("")
                Jugador1.set_boton_seleccionado(False)
                continue
            if AV.posicionValida(box_x,box_y,tab_Ejecucuon) and segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y) :
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

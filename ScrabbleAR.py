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
import Top


todo=c.Configuracion()
if todo[2]:
    nivel=todo[0]
    ok_posponer=todo[1]
    Top = Top.Top()                    #CREO EL Top
    Jugador1=Jugador(todo[3],True)
    maquina = Maquinola(True)
    lista=Jugador1.BuscarEnLaBolsa(7)
    Jugador1.set_Atril(lista)
    lista=maquina.BuscarEnLaBolsa(7)
    maquina.set_Atril(lista)
    tab_Ejecucuon=TE.Turno()
    tupla=IG.tablero(Jugador1,tab_Ejecucuon)
    window=tupla[0]
    lista_total_persona=[]
    lista_total_maquina=[]
    g=tupla[1]
    listas_palabras=[]
    ab=actualizar_columna.columna(window,0)
    tiempo_actual = 0
    okey_fin=False
    try:
        if ok_posponer:
            listas_palabras=AV.ReaundarPartida(g,window,maquina,tab_Ejecucuon,ab,Jugador1)
            print(listas_palabras)
            if listas_palabras!= None:
                lista_total_persona=listas_palabras[1]
                lista_total_maquina=listas_palabras[0]
                tiempo_actual=listas_palabras[2]
        segundaletra=False
        start_time = int(round(time.time()*100))-tiempo_actual
        agrego_letra_del_tablero=   True
        while True:
            event, values = window.read(timeout=10,timeout_key="TIMEOUT_KEY")
            tiempo_actual=int(round(time.time() * 100)) - start_time
            window['tiempo'].update('{:02d}:{:02d}.{:02d}'.format((tiempo_actual // 100) // 60,
                                                                (tiempo_actual // 100) % 60,
                                                                tiempo_actual%100))
            tiempo_actual+=1
            if ((nivel[0]=="Facil" and tiempo_actual>60000) or (nivel[0]=="Medio" and tiempo_actual>=42000) or (nivel[0]=="VB" and tiempo_actual>=30000) or (nivel[0]=="JJ" and tiempo_actual>=30000)):
                okey_fin=True
                raise IndexError
            if event == "Fin del Juego":
                raise IndexError

            if event=="TIMEOUT_KEY" or event=="_GRAPH_6" or event=="_GRAPH_7" or event=="_GRAPH_8" or event=="_GRAPH_9":
                continue

            if event=="paso" and Jugador1.get_boton_seleccionado()==False :
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
            if (event=="paso" and Jugador1.get_boton_seleccionado()==True):
                continue
            if event is None :
                break

            if event == "ev" and tab_Ejecucuon.get_palabra()!="" and Jugador1.get_boton_seleccionado()==False:
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
            if event == "Posponer" and Jugador1.get_boton_seleccionado()==False:
                AV.posponerPartida(tab_Ejecucuon,lista_total_persona,lista_total_maquina,ab,Jugador1,maquina,tiempo_actual)
                break
            if event=="inst":
                layout = [
                    [sg.Image(r'Instrucciones.png')],
                    [sg.Button("¡Entendido!",key="ok")]
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

            if event == "Cambio Letras" and Jugador1.get_boton_seleccionado()==False:
                window.FindElement(event).Update("¡Presioname luego de selecionar todas tus letras a cambiar!.")
                window.FindElement(event).Update(button_color=('white','black'))
                AV.cambiamosLetras(window,Jugador1,event,tab_Ejecucuon,ab,tiempo_actual)
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
        window.close()
    except(IndexError):
        AV.FinDelJuego(window,maquina,Jugador1,Top,listas_palabras,okey_fin)

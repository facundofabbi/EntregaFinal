import PySimpleGUI as sg
import Configuracion  as c
import json
import random as r
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
    Top = Top.Top()
    Jugador1=Jugador(todo[3],True)
    maquina = Maquinola(True)
    lista=Jugador1.BuscarEnLaBolsa(7)
    Jugador1.set_Atril(lista)
    lista=maquina.BuscarEnLaBolsa(7)
    maquina.set_Atril(lista)
    tab_Ejecucuon=TE.Turno()
    tupla=IG.tablero(Jugador1,tab_Ejecucuon,todo[4])
    window=tupla[0]
    lista_total_persona=[]
    lista_total_maquina=[]
    g=tupla[1]
    listas_palabras=[]
    ab=actualizar_columna.columna(window,0)
    tiempo_actual = 0
    okey_fin=False
    ok_invalida_todo=True
    ok_juegaMaquina=False
    formo_palabra_corta=True
    ok_no_entro=True
    no_hay_partida=True
    Reanudo_partida=True
    try:
        if ok_posponer:
            listas_palabras=AV.ReaundarPartida(g,window,maquina,tab_Ejecucuon,ab,Jugador1,nivel)
            if listas_palabras!= "":
                no_hay_partida=False
                Reanudo_partida=False
                lista_total_persona=listas_palabras[1]
                lista_total_maquina=listas_palabras[0]
                tiempo_actual=listas_palabras[2]
                nivel=listas_palabras[3]
        segundaletra=False
        start_time = int(round(time.time()*100))-tiempo_actual
        agrego_letra_del_tablero=True
        arranque_random=r.randrange(2)
        if arranque_random==1:
            no_hay_partida=False
            letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
            maquina.PrimerLugar(tab_Ejecucuon,g)
            AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
            ab.set_cant(len(letrita[1]))
            maquina.fin_turno()
            tab_Ejecucuon.FinTurno()
            lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
            AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
            agrego_letra_del_tablero=True
        while True:
            if ok_juegaMaquina:
                ok_juegaMaquina=False
                letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
                if arranque_random==0:
                    maquina.PrimerLugar(tab_Ejecucuon,g)
                    arranque_random=1
                else:
                    maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
                AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
                ab.set_cant(len(letrita[1]))
                maquina.fin_turno()
                tab_Ejecucuon.FinTurno()
                lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
                AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
                agrego_letra_del_tablero=   True
            event, values = window.read(timeout=10,timeout_key="TIMEOUT_KEY")
            tiempo_actual=int(round(time.time() * 100)) - start_time
            window['tiempo'].update('{:02d}:{:02d}.{:02d}'.format((tiempo_actual // 100) // 60,
                                                                (tiempo_actual // 100) % 60,
                                                                tiempo_actual%100))
            tiempo_actual+=1
            tuplita=tab_Ejecucuon.get_posicionLetra_anterior()
            if maquina.get_cant_paso()==3:
                raise IndexError
            if ((nivel[0]=="Facil" and tiempo_actual>60000) or (nivel[0]=="Medio" and tiempo_actual>=42000) or (nivel[0]=="VB" and tiempo_actual>=30000) or (nivel[0]=="JJ" and tiempo_actual>=30000)):
                okey_fin=True
                raise IndexError
            if event == "Fin del Juego":
                raise IndexError

            if event=="TIMEOUT_KEY" or event=="_GRAPH_6" or event=="_GRAPH_7" or event=="_GRAPH_8" or event=="_GRAPH_9":
                continue

            if len(tab_Ejecucuon.get_key_usadas())==0 and  not Jugador1.get_boton_seleccionado():
                ok_invalida_todo=True
            no_hay_partida=False
            if (event=="paso" and ok_invalida_todo):
                letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
                if arranque_random==0:
                    maquina.PrimerLugar(tab_Ejecucuon,g)
                    arranque_random=1
                else:
                    maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
                AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
                ab.set_cant(len(letrita[1]))
                maquina.fin_turno()
                tab_Ejecucuon.FinTurno()
                lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
                AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
                agrego_letra_del_tablero=   True
                continue
            if event=="paso" and Jugador1.get_boton_seleccionado()==True:
                continue
            if event is None :
                break
            if event == "ev"  and Jugador1.get_boton_seleccionado()==False:
                anterior=tab_Ejecucuon.get_posicionLetra_anterior()
                if anterior[0] != -20 and tab_Ejecucuon.get_palabra()=="":
                    formo_palabra_corta=tab_Ejecucuon.palabra_corta()
                if formo_palabra_corta==False:
                    if ok_no_entro:
                        ok_no_entro=False
                        arranque_random=0
                    tab_Ejecucuon.set_palabra(letra)
                    AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
                    Jugador1.FinTurno()
                    tab_Ejecucuon.FinTurno()
                    segundaletra=False
                    letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
                    if arranque_random==0:
                        maquina.PrimerLugar(tab_Ejecucuon,g)
                        arranque_random=1
                    else:
                        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
                    maquina.fin_turno()
                    puntos_maquina = maquina.get_puntos_jugador()
                    lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
                    AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
                    tab_Ejecucuon.FinTurno()
                    AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
                    ab.set_cant(len(letrita[1]))
                    ok_invalida_todo=True
                    formo_palabra_corta=True
                    continue
                if tab_Ejecucuon.get_palabra()!="":
                    agrego_letra_del_tablero=   True
                    if AV.EvaluarPalabra(tab_Ejecucuon.get_palabra(),nivel[0]):
                    #if True:
                        ok_no_entro=False
                        arranque_random=0
                        palabra = tab_Ejecucuon.get_palabra()
                        lista_total_persona.append(Jugador1.Actualizar_Puntaje(AV,tab_Ejecucuon))
                        AV.Post_Evaluamos(window,Jugador1,tab_Ejecucuon)
                        tab_Ejecucuon.FinTurno()
                        AV.roleo_random_fichas(ab.get_keys(),window,len(palabra),ab)
                        ab.set_cant(len(palabra))
                        AV.VerPuntajeNuevo(lista_total_persona,window,Jugador1)
                    else:
                        AV.palabra_Invalida(tab_Ejecucuon,g,Jugador1,window)
                        if ok_no_entro:
                            ok_no_entro=False
                            arranque_random=0
                    Jugador1.FinTurno()
                    tab_Ejecucuon.FinTurno()
                    segundaletra=False
                    letrita = maquina.EncontrarPalabra(nivel[0],tab_Ejecucuon)
                    if arranque_random==0:
                        maquina.PrimerLugar(tab_Ejecucuon,g)
                        arranque_random=1
                    else:
                        maquina.evaluar_donde(tab_Ejecucuon,g,letrita[0])
                    maquina.fin_turno()
                    puntos_maquina = maquina.get_puntos_jugador()
                    lista_total_maquina.append(maquina.Actualizar_Puntaje(AV,letrita[1],tab_Ejecucuon))
                    AV.VerPuntajeNuevo(lista_total_maquina,window,maquina)
                    tab_Ejecucuon.FinTurno()
                    AV.roleo_random_fichas(ab.get_keys(),window,len(letrita[1]),ab)
                    ab.set_cant(len(letrita[1]))
                    ok_invalida_todo=True
                    continue
            if event == 'ev' and tab_Ejecucuon.get_palabra()=='':
                continue
            if event == "Posponer" and ok_invalida_todo:
                AV.posponerPartida(tab_Ejecucuon,lista_total_persona,lista_total_maquina,ab,Jugador1,maquina,tiempo_actual,todo[4],nivel)
                break
            if event=="inst":
                layout = [
                    [sg.Image(r'Imagenes/Instrucciones.png')],
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
            if event == "Cambio Letras" and ok_invalida_todo:
                window.FindElement(event).Update("¡Presioname luego de selecionar todas tus letras a cambiar!.")
                window.FindElement(event).Update(button_color=('white','black'))
                AV.cambiamosLetras(window,Jugador1,event,tab_Ejecucuon,ab,tiempo_actual)
                ok_juegaMaquina=True
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
                if arranque_random==0 and (box_x!=7 or box_y!=7) and Reanudo_partida :
                    continue
                else:
                    Reanudo_partida=False
                    arranque_random=1
                if Jugador1.get_boton_seleccionado(): # logica de boton
                    if not segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y):
                        tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra)
                        tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                        segundaletra=True
                        tab_Ejecucuon.set_posicionLetra_anterior((box_x,box_y))
                        Jugador1.set_boton_seleccionado(False)
                        Jugador1.set_letra("")
                        tab_Ejecucuon.set_primera_letra_palabra((box_x,box_y))
                        continue
                    if AV.posicionValida(box_x,box_y,tab_Ejecucuon) and segundaletra and not tab_Ejecucuon.get_selected_posicion(box_x,box_y) :
                        tab_Ejecucuon.EscribirEnTablero(box_x,box_y,g,letra)
                        tab_Ejecucuon.chequeroDuplica(box_x,box_y,letra)
                        Jugador1.set_letra("")
                        Jugador1.set_boton_seleccionado(False)
                        if tab_Ejecucuon.get_abajo():
                            tab_Ejecucuon.Armar_palabra_y(box_x,box_y)
                        if tab_Ejecucuon.get_derecha() :
                            tab_Ejecucuon.Armar_palabra_x(box_x,box_y)
                        tab_Ejecucuon.set_posicionLetra_anterior((box_x,box_y))

                        continue
                    else :
                        continue
            else:
                if Jugador1.get_boton_seleccionado():
                    lista=tab_Ejecucuon.get_key_usadas()
                    total=len(lista)
                    if event==lista[total-1]:
                        letra==""
                        Jugador1.set_boton_seleccionado(False)
                        IG.Uncheck_boton(event,window)
                        AV.error_de_boton(window,Jugador1,tab_Ejecucuon,event)
                    continue
                else:
                    if event in tab_Ejecucuon.get_llaves():
                        Jugador1.set_boton_seleccionado(True)
                        ok_invalida_todo=False
                        letra=AV.tocoBoton(window,Jugador1,tab_Ejecucuon,event)
                        if letra=="":
                            Jugador1.set_boton_seleccionado(False)
                            continue
        window.close()
    except(IndexError):
        AV.FinDelJuego(window,maquina,Jugador1,Top,listas_palabras,okey_fin,tab_Ejecucuon,no_hay_partida)

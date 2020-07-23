import PySimpleGUI as sg
import InterfazGrafica
import json
from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
import random as r
import time
# import Actualizacion_Bolsa as ab

def cambiamosLetras(window,Jugador1,event,tab_Ejecucuon,actualizar_columna):
        Llaves=tab_Ejecucuon.get_llaves()
        ok=True
        ok1=False
        cambio=[]
        llavesTurno = []
        llavess=[]
        oki=True
        okas=True
        # InterfazGrafica.Check_button(event,window)
        print(len(actualizar_columna.get_muchosbotones()))
        print(tab_Ejecucuon.get_key_usadas())
        while(len(actualizar_columna.get_muchosbotones())>len(llavesTurno)):
            event,values=window.Read()
            if event!='_GRAPH_' and event !="Evaluar":
                if event in Llaves and not event in llavesTurno:
                    llavesTurno.append(event)
                    cambio.append(window.FindElement(event).GetText())
                    InterfazGrafica.Check_boton(event,window)
                    llavess.append(event)
                if  event== "Cambio Letras":
                    okas=False
                    window.FindElement(event).Update("Ahora elige tus nuevas fichas")
                    window.FindElement(event).Update(button_color=('white','black'))
                    # InterfazGrafica.Uncheck_button(event,window)
                    break
                if event== None:
                    oki=False
                    break
            else:
                continue
        if   okas:
            window.FindElement("Cambio Letras").Update("Selecciono la maxima cantidad de fichas disponibles")
            window.FindElement("Cambio Letras").Update(button_color=('white','black'))
        if oki:
            lista=Jugador1.CambioLetras(cambio)
            llet=tab_Ejecucuon.get_lista_de_letras_en_tablero()
            actualizar_bolsa_de_fichas(len(llet),window,actualizar_columna,lista)
            window.FindElement("Cambio Letras").Update("Cambio Letras")
            InterfazGrafica.Uncheck_button("Cambio Letras",window)
            Jugador1.FinTurno()
            for i in range(len(llavess)):
                window.FindElement(llavess[i]).Update(lista[i])
                InterfazGrafica.Uncheck_boton(llavess[i],window)




def tocoBoton(window,jugador,tab_Ejecucuon,event):
        lis=tab_Ejecucuon.get_key_usadas()
        letra=window.FindElement(event).GetText()
        InterfazGrafica.Check_boton(event,window)
        if not event  in lis:
            tab_Ejecucuon.set_key_usadas(event)
            jugador.set_letra_usada(letra)
            return letra
        else:
            return ""


def Post_Evaluamos (window,Jugador1,tab_Ejecucuon):
        # ''' update color a botones , y fin de turno a jugador'''
        Antes_usadas=Jugador1.get_Ya_Use()
        lista=Jugador1.CambioLetrasSinDevolver(Antes_usadas)
        key_usadas=tab_Ejecucuon.get_key_usadas()
        for i  in range(len(lista)):
            window.FindElement(key_usadas[i]).Update(lista[i],button_color=('black','#FEEFBA'))
        Jugador1.FinTurno()



def palabra_Invalida(tab_Ejecucuon,g,Jugador1,window):
        id_delete=tab_Ejecucuon.get_id()
        lista=tab_Ejecucuon.get_key_usadas()
        text_box=tab_Ejecucuon.get_text_box()
        selected=tab_Ejecucuon.get_selected()
        for i in id_delete:
            g.DeleteFigure(text_box[i[0]][i[1]])
            selected[i[0]][i[1]]=False
            tab_Ejecucuon.set_coordenadas_en_tablero(i[0],i[1])
        for i in lista:
            InterfazGrafica.Uncheck_boton(i,window)
        tab_Ejecucuon.set_text_box(text_box)
        tab_Ejecucuon.set_selected(selected)


def posicionValida(box_x,box_y,tab_Ejecucuon):
    posicionLetra1=tab_Ejecucuon.get_posicionLetra1()
    print(posicionLetra1)
    x=posicionLetra1[0]
    y=posicionLetra1[1]
    if x==box_x and y+2==box_y and not tab_Ejecucuon.get_abajo() and tab_Ejecucuon.get_desbugeo() and  tab_Ejecucuon.get_coordenadas_en_tablero(box_x,y+1)!="":
        tab_Ejecucuon.set_derecha()
        tab_Ejecucuon.set_desbugeo()
        l=tab_Ejecucuon.get_coordenadas_en_tablero(box_x,y+1)
        tab_Ejecucuon.set_palabra(l)
        return True
    if box_x==x+2 and y==box_y and not tab_Ejecucuon.get_derecha() and tab_Ejecucuon.get_desbugeo()and tab_Ejecucuon.get_coordenadas_en_tablero(x+1,box_y)!="":
        tab_Ejecucuon.set_abajo()
        tab_Ejecucuon.set_desbugeo()
        l=tab_Ejecucuon.get_coordenadas_en_tablero(x+1,box_y)
        tab_Ejecucuon.set_palabra(l)
        return True
    y=y+1
    if box_x==x and y==box_y and not tab_Ejecucuon.get_abajo() :
        tab_Ejecucuon.set_derecha()
        # pal=tab_Ejecucuon.get_palabra()
        # pal=pal[1:]
        # tab_Ejecucuon.set_palabra_TODA(pal)
        return True
    else :
        y=y-1
        x=x+1
        if box_x==x and y==box_y and not tab_Ejecucuon.get_derecha() :
            tab_Ejecucuon.set_abajo()
            # pal=tab_Ejecucuon.get_palabra()
            # pal=pal[1:]
            # tab_Ejecucuon.set_palabra_TODA(pal)
            return True
    return False



def VerPuntajeNuevo(lista_total_maquina,window,objeto):
    if objeto.get_id() ==1:
        window['lista_maquina'].update(values = lista_total_maquina)
        window['puntaje_maquina'].Update(objeto.get_puntaje_total())
    else:
        window['lista_persona'].update(values = lista_total_maquina)
        window['puntaje_persona'].Update(objeto.get_puntaje_total())


def EvaluarPalabra(palabra,nivel):
    nivel=nivel.upper()
    pal=parse(palabra).split("/")
    aux=pal[1]
    if nivel == "FACIL":
        if palabra.lower() in spelling or palabra.lower() in lexicon :
            return True
        else:
            return False
    if nivel == "MEDIO":
        if aux=="VB" or aux=="JJ":
            return True
        else:
            return False
    if nivel != "FACIL" and nivel != "MEDIO":
        if aux == nivel:
            return True
        else:
            return False




def roleo_random_fichas(mb,window,cant,ab):
    #try:
        for i in range(cant):
            key= r.choice(mb)
            ab.agregar_deshabilitado(key)
            ab.sacar_llave(key)
            window.FindElement(key).Update(button_color=('black','#092F50'))
    #except:
        #sg.popup("chicos aca se termia el programa dsp lo vemos")
        #window.close()
def actualizar_bolsa_de_fichas(cant,window,ab,cambio):
    num=ab.get_cant()
    mb=ab.get_keys()
    cant=cant-num
    roleo_random_fichas(mb,window,cant,ab)
    ab.set_cant(cant)
    lista_leras=ab.get_keys()
    for i in lista_leras:
        window.FindElement(i).Update(disabled=False)
        window.FindElement(i).Update(button_color=('white','#07589B'))
    h=bucle_de_cambio_letras(cambio,lista_leras,window)
    for i in h:
        window.FindElement(i).Update("¿?")
    for i in lista_leras:
        window.FindElement(i).Update(disabled=True)
        window.FindElement(i).Update(button_color=('black','#044880'))
def bucle_de_cambio_letras(cambio,lista_keys,window):
    cant=len(cambio)
    lista1=[]
    while True :
        cant=cant-1
        event,values=window.read()
        if cant==0:
            window.FindElement(event).Update(cambio[cant])
            window.FindElement(event).Update(button_color=('black','#FEEFBA'),disabled=True)
            lista1.append(event)
            break
        if event in lista_keys:
            window.FindElement(event).Update(cambio[cant])
            window.FindElement(event).Update(button_color=('black','#FEEFBA'),disabled=True)
            lista1.append(event)
            continue
        if event==None:
            break
    return lista1


def CrucePrimerLetra(letra,pos,tab):
    x=pos[0]
    y=pos[1]
    if tab.get_selected_posicion(x-1,y) and tab.get_selected_posicion(x+1,y)==False:
        ant=tab.get_coordenadas_en_tablero(x-1,y)
        tab.set_palabra(ant)
        return True
    else:
        if tab.get_selected_posicion(x,y-1) and tab.get_selected_posicion(x,y+1)==False:
            ant=tab.get_coordenadas_en_tablero(x,y-1)
            tab.set_palabra(ant)
            return True



def ReaundarPartida(g,window,maquina,tab_Ejecucuon,AB,jugador1):
    #try:
    lista_posponer=[]
    print("cargando partidda.......")
    archivo11 = open('posponerPartida.json','r')
    lista_posponer=json.load(archivo11)
    archivo11.close()
    tab_Ejecucuon.set_coordenadas_en_tablero_lista(lista_posponer[1])
    tab_Ejecucuon.set_selected(lista_posponer[2])
    tab_Ejecucuon.set_matriz(lista_posponer[3])
    tab_Ejecucuon.set_matrizMultiplica(lista_posponer[4])
    tab_Ejecucuon.set_text_box(lista_posponer[0])
    for x in range(0,15):
        for y in range(0,15):
            tab_Ejecucuon.EscribirEnTableroPosponer(x,y,g)
    VerPuntajeNuevo(lista_posponer[5],window,maquina)
    VerPuntajeNuevo(lista_posponer[6],window,jugador1)
    AB.set_deshabilitados(lista_posponer[7])
    AB.sacar_primer_atril(window,len(lista_posponer[7]))
    archivo1 = open ('bolsa.json','w')
    json.dump(lista_posponer[8],archivo1,indent=1)
    archivo1.close()
    jugador1.set_puntaje_total(lista_posponer[9])
    jugador1.set_nombre(lista_posponer[11][0])
    print(lista_posponer[11][0])
    print(jugador1.get_nombre())
    maquina.set_puntaje_total(lista_posponer[10])
    window["puntaje_persona"].update(lista_posponer[9])
    window["puntaje_maquina"].update(lista_posponer[10])
    window["n_j"].update(jugador1.get_nombre())

    jugador1.FinTurno()
    maquina.fin_turno()
    tab_Ejecucuon.FinTurno()
    return lista_posponer[5],lista_posponer[6]
    #except:
         #sg.popup("No se puede cargar la partida ya q no se a guardado una nunca. Disculpe las molestias")

def posponerPartida(tab_Ejecucuon,lista_total_persona,lista_total_maquina,AB,jugador1,maquina):
    lista_posponer=[]
    lista_posponer.append(tab_Ejecucuon.get_text_box())
    lista_posponer.append(tab_Ejecucuon.get_coordenadas_en_tablero_lista())
    lista_posponer.append(tab_Ejecucuon.get_selected())
    lista_posponer.append(tab_Ejecucuon.get_matriz())
    lista_posponer.append(tab_Ejecucuon.get_matrizMultiplica())
    lista_posponer.append(lista_total_maquina)
    lista_posponer.append(lista_total_persona)
    lista_posponer.append(AB.get_deshabilitados())
    archivo1 = open ('bolsa.json','r')
    bolsa=json.load(archivo1)
    print(bolsa)
    archivo1.close()
    lista_posponer.append(bolsa)
    lista_posponer.append(jugador1.get_puntaje_total())
    lista_posponer.append(maquina.get_puntaje_total())
    lista = []
    lista.append(jugador1.get_nombre())
    print(lista)
    lista_posponer.append(lista)
    archivo = open ('posponerPartida.json','w')
    json.dump(lista_posponer,archivo)
    archivo.close()
    sg.popup("La partida sera pospueta para un futuro no muy lejano :D, anda a descansar y veni fresquito para seguire jugando")

def Top10():
    archivo = open('TopJugadores.json','r')
    lista1=json.load(archivo)
    archivo.close()
    sg.theme('DarkAmber')
    layout = [ [sg.Listbox(lista1,key='lista_maquina',size=(20,10))],
    [sg.Button("Ok",size=(10,2))]]
    w = sg.Window('Top 10').Layout(layout)
    while True:
        event,values = w.read()
        if event == "Ok":
            break
        if event == None:
            break
    w.close()
def MostrarFichasMaquina(w,maquina):
    atril = maquina.get_atril()
    for i in range(len(atril)):
        i=i+1
        i=i*-1
        w.FindElement(str(i)).Update(atril[i])

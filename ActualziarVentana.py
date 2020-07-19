import PySimpleGUI as sg
import InterfazGrafica
import json
from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
import random as r
# import Actualizacion_Bolsa as ab

def cambiamosLetras(window,Jugador1,event,tab_Ejecucuon,actualizar_columna):
        Llaves=tab_Ejecucuon.get_llaves()
        ok=True
        ok1=False
        cambio=[]
        llavesTurno = []
        llavess=[]
        oki=True
        # InterfazGrafica.Check_button(event,window)
        while True:
            event,values=window.Read()
            if event!='_GRAPH_' and event !="Evaluar":
                if event in Llaves and not event in llavesTurno:
                    llavesTurno.append(event)
                    cambio.append(window.FindElement(event).GetText())
                    InterfazGrafica.Check_boton(event,window)
                    llavess.append(event)
                if  event== "Cambio Letras":
                    window.FindElement(event).Update("Ahora elige tus nuevas fichas")
                    window.FindElement(event).Update(button_color=('white','black'))
                    # InterfazGrafica.Uncheck_button(event,window)
                    break
                if event== None:
                    oki=False
                    break
            else:
                continue
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
        for i in lista:
            InterfazGrafica.Uncheck_boton(i,window)
        tab_Ejecucuon.set_text_box(text_box)
        tab_Ejecucuon.set_selected(selected)


def posicionValida(box_x,box_y,tab_Ejecucuon):
    posicionLetra1=tab_Ejecucuon.get_posicionLetra1()
    x=posicionLetra1[0]
    y=posicionLetra1[1]
    y=y+1
    if box_x==x and y==box_y and not tab_Ejecucuon.get_abajo() :
        tab_Ejecucuon.set_derecha()
        return True
    else :
        y=y-1
        x=x+1
        if box_x==x and y==box_y and not tab_Ejecucuon.get_derecha() :
            tab_Ejecucuon.set_abajo()
            return True
    return False


def PuntosPalabra(tab_Ejecucuon):
    pts=0
    archivo= open("puntaje_letras.json","r")
    dicc1=json.load(archivo)
    archivo.close()
    palabra=tab_Ejecucuon.get_palabra()
    lista=tab_Ejecucuon.get_duplica()
    lista1=tab_Ejecucuon.get_triplica()
    for i in palabra:
        num=dicc1[i]
        num=num[0]
        if i in lista:
            num=num*2
        if i in lista1:
            num=num*3
        pts+=num
    return pts


def EvaluarPalabra(palabra,nivel):
    print(palabra)
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




def actualizar_bolsa_de_fichas(cant,window,ab,cambio):
    num=ab.get_cant()
    mb=ab.get_keys()
    cant=cant-num
    for i in range(cant):
        key= r.choice(mb)
        ab.agregar_deshabilitado(key)
        ab.sacar_llave(key)
        window.FindElement(key).Update(button_color=('black','#092F50'))
    ab.set_cant(cant)
    lista_leras=ab.get_keys()
    for i in lista_leras:
        window.FindElement(i).Update(disabled=False)
        window.FindElement(i).Update(button_color=('white','#07589B'))
        # (button_color=('black','#FEEFBA'))
        # (button_color=('white','#07589B'))
    bucle_de_cambio_letras(cambio,lista_leras,window)
    for i in lista_leras:
        window.FindElement(i).Update(disabled=True)
        window.FindElement(i).Update(button_color=('black','#044880'))
def bucle_de_cambio_letras(cambio,lista_keys,window):
    cant=len(cambio)
    lista1=[]
    while True :
        event,values=window.read()
        if event in lista_keys:
            cant=cant-1
            window.FindElement(event).Update(cambio[cant])
            window.FindElement(event).Update(button_color=('black','#FEEFBA'))
            lista1.append(event)
        if cant<=0:
            break
        if event==None:
            break
    for i in lista1:
        window.FindElement(i).Update("¿?")

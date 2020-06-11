import PySimpleGUI as sg
import InterfazGrafica
import json
from pattern.es import spelling as sp
from pattern.es import lexicon as le
from pattern.es import verbs
from pattern.es import parse

def cambiamosLetras(window,Jugador1,event,tab_Ejecucuon):
        Llaves=tab_Ejecucuon.get_llaves()
        ok=True
        ok1=False
        cambio=[]
        llavess=[]
        InterfazGrafica.Check_button(event,window)
        while True:
            event,values=window.Read()
            if event!='_GRAPH_' and event !="Evaluar":
                if event in Llaves and not event in cambio:
                    cambio.append(window.FindElement(event).GetText())
                    InterfazGrafica.Check_boton(event,window)
                    llavess.append(event)
                if  event== "Cambio Letras":
                    InterfazGrafica.Uncheck_button(event,window)
                    break
            else:
                continue
        lista=Jugador1.CambioLetras(cambio)
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
            window.FindElement(i).Update(button_color=('white','green'))
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
    nivel=nivel.upper()
    pal=parse(palabra).split("/")
    aux=pal[1]
    if nivel == "FACIL":
        if palabra in sp or palabra in le.keys() :
            return True
        else:
            return False
    if nivel == "MEDIO":
        if aux=="VB" or aux=="JJ":
            return True
        else:
            return False
    if nivel != "facil" and nivel != "medio":
        if aux == nivel:
            return True
        else:
            return False

import PySimpleGUI as sg
import modulito
import json
from pattern.es import spelling as sp
from pattern.es import lexicon as le
from pattern.es import verbs
from pattern.es import parse



def cambiamosLetras(window,Jugador1,event,Llaves):
        ok=True
        ok1=False
        cambio=[]
        llavess=[]
        window.FindElement(event).Update(button_color=('white','blue'))
        while True:
            event,values=window.Read()
            if event!='_GRAPH_':
                if event in Llaves and not event in cambio:
                    cambio.append(window.FindElement(event).GetText())
                    window.FindElement(event).Update(button_color=('white','#45b300'))
                    llavess.append(event)
                if  event== "Cambio Letras":
                    window.FindElement(event).Update(button_color=('black','grey'))
                    break
            else:
                continue
        lista=Jugador1.CambioLetras(cambio)
        Jugador1.FinTurno()
        for i in range(len(llavess)):

            window.FindElement(llavess[i]).Update(lista[i])
            window.FindElement(llavess[i]).Update(button_color=('white','green'))


def tocoBoton(window,jugador,event):
        lis=jugador.get_key_usadas()
        letra=window.FindElement(event).GetText()
        window.FindElement(event).Update(button_color=('white','#45b300'))
        if not event  in lis:
            jugador.set_key_usadas(event)
            jugador.Ya_use(letra)
            return letra
        else:
            return ""




def Post_Evaluamos (window,Jugador1):
        # ''' update color a botones , y fin de turno a jugador'''
        Antes_usadas=Jugador1.get_Ya_Use()
        lista=Jugador1.CambioLetras(Antes_usadas)
        key_usadas=Jugador1.get_key_usadas()
        for i  in range(len(lista)):
            window.FindElement(key_usadas[i]).Update(lista[i],button_color=('white','green'))
        Jugador1.FinTurno()

def palabra_Invalida(text_box,selected,g,Jugador1,window):
        id_delete=Jugador1.get_id()
        lista=Jugador1.get_key_usadas()
        for i in id_delete:
            g.DeleteFigure(text_box[i[0]][i[1]])
            selected[i[0]][i[1]]=False
        for i in lista:
            window.FindElement(i).Update(button_color=('white','green'))


def posicionValida(box_x,box_y,posicionLetra1 ,DL):
    x=posicionLetra1[0]
    y=posicionLetra1[1]
    y=y+1
    if box_x==x and y==box_y and not DL.get_abajo() :
        DL.set_derecha()
        return True
    else :
        y=y-1
        x=x+1
        if box_x==x and y==box_y and not DL.get_derecha() :
            DL.set_abajo()
            return True
    return False


def EscribirEnTablero(box_x,box_y,g,matriz,selected,text_box,letra,tam_celda,Jugador1):
    modulito.Check_box(box_x,box_y,g,matriz)
    selected[box_x][box_y]=True # esto es para no volver al mismo casillero
    text_box[box_x][box_y] = g.DrawText(letra, (box_x * tam_celda + 12, box_y * tam_celda + 11))
    Jugador1.id_usados_en_turno((box_x,box_y))


def PuntosPalabra(palabra,DL):
    pts=0
    archivo= open("puntaje_letras.json","r")
    dicc1=json.load(archivo)
    lista=DL.get_duplica()
    lista1=DL.get_triplica()
    for i in palabra:
        num=dicc1[i]
        num=num[0]
        if i in lista:
            num=num*2
        else:
            if i in lista:
                num=num*3
        pts+=num
    return pts


def EvaluarPalabra(palabra,nivel):
    nivel=nivel.upper()
    pal=parse(palabra).split("/")
    aux=pal[1]
    if nivel == "facil":
        if palabra in sp or palabra in le :
            return True
        else:
            return False
    if nivel == "medio":
        if aux=="VB" or aux=="JJ":
            return True
        else:
            return False
    if nivel != "facil" and nivel != "medio":
        if aux == nivel:
            return True
        else:
            return False

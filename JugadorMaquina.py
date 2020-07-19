from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
from random import choice
import random
import json
from JugadorGenerico import Padre

class Maquinola(Padre):

    def __init__(self,turno=False):
        super().__init__(turno)
        self._palabra = ""

    def fin_turno(self):
        self._palabra = ""
        super().set_turno(False)
        super().set_letra("")

    def get_palabra(self):
        return self._palabra
    def set_palabra(self,palabra):
        self._palabra = palabra


    def busco_en_x(self,x,y,tablero,tab):
        ok=False
        cant=len(self._palabra)
        for i in range(cant):
            x=x+1
            if( x<15):
                if tablero[x][y] :
                        return False
            else :
                return False
        return True
    def busco_en_y(self,x,y,tablero,tab):
        ok=False
        cant=len(self._palabra)
        for i in range(cant):
            y=y+1
            if( y<15):
                if tablero[x][y] :
                        return False
            else :
                return False
        return True

    def poner_palabra_x(self,x,y,tab,g):
        pal=self._palabra
        for i in pal:
            tab.EscribirEnTablero(x,y,g,i)
            x=x+1


    def poner_palabra_y(self,x,y,tab,g):
        pal=self._palabra
        for i in pal:
            tab.EscribirEnTablero(x,y,g,i)
            y=y+1



    def _chequeo_espacio(self,tablero,tab,x,y,g):
        ok=True
        if(tablero[x][y]==False):
            if self.busco_en_x(x,y,tablero,tab,):
                ok=False
                self.poner_palabra_x(x,y,tab,g)
                return True
            if self.busco_en_y(x,y,tablero,tab,) and ok:
                self.poner_palabra_y(x,y,tab,g)
                return True
        return False






    def lugar_random(self,tab,g):
        ok=False
        x=random.randrange(15)
        y=random.randrange(15)
        tablero=[]
        tablero=tab.get_tablero_booleano()
        num=500
        while True:
            num=num-1
            puse_palabra=self._chequeo_espacio(tablero,tab,x,y,g)

            if puse_palabra:
                break
            else:
                x=random.randrange(15)
                y=random.randrange(15)
            if num<=0:
                break


    def calculo_lugar_en_x_cruzada(self,tab,x,y,primerMitad,segundaMitad):
        pal=self._palabra
        cant=len(pal)
        x=x-len(primerMitad)

        if x>=0 and x<15:
            for i in range(len(primerMitad)):
                if tab.chequeo_selected(x,y):
                    return False
                if x<14:
                    x=x+1
                else : return False
            if x<14:
                x=x+1
                for i in range(len(segundaMitad)):
                    if tab.chequeo_selected(x,y):
                        return False
                    if x<14:
                        x=x+1
                    else :
                        return False
            else :
                return False
        return True
    def calculo_lugar_en_y_cruzada(self,tab,x,y,primerMitad,segundaMitad):
        pal=self._palabra
        cant=len(pal)
        y=y-len(primerMitad)
        if y>=0 and y<15:
            for i in range(len(primerMitad)):
                if tab.chequeo_selected(x,y):
                    return False
                if y<14:
                    y=y+1
                else : return False
            if y<14:
                y=y+1
                for i in range(len(segundaMitad)):
                    if tab.chequeo_selected(x,y):
                        return False
                    if y<14:
                        y=y+1
                    else :
                        return False
            else :
                return False
        return True

    def poner_palabra_x_cruzada(self,tab_ejecucion,primerMitad,segundoMitad,x,y,g):
        pal=self._palabra
        cant=len(pal)
        x=x-len(primerMitad)
        if x>=0:
            for i in range(len(primerMitad)):
                tab_ejecucion.EscribirEnTablero(x,y,g,primerMitad[i])
                x=x+1
            x=x+1
            for i in range(len(segundoMitad)):
                tab_ejecucion.EscribirEnTablero(x,y,g,segundoMitad[i])
                x=x+1
    def poner_palabra_y_cruzada(self,tab_ejecucion,primerMitad,segundoMitad,x,y,g):
        pal=self._palabra
        cant=len(pal)
        y=y-len(primerMitad)
        if x>=0:
            for i in range(len(primerMitad)):
                tab_ejecucion.EscribirEnTablero(x,y,g,primerMitad[i])
                y=y+1
            y=y+1
            for i in range(len(segundoMitad)):
                tab_ejecucion.EscribirEnTablero(x,y,g,segundoMitad[i])
                y=y+1




    def evaluar_donde(self,tab_ejecucion,g,l):
        box_x = -1
        box_y = -1
        okk=True
        ok = False
        id_usados = []
        booleanito=True
        pos=-1
        pal=self._palabra
        if l != "":
            for x in range(15):
                for y in range(15):
                    if l.upper()== tab_ejecucion.get_coordenadas_en_tablero(x,y).upper():
                        box_x = x
                        box_y = y
            for i in range(len(pal)):
                if l == pal[i]:
                    pos = i
            if box_x!=-1:
                primerMitad=pal[0:pos]
                segundoMitad=pal[pos+1:]
                if self.calculo_lugar_en_x_cruzada(tab_ejecucion,box_x,box_y,primerMitad,segundoMitad):
                    self.poner_palabra_x_cruzada(tab_ejecucion,primerMitad,segundoMitad,box_x,box_y,g)
                    booleanito=False
                    okk=False
                if self.calculo_lugar_en_y_cruzada(tab_ejecucion,box_x,box_y,primerMitad,segundoMitad) and okk :
                    self.poner_palabra_y_cruzada(tab_ejecucion,primerMitad,segundoMitad,box_x,box_y,g)
                    booleanito=False
                if booleanito:
                    self.lugar_random(tab_ejecucion,g)
            else :
                self.lugar_random(tab_ejecucion,g)
        else:
             self.lugar_random(tab_ejecucion,g)

    def buscarEn(self,nombre):
        for palabra in nombre:
            ya_usadas=[]
            atril_a_usar=self.get_atril().copy()
            sirve=True
            palabra=palabra.upper()
            for i in palabra:
                if i in atril_a_usar:
                    ya_usadas.append(i)
                    atril_a_usar.remove(i)
                else:
                    sirve=False
            if sirve and len(palabra)>1:
                nuevo = self.BuscarEnLaBolsa(len(ya_usadas))
                for letra in self.get_atril():
                    for i in ya_usadas:
                        if letra == i:
                            ya_usadas.remove(i)
                            self.set_remove_atril(letra)
                for i in nuevo:
                    self.set_agregar_atril(i)
                break
        if sirve:
            return (palabra,True,ya_usadas)
        else:
            return("",False,[])


    def get_palabra(self):
        return self._palabra

    def EncontrarPalabra(self,nivel,TE):
        listaDeLetrasEnElTablero=TE.get_lista_de_letras_en_tablero()
        tupla=("",False,[])
        archivo=open ("adjetivos.json","r")
        adjetivos=json.load(archivo)
        archivo.close()
        letra=""
        if nivel=="Facil":
            tupla=self.buscarEn(lexicon)
            if not tupla[1]:
                tupla=self.buscarEn(spelling)
        if nivel=="Medio":
            tupla=self.buscarEn(verbs)
            if not tupla[1]:
                tupla=self.buscarEn(adjetivos)
        if nivel=="VB":
            tupla=self.buscarEn(verbs)
        if nivel=="JJ":
            tupla=self.buscarEn(adjetivos)

        if tupla[1]:
            for k in tupla[0]:
                if k in listaDeLetrasEnElTablero:
                    letra=k
                    break
        self._palabra=tupla[0]
        super().set_letra(letra)
        palabra=tupla[0]
        return letra,palabra

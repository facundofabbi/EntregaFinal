from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
import time
from random import choice
import random
import json
from JugadorGenerico import Padre

class Maquinola(Padre):

    def __init__(self,turno=False):
        super().__init__(turno)
        self._palabra = ""
        self._ID = 1

    def get_id(self):
        return self._ID
    def fin_turno(self):
        '''Finaliza el turno de la maquina '''
        self._palabra = ""
        super().set_turno(False)
        super().set_letra("")

    def get_palabra(self):
        return self._palabra
    def set_palabra(self,palabra):
        self._palabra = palabra
    def get_palabra(self):
        return self._palabra

    def busco_en_x(self,x,y,tablero,tab):
        '''Busca si en el eje x es posibe ingresar la letra'''
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
        '''Busca si en el eje y es posibe ingresar la letra'''
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
        '''Verifica si la palabra puede ser colocado en el eje x'''
        pal=self._palabra
        for i in pal:
            tab.chequeroDuplica(x,y,i)
            tab.EscribirEnTablero(x,y,g,i)
            x=x+1

    def poner_palabra_y(self,x,y,tab,g):
        '''Verifica si la palabra puede ser colocado en el eje y'''
        pal=self._palabra
        for i in pal:
            tab.chequeroDuplica(x,y,i)
            tab.EscribirEnTablero(x,y,g,i)
            y=y+1

    def _chequeo_espacio(self,tablero,tab,x,y,g):
        '''Chequeo que la proxima posicion sea valida'''
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
        '''Eligue un lugar random al colocar la palabra'''
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

    def PrimerLugar(self,tab,g):
        '''Coloca la primer palabra en el casilllero de inicio'''
        ok=False
        x=7
        y=7
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
        '''Busca que haya lugar antes y despues de la letra que se quiere cruzar en el eje X'''
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
        '''Busca que haya lugar antes y despues de la letra que se quiere cruzar en el eje Y'''
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
        '''Escribe una palabra en el eje X cruzando una letra del tablero'''
        pal=self._palabra
        cant=len(pal)
        x=x-len(primerMitad)
        if x>=0:
            for i in range(len(primerMitad)):
                tab_ejecucion.chequeroDuplica(x,y,i)
                tab_ejecucion.EscribirEnTablero(x,y,g,primerMitad[i])
                x=x+1
            x=x+1
            for i in range(len(segundoMitad)):
                tab_ejecucion.chequeroDuplica(x,y,i)
                tab_ejecucion.EscribirEnTablero(x,y,g,segundoMitad[i])
                x=x+1

    def poner_palabra_y_cruzada(self,tab_ejecucion,primerMitad,segundoMitad,x,y,g):
        '''Escribe una palabra en el eje Y cruzando una letra del tablero'''
        pal=self._palabra
        cant=len(pal)
        y=y-len(primerMitad)
        if y>=0:
            for i in range(len(primerMitad)):
                tab_ejecucion.chequeroDuplica(x,y,i)
                tab_ejecucion.EscribirEnTablero(x,y,g,primerMitad[i])
                y=y+1
            y=y+1
            for i in range(len(segundoMitad)):
                tab_ejecucion.chequeroDuplica(x,y,i)
                tab_ejecucion.EscribirEnTablero(x,y,g,segundoMitad[i])
                y=y+1

    def PuntosPalabra_Maquina(self,palabra,tab):
        '''Calculo los puntos de la palabra ingresada'''
        pts=0
        archivo= open("puntaje_letras.json","r")
        dicc1=json.load(archivo)
        archivo.close()
        lista=tab.get_duplica()
        lista1=tab.get_triplica()
        for i in palabra:
            num=dicc1[i]
            num=num[0]
            if i in lista:
                num=num*2
            if i in lista1:
                num=num*3
            pts+=num
        return pts

    def Actualizar_Puntaje(self,AV,palabra,tab):
        '''Actuliza el puntaje total de la maquina'''
        puntos_maquina = self.PuntosPalabra_Maquina(palabra,tab)
        palabra_y_puntaje_maquina = palabra + ' ' +str(puntos_maquina)
        self._puntaje_total = self._puntaje_total + puntos_maquina
        return palabra_y_puntaje_maquina

    def evaluar_donde(self,tab_ejecucion,g,l):
        '''Evalua donde es posible colocar la palabra'''
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
        '''Busca  en el conjunto dependiendo del nivel elegido'''
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

    def EncontrarPalabra(self,nivel,TE):
        '''Manda a buscar una palabra en el conjunto seleccionado dependiendo del nivel'''
        listaDeLetrasEnElTablero=TE.get_lista_de_letras_en_tablero()
        tupla=("",False,[])
        letra=""
        if nivel=="Facil":
            tupla=self.buscarEn(lexicon)
            if not tupla[1]:
                tupla=self.buscarEn(spelling)
        if nivel=="Medio":
            tupla=self.buscarEn(verbs)
            if not tupla[1]:
                archivo=open ("adjetivos.json","r")
                adjetivos=json.load(archivo)
                archivo.close()
                tupla=self.buscarEn(adjetivos)
        if nivel=="VB":
            tupla=self.buscarEn(verbs)
        if nivel=="JJ":
            archivo=open ("adjetivos.json","r")
            adjetivos=json.load(archivo)
            archivo.close()
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

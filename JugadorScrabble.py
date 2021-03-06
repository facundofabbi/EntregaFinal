import json
import random as r
from JugadorGenerico import Padre

class Jugador(Padre):

    def __init__(self,nom="Jugador",turno=False):
        super().__init__(turno)
        self._nombre=nom
        self._ID=2
        self._Letras_Turno=[]  #ya use
        self._boton_seleccionado=False

    def set_nombre(self,nombre):
        self._nombre=nombre
    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre=nombre
    def get_id(self):
        return self._ID
    def FinTurno(self):
        self._Letras_Turno=[]
        super().set_turno(False)

    def get_Ya_Use(self):
        return self._Letras_Turno

    def eliminar_letra_usada(self,dato):
        self._Letras_Turno.remove(dato)

    def set_letra_usada(self,letra):
        self._Letras_Turno.append(letra)

    def get_boton_seleccionado(self):
        return self._boton_seleccionado

    def set_boton_seleccionado(self,booleano):
        self._boton_seleccionado=booleano

    def PuntosPalabraJugador(self,tab_Ejecucuon):
        '''Evalua si la palabra fue ingresada en un casillero especial y devuelve los puntos actualizados'''
        pts=0
        archivo= open("Almacenamiento/puntaje_letras.json","r")
        dicc1=json.load(archivo)
        archivo.close()
        palabra=tab_Ejecucuon.get_palabra()
        lista=tab_Ejecucuon.get_duplica()
        lista1=tab_Ejecucuon.get_triplica()
        lista2=tab_Ejecucuon.get_resta()
        for i in palabra:
            num=dicc1[i]
            num=num[0]
            if i in lista:
                num=num*2
            if i in lista1:
                num=num*3
            if i in lista2:
                num=0
            pts+=num
        return pts

    def Actualizar_Puntaje(self,AV,tab):
        '''Actualiza el puntaje y agrega la palabra en la lista del jugador'''
        puntos = self.PuntosPalabraJugador(tab)
        palabra_y_puntaje = tab.get_palabra() + ' ' +str(puntos)
        self._puntaje_total = self._puntaje_total + puntos
        return palabra_y_puntaje

    def chequetoLetra(self,letra):
        '''Cheque si la letra esta en la bolsa'''
        archivo=open ("Almacenamiento/bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        if letra in datos.keys():
            return True
        else :
            return False

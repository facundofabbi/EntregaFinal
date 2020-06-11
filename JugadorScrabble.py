import json
import random as r
from JugadorGenerico import Padre

class Jugador(Padre):

    def __init__(self,turno=False):
        super().__init__(turno)

        self._Letras_Turno=[]  #ya use
        self._boton_seleccionado=False

    def FinTurno(self):
        self._Letras_Turno=[]
        super().set_turno(False)

    def get_Ya_Use(self):
        return self._Letras_Turno

    def set_letra_usada(self,letra):
        self._Letras_Turno.append(letra)

    def get_boton_seleccionado(self):
        return self._boton_seleccionado

    def set_boton_seleccionado(self,booleano):
        self._boton_seleccionado=booleano


    def chequetoLetra(self,letra):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        if letra in datos.keys():
            return True
        else :
            return False

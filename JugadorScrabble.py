import json
import random as r

class Jugador:

    def __init__(self,turno=False):
        self._atril = []
        self._turno = turno
        self._Letras_Turno=[]  #ya use
        self._puntaje_Jugador=0
        self._letra=""
        self._boton_seleccionado=False




    def FinTurno(self):
        self._Letras_Turno=[]
        self._turno=False
    def get_boton_seleccionado(self):
        return self._boton_seleccionado
    def set_boton_seleccionado(self,booleano):
        self._boton_seleccionado=booleano
    def get_letra(self):
        return self._letra
    def set_letra(self,l):
        self._letra=l
    def get_Ya_Use(self):
        return self._Letras_Turno
    def set_letra_usada(self,letra):
        self._Letras_Turno.append(letra)

    def get_atril(self):
        return self._atril

    def set_Atril(self,lista):
        self._atril=lista

    def BuscarEnLaBolsa(self,cantidad):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        print(datos)
        lista=[]
        llaves=datos.keys()
        for i in range(cantidad):
            letra= r.choice(list(llaves))
            listaNum=datos[letra]
            num=listaNum[0]
            num = num-1
            datos[letra]=[num]
            lista.append(letra)
            if num==0:
                del datos[letra]
        archivo=open ("bolsa.json","w")
        json.dump(datos,archivo,indent=1)
        archivo.close()
        return  lista

    def CambioLetras(self,LetrasCambio=[]):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        for i in LetrasCambio:
            try:
                ListaNum=datos[i]
                num=ListaNum[0]
                num=num+1
                datos[i]=[num]
            except KeyError:
                datos[i]=[1]
        archivo=open ("bolsa.json","w")
        json.dump(datos,archivo,indent=1)
        archivo.close()
        lista= self.BuscarEnLaBolsa(len(LetrasCambio))
        return lista




    def chequetoLetra(self,letra):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        if letra in datos.keys():
            return True
        else :
            return False

    def Actualizar_Puntaje(self,puntaje_nuevo):
        self._puntaje_Jugador+=puntaje_nuevo

    def get_puntos_jugador(self):
        return self._puntaje_Jugador

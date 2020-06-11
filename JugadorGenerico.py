import json
import random as r

class Padre:

    def __init__(self,turno):
        self._atril = []
        self._turno = turno
        self._puntaje_Jugador=0
        self._letra=""

    def Actualizar_Puntaje(self,puntaje_nuevo):
        self._puntaje_Jugador+=puntaje_nuevo

    def get_puntos_jugador(self):
        return self._puntaje_Jugador

    def get_letra(self):
        return super()._letra

    def set_letra(self,l):
        self._letra=l

    def get_atril(self):
        return self._atril

    def set_Atril(self,lista):
        self._atril=lista

    def set_remove_atril(self,letra):
        self._atril.remove(letra)

    def set_agregar_atril(self,letra):
        self._atril.append(letra)

    def set_turno(self,turno):
        self._turno=turno
    def CambioLetras(self,LetrasCambio=[]):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        for i in LetrasCambio:
            try:
                ListaNum=datos[i]
                num=ListaNum[0] + 1
                datos[i]=[num]
            except KeyError:
                datos[i]=[1]
        archivo=open ("bolsa.json","w")
        json.dump(datos,archivo,indent=1)
        archivo.close()
        lista= self.BuscarEnLaBolsa(len(LetrasCambio))
        return lista


    def CambioLetrasSinDevolver(self,LetrasCambio=[]):      #no devuelvo las letras al json
        lista= self.BuscarEnLaBolsa(len(LetrasCambio))
        return lista

    def BuscarEnLaBolsa(self,cantidad):
        archivo=open ("bolsa.json","r")
        datos=json.load(archivo)
        archivo.close()
        #print(datos)
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

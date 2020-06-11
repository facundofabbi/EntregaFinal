import json
import random as r



class Jugador:

    def __init__(self,turno=False):
        self._atril = []
        self._turno = turno
        self._Letras_Turno=[]
        self._id_letra=[]
        self._key_usadas=[]
        self._puntaje_Jugador=0
        # self._puntos=0

    # def inicio(self):
    #     lista=BuscarEnLaBolsa(7)
    #     self._atril=lista
    #     self._truno=True

    def get_Tablero_Actual(self):
        return self._atril

    def set_Atril(self,lista):
        self._atril=lista
    def set_key_usadas(self,key):
        self._key_usadas.append(key)
    def get_key_usadas(self):
        return self._key_usadas

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

    def Ya_use(self,letra):
        self._Letras_Turno.append(letra)

    def get_id(self):
        return self._id_letra

    def id_usados_en_turno(self,id):
        self._id_letra.append(id)


    def get_Ya_Use(self):
        return self._Letras_Turno



    def FinTurno(self):
        self._Letras_Turno=[]
        self._turno=False
        self._key_usadas=[]




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

if __name__ == 'main':
    print("")

import json


class Top:

    def __init__(self):
        self._lista_ganadores = []


    def get_lista_ganadores(self):
        return self._lista_ganadores

    def modificar_lista_ganadores(self,tupla):
        archivo = open ('TopJugadores.json','r')
        self._lista_ganadores = json.load(archivo)
        archivo.close()
        pos = -1
        for i in range(10):
            tuplita = self._lista_ganadores[i]
            if(tuplita[1]<tupla[1]):
                pos = i
                break
        cont = 9
        if pos != -1:
            while(cont>pos):
                self._lista_ganadores[cont] =self._lista_ganadores[cont-1]
                cont = cont - 1
            self._lista_ganadores[pos]=tupla
            archivo = open ('TopJugadores.json','w')
            json.dump(self._lista_ganadores,archivo)
            archivo.close()

import PySimpleGUI as sg
import random as r


class columna:
    def __init__(self,window,cant):
        self._muchosbotones=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","18","19","20",
        "21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46",
        "47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72",
        "73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89"]
        self._deshabilitados=[]
        self._cant=0
        self.sacar_primer_atril(window,cant)
    def set_cant(self,cont):
        self._cant=self._cant+cont
    def get_cant(self):
         return self._cant

    def sacar_primer_atril(self,window,cant):
        for i in range (cant):
            dato=r.choice(self._muchosbotones)
            self.sacar_llave(dato)
            self.agregar_deshabilitado(dato)
            window.FindElement(dato).Update(button_color=('black','#092F50'))

    def get_keys(self):
        return self._muchosbotones


    def get_deshabilitados (self):
        return self._deshabilitados
    def set_deshabilitados(self,deshabilitados):
        self._desabilitados=deshabilitados

    def agregar_deshabilitado(self,key):
        self._deshabilitados.append(key)
    def sacar_llave(self,dato):
        self._muchosbotones.remove(dato)

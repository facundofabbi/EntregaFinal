from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
from random import choice
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



    def _calcular_lugar_der_aba(self,pos,tab,x,y,ok):
        abajo_derecha = len(self._palabra) - pos
        for i in range(abajo_derecha):
            if tab.chequeo_selected(x+i,y) == False and ok:
                palabra_en_x = True
            else:
                ok = False
                palabra_en_x = False
        if palabra_en_x and self._calcular_lugar_izq_arri(pos-1,tab,x,y,True):
            return "x"
        else:
            ok = True
            for i in range(abajo_derecha):
                if tab.chequeo_selected(x,y+1) == False and ok:
                    palabra_en_y = True
                else:
                    ok = False
                    palabra_en_y= False
            if palabra_en_y and self._calcular_lugar_izq_arri(pos-1,tab,x,y,False):
                return "y"
        return ""



    def _calcular_lugar_izq_arri(self,pos,tab,x,y,ok):
        if ok:
            for i in range(pos):
                if x - i >=0:
                    if tab.chequeo_selected(x-i,y) == False and ok:
                        ok = True
                    else:
                        ok = False
                        break
            return ok
        else:
            for i in range(pos):
                if y - i >=0:
                    if tab.chequeo_selected(x,y-1) == False and not ok:
                        ok = False
                    else:
                        ok = True
                        break
            return not ok


    def lugar_random(self,tab,g):
        num = len(self._palabra)
        box_x = -1
        ok = False
        cant_libres = 0
        for x in range(0,14):
            for y in range (0,14):
                if tab.chequeo_selected(x,y) == False:
                    if cant_libres < num:
                        cant_libres = cant_libres+1
                else:
                    cant_libres = 0
                if cant_libres == num:
                    ok=True
                    box_x = x
                    box_y = y
                    break
        if box_x != -1:
            for y in range(0,14):
                for x in range (0,14):
                    if tab.chequeo_selected(x,y) == False:
                        if cant_libres < num:
                            cant_libres = cant_libres+1
                    else:
                        cant_libres = 0
                    if cant_libres == num:
                        box_x=x
                        box_y = y
                        break

        for i in self._palabra:
            self._EscribirEnTablero(box_x,box_y,g,i,tab)
            if ok:
                box_x = box_x + 1
            else:
                box_y = box_y + 1



    def _EscribirEnTablero(self,box_x,box_y,g,letra,tab):
        tab.set_casillero_selected(box_x,box_y) # esto es para no volver al mismo casillero
        id = g.DrawText(letra, (box_x * 15 + 14, box_y * 15+ 14))
        tab.set_text_box_read(box_x,box_y,id)
        tab.id_usados_en_turno((box_x,box_y))



    def evaluar_donde(self,tab_ejecucion,g,l):
        box_x = -1
        box_y = -1
        ok = False
        id_usados = []
        pos=0
        if super().get_letra != "":
            for x in range(0,14):
                for y in range(0,14):
                    if l== tab_ejecucion.get_coordenadas_en_tablero(x,y):
                        box_x = x
                        print("ALGOOOOOOOOOOOO")
                        box_y = y
            for i in range(len(self._palabra)):
                if super().get_letra == self._palabra[i]:
                    pos = i+1

            if self._calcular_lugar_der_aba(pos,tab_ejecucion,box_x,box_y,True) == "x":       # EVALUAMOS EN LA X
                num = pos-2
                for i in range (pos-1):
                    box_x = box_x-1
                    self._EscribirEnTablero(box_x,box_y,g,self._palabra[num],tab_ejecucion,g)
                    num=num-1
                q = len(self._palabra) - pos
                num = pos+1
                for i in range (q-1):
                    box_x = box_x+1
                    self._EscribirEnTablero(box_x,box_y,g,self._palabra[num],tab_ejecucion)
                    num=num+1


            elif self._calcular_lugar_der_aba(pos,tab_ejecucion,box_x,box_y,True) == "y":       # EVALUAMOS EN LA Y
                num = pos-2
                for i in range (pos-1):
                    box_y = box_y-1
                    self._EscribirEnTablero(box_x,box_y,g,self._palabra[num],tab_ejecucion,g)
                    num=num-1
                q = len(self._palabra) - pos
                num = pos+1
                for i in range (q):
                    box_y = box_y+1
                    self._EscribirEnTablero(box_x,box_y,g,self._palabra[num],tab_ejecucion)
                    num=num+1
            else:
                 self.lugar_random(tab_ejecucion,g)
        else:
             self.lugar_random(tab_ejecucion,g)

    def buscarEn(self,nombre):
        for palabra in nombre:
            ya_usadas=[]
            sirve=True
            for i in palabra:
                if i.upper() in super().get_atril() and not i in ya_usadas:
                    ya_usadas.append(i)
                else:
                    sirve=False
            if sirve and len(palabra)>1:
                nuevo = super().BuscarEnLaBolsa(len(ya_usadas))
                for letra in super().get_atril():
                    for i in ya_usadas:
                        if letra == i:
                            ya_usadas.remove(i)
                            super().set_remove_atril(letra)
                for i in nuevo:
                    super().set_agregar_atril(i)
                break
        if sirve:
            return (palabra,True,ya_usadas)
        else:
            return("",False,[])



    def EncontrarPalabra(self,nivel,listaDeLetrasEnElTablero):
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
        if not tupla[1]:
            print("aca tendriamos q hacer q cambie letras .... porq no encontro niguna palabra :D")
            print(tupla[0] , " ASDASDASDASD")
        print(tupla[0])
        print(tupla[1])

        self._palabra=tupla[0]
        super().set_letra(letra)
        return letra

from pattern.es import spelling
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
from random import choice
import json

class Maquina:

    def __init__(self,turno):
        self._palabra = ""
        self._turno = turno
        self._letra = ""
        self._atril = []
        self._puntaje_Jugador=0

    def fin_turno(self):
        self._palabra = ""
        self._turno = turno
        self._letra = ""

    def _calcular_lugar_der_aba(self,pos,tab,x,y,ok):
        abajo_derecha = len(self._palabra) - pos
        for i in abajo_derecha:
            if tab.chequeo_selected(x+i,y) == False and ok:
                palabra_en_x = True
            else:
                ok = False
                palabra_en_x = False
        if palabra_en_x and self._calcular_lugar_izq_arri(pos-1,tab_ejecucion,box_x,box_y,True):
            return "x"
        else:
            ok = True
            for i in abajo_derecha:
                if tab.chequeo_selected(x,y+1) == False and ok:
                    palabra_en_y = True
                else:
                    ok = False
                    palabra_en_y= False
            if palabra_en_y and self._calcular_lugar_izq_arri(pos-1,tab_ejecucion,box_x,box_y,False):
                return "y"
        return ""



    def _calcular_lugar_izq_arri(self,pos,tab,x,y,ok):
        if ok:
            for i in pos:
                if x - i >=0:
                    if tab.chequeo_selected(x-i,y) == False and ok:
                        ok = True
                    else:
                        ok = False
                        break
            return ok
        else:
            for i in pos:
                if y - i >=0:
                    if tab.chequeo_selected(x,y-1) == False and !ok:
                        ok = False
                    else:
                        ok = True
                        break
            return !ok


    def lugar_random(self,tab,g):
        num = len(self._palabra)
        box_x = -1
        ok = False
        for x in range(0,14):
            for y in range (0,14):
                if tab.chequeo_selected(x,y) == False:
                    if cant_libres < num:
                        cant_libres = cant_libres+1
                else:
                    cant_libres = 0
                if cant_libres = num:
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
                    if cant_libres = num:
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
        tab.set_text_box_read(box_x,box_y,g.DrawText(letra, (box_x * self._Tam_Celda + 14, box_y * self._Tam_Celda+ 14)))
        tab.id_usados_en_turno((box_x,box_y))



    def evaluar_donde(self,tab_ejecucion,g):
        box_x = -1
        box_y = -1
        ok = False
        id_usados = []
        if self._letra != "":
            for x in range(0,14):
                for y in range(0,14):
                    if letra == tab_ejecucion.get_coordenadas_en_tablero(x,y)
                        box_x = x
                        box_y = y
            for i in range(len(self._palabra)):
                if self._letra == self._palabra[i]:
                    pos = i+1

            if self._calcular_lugar_der_aba(pos,tab_ejecucion,box_x,box_y,True) == "x":       # EVALUAMOS EN LA X
                num = pos-2
                for i in range (pos-1):
                    box_x = box_x-1
                    self._EscribirEnTablero(box_x,box_y,g,self._palabra[num],tab_ejecucion,g)
                    num=num-1
                q = len(self._palabra) - pos
                num = pos+1
                for i in range (q):
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
                 lugar_random(tab_ejecucion,g)
        else:
             lugar_random(tab_ejecucion,g)

        def buscarEn(self,nombre):
    for palabra in nombre:
        ya_usadas=[]
        sirve=True
        for i in palabra:
            if i in self._atril and not i in ya_usadas:
                ya_usadas.append(i)
            else:
                sirve=False
        if sirve and len(palabra)>1:
            #ACA SE ELIMINA LAS LETRAS Y SE RELEAN LA CANTIDAD Q SE USARON
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
        if nivel=="FACIL":
            tupla=self.buscarEn(lexicon)
            if not tupla[1]:
                tupla=self.buscarEn(spelling)
        if nivel=="MEDIO":
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

        self._palabra=tupla[0]
        self._letra=letra

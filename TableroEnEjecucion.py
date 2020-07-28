import InterfazGrafica as IG
class Turno:
    Llaves=["boton0","boton1","boton2","boton3","boton4","boton5","boton6",]
    botones_maquina=["m1","m2","m3","m4","m5","m6","m7"]
    def __init__(self):
        self._derecha = True
        self._abajo= True
        self._lista_de_letras_en_tablero=[]
        self._duplica_palabra=[]
        self._triplica_palabra=[]
        self._palabra=""
        self._desbugeo=True
        self._id_usados_en_turno=[]
        self._key_usadas=[]
        self._matriz=[]
        self._coordenadas_en_tablero=[]
        self._selected=[]
        self._text_box=[]
        self._Tam_Celda=15
        self._matrizMultiplica=[]
        self._posicionLetra1=(-20,-20)
        self._Casilleros_Especiales={}
        self._primera_letra_en_el_turno_posicion=""
        self._letra_anterior_a_la_primera=True
        self._primer_letra=True
        for i in range(0,15):
            self._coordenadas_en_tablero.append([""]*15 )
            self._matriz.append([0]*15)
            self._selected.append([False]*15)
            self._text_box.append([""]*15)
            self._matrizMultiplica.append([0]*15)

    def get_botones_maquina(self):
        return self.botones_maquina

    def set_primer_letra(self):
        self._primer_letra=False
    def get_primer_letra(self):
        return self._primer_letra
    def get_letra_anterior_a_la_primera(self):
        return self._letra_anterior_a_la_primera
    def set_letra_anterior_a_la_primera(self):
        self._letra_anterior_a_la_primera=False
    def set_desbugeo(self):
        self._desbugeo=False
    def get_desbugeo(self):
        return self._desbugeo
    def set_palabra_TODA(self,pal):
        self._palabra=pal
    def chequeo_selected(self,x,y):
        return self._selected[x][y]
    def get_tablero_booleano(self):
        return self._selected
    def set_casillero_selected(self ,x,y):
        self._selected[x][y]=True
    def set_text_box_read(self,x,y,id):
        self._text_box[x][y]=id
    def get_matrizMultiplica(self):
        return self._matrizMultiplica
    def set_matrizMultiplica(self,m):
        self._matrizMultiplica=m
    def FinTurno(self):
        self._posicionLetra1=(-20,-20)
        self._letra_anterior_a_la_primera=True
        self._primera_letra_en_el_turno_posicion=""
        self._derecha = True
        self._abajo= True
        self._palabra=""
        self._id_usados_en_turno=[]
        self._key_usadas=[]
        self._duplica_palabra =[]
        self._triplica_palabra = []
        self._desbugeo=True
        self._primer_letra=True
    def set_palabra(self,letra):
        self._palabra+=letra
    def get_llaves(self):
        return self.Llaves
    def get_posicionLetra_anterior(self):
        return self._posicionLetra1
    def set_posicionLetra_anterior(self,tupla):
        self._posicionLetra1=tupla
    def get_tam_Celda(self):
        return  self._Tam_Celda
    def set_Casilleros_Especiales(self,x):
        self._Casilleros_Especiales=x
    def get_Casilleros_Especiales(self):
        return self._Casilleros_Especiales
    # def Agrego_a_Matriz(self,x,y,g):
    def get_matriz(self):
        return self._matriz
    def set_matriz(self,matriz):
        self._matriz=matriz
    def get_selected(self):
        return self._selected
    def set_selected(self,selected):
        self._selected=selected
    def get_text_box(self):
        return self._text_box
    def set_text_box(self,text_box):
        self._text_box=text_box

    def Actualizo_selected(self,x,y,booleano):
        selected[x][y]=booleano
    def get_selected_posicion(self,x,y):
        return self._selected[x][y]

    def Agrego_a_text_box(self,x,y,g):
        text_box[x][y] = g.DrawText(letra, (x * self._tam_celda + 12, y * self._tam_celda + 11))




    def set_key_usadas(self,key):
        self._key_usadas.append(key)
    def get_key_usadas(self):
        return self._key_usadas
    def eliminar_key_usada(self,dato):
        self._key_usadas.remove(dato)
    def get_id(self):
        return self._id_usados_en_turno

    def id_usados_en_turno(self,id):
        ''' El ID que llega es una tupla con las coordenas x , y para buscar en la matriz q contiene
        los id(matriz) de las figuras en el grafico '''
        self._id_usados_en_turno.append(id)

    def get_derecha(self):
        return self._derecha
    def get_abajo(self):
        return self._abajo

    def set_derecha(self):
        self._derecha = False
    def set_abajo(self):
        self._abajo=False

    def chequeroDuplica(self,x,y,letra):
        try:
            if self._Casilleros_Especiales[(x,y)]=="DP":
                self._duplica_palabra.append(letra)
            else :
                if self._Casilleros_Especiales[(x,y)]=="TP":
                    self._triplica_palabra.append(letra)
        except KeyError:
            print("")
    def get_duplica(self):
        return self._duplica_palabra
    def get_triplica(self):
        return self._triplica_palabra
    def agregar_Letra(self,letra):
        self._palabra+=letra
    def get_palabra(self):
        return self._palabra
    def set_lista_de_letras_en_tablero(self,letra):
        self._lista_de_letras_en_tablero.append(letra)
    def get_lista_de_letras_en_tablero(self):
        return self._lista_de_letras_en_tablero
    def get_coordenadas_en_tablero(self,x,y):
        return self._coordenadas_en_tablero[x][y]
    def set_coordenadas_en_tablero(self,x,y):
        self._coordenadas_en_tablero[x][y]=""
    def get_coordenadas_en_tablero_lista(self):
        return self._coordenadas_en_tablero
    def set_coordenadas_en_tablero_lista(self,coordenadas_en_tablero_lista):
        self._coordenadas_en_tablero=coordenadas_en_tablero_lista

    def set_primera_letra_palabra(self,tupla):
        self._primera_letra_en_el_turno_posicion=tupla
    def get_primera_letra_palabra(self):
        return self._primera_letra_en_el_turno_posicion





    def Armar_palabra_y(self,box_x,box_y):
        primer_letra=self._primera_letra_en_el_turno_posicion
        primer_x=primer_letra[0]
        primer_y=primer_letra[1]
        anterior=self._posicionLetra1
        anterior_x=anterior[0]
        anterior_y=anterior[1]
        ok_dos_veces_la_primera=True
        if self.get_coordenadas_en_tablero(primer_x,primer_y-1)!="" and  self.get_letra_anterior_a_la_primera():
            self.set_letra_anterior_a_la_primera()
            ok_dos_veces_la_primera=False
            self.set_primer_letra()
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x,primer_y-1))
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x,primer_y))
        if  self.get_primer_letra():
            self.set_primer_letra()
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x,primer_y))
        if  box_x==anterior_x and box_y-2==anterior_y:
            self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y+1))
            self.set_palabra(self.get_coordenadas_en_tablero(box_x,box_y))
        else :
            self.set_palabra(self.get_coordenadas_en_tablero(box_x,box_y))



    def ultima_letra(self):
        anterior=self._posicionLetra1
        anterior_x=anterior[0]
        anterior_y=anterior[1]
        if self.get_abajo()and self.get_coordenadas_en_tablero(anterior_x,anterior_y+1)!="" :
            self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y+1))
        if self.get_derecha() :
            self.set_palabra(self.get_coordenadas_en_tablero(anterior_x+1,anterior_y))

    def palabra_corta(self):
        ''' a este modulo le falta evaluar q palabra se pone cuando es de dos letras , evaluar en pattern
        y setear la palabra'''
        anterior=self._posicionLetra1
        anterior_x=anterior[0]
        anterior_y=anterior[1]
        if self.get_abajo():
            ok1=True
            if self.get_coordenadas_en_tablero(anterior_x,anterior_y-1)!="" and self.get_coordenadas_en_tablero(anterior_x,anterior_y+1)!="":
                ok1=False
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y-1))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y+1))
            if self.get_coordenadas_en_tablero(anterior_x,anterior_y-1)!="" and ok1:
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y-1))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
            if self.get_coordenadas_en_tablero(anterior_x,anterior_y+1)!="" and ok1:
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y+1))
        if self.get_derecha():
            ok1=True
            if self.get_coordenadas_en_tablero(anterior_x-1,anterior_y)!="" and self.get_coordenadas_en_tablero(anterior_x+1,anterior_y)!="":
                ok1=False
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x-1,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x+1,anterior_y))
            if self.get_coordenadas_en_tablero(anterior_x-1,anterior_y)!="" and ok1:
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x-1,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
            if self.get_coordenadas_en_tablero(anterior_x+1,anterior_y)!="" and ok1:
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x,anterior_y))
                self.set_palabra(self.get_coordenadas_en_tablero(anterior_x+1,anterior_y))

    def Armar_palabra_x(self,box_x,box_y):
        primer_letra=self._primera_letra_en_el_turno_posicion
        primer_x=primer_letra[0]
        primer_y=primer_letra[1]
        anterior=self._posicionLetra1
        anterior_x=anterior[0]
        anterior_y=anterior[1]
        ok_dos_veces_la_primera=True
        if self.get_coordenadas_en_tablero(primer_x-1,primer_y)!="" and  self.get_letra_anterior_a_la_primera():
            self.set_letra_anterior_a_la_primera()
            ok_dos_veces_la_primera=False
            self.set_primer_letra()
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x-1,primer_y))
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x,primer_y))
        if  self.get_primer_letra():
            self.set_primer_letra()
            self.set_palabra(self.get_coordenadas_en_tablero(primer_x,primer_y))
        if  box_x-2==anterior_x and box_y==anterior_y:
            self.set_palabra(self.get_coordenadas_en_tablero(anterior_x+1,anterior_y))
            self.set_palabra(self.get_coordenadas_en_tablero(box_x,box_y))
        else :
            self.set_palabra(self.get_coordenadas_en_tablero(box_x,box_y))





    def EscribirEnTableroPosponer(self,box_x,box_y,g):
        letra=self.get_coordenadas_en_tablero(box_x,box_y)
        self._text_box[box_x][box_y] = g.DrawText(letra.upper(), (box_x * self._Tam_Celda+14, box_y * self._Tam_Celda +14))

    def EscribirEnTablero(self,box_x,box_y,g,letra):
        if self._selected[box_x][box_y]==False:
        #IG.Check_box(box_x,box_y,g,self._matriz)
            self._lista_de_letras_en_tablero.append(letra.upper())
            self._coordenadas_en_tablero[box_x][box_y]=letra.upper()
            self._selected[box_x][box_y]=True # esto es para no volver al mismo casillero
            self._text_box[box_x][box_y] = g.DrawText(letra.upper(), (box_x * self._Tam_Celda+14, box_y * self._Tam_Celda +14))
            self.id_usados_en_turno((box_x,box_y))

            # matriz=self.get_matriz
            # IG.Check_box(box_x,box_y,g,matriz)
            # IG.Uncheck_box(box_x,box_y,g,matriz)


import InterfazGrafica as IG
class Turno:
    Llaves=["boton0","boton1","boton2","boton3","boton4","boton5","boton6",]
    def __init__(self):
        self._derecha = False
        self._abajo= False
        self._duplica_palabra=[]
        self._triplica_palabra=[]
        self._palabra=""
        self._id_usados_en_turno=[]
        self._key_usadas=[]
        self._matriz=[]
        self._selected=[]
        self._text_box=[]
        self._Tam_Celda=15
        self._posicionLetra1=(-20,-20)
        self._Casilleros_Especiales={}
        for i in range(0,15):
            self._matriz.append([0]*15)
            self._selected.append([False]*15)
            self._text_box.append([""]*15)

    def FinTurno(self):
        self._derecha = False
        self._abajo= False
        self._palabra=""
        self._id_usados_en_turno=[]
        self._key_usadas=[]
    def set_palabra(self,letra):
        self._palabra+=letra
    def get_llaves(self):
        return self.Llaves
    def get_posicionLetra1(self):
        return self._posicionLetra1
    def set_posicionLetra1(self,tupla):
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


    def get_id(self):
        return self._id_letra

    def id_usados_en_turno(self,id):
        ''' El ID que llega es una tupla con las coordenas x , y para buscar en la matriz q contiene
        los id(matriz) de las figuras en el grafico '''
        self._id_usados_en_turno.append(id)

    def get_derecha(self):
        return self._derecha
    def get_abajo(self):
        return self._abajo

    def set_derecha(self):
        self._derecha = True
    def set_abajo(self):
        self._abajo=True

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



    def EscribirEnTablero(self,box_x,box_y,g,letra,Jugador1):
        IG.Check_box(box_x,box_y,g,self._matriz)
        self._selected[box_x][box_y]=True # esto es para no volver al mismo casillero
        self._text_box[box_x][box_y] = g.DrawText(letra, (box_x * self._Tam_Celda + 12, box_y * self._Tam_Celda + 11))
        self.id_usados_en_turno((box_x,box_y))

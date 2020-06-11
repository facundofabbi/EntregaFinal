
class DireccionLetra:
    def __init__(self):
        self._derecha = False
        self._abajo= False
        self._duplica_palabra=[]
        self._triplica_palabra=[]

    def get_derecha(self):
        return self._derecha
    def get_abajo(self):
        return self._abajo

    def set_derecha(self):
        self._derecha = True
    def set_abajo(self):
        self._abajo=True
    def FinTurno(self):
        self._derecha = False
        self._abajo= False
    def chequeroDuplica(self,x,y,dicc,letra):
        try:
            if dicc[(x,y)]=="DP":
                self._duplica_palabra.append(letra)
            else :
                if dicc[(x,y)]=="TP":
                    self._triplica_palabra.append(letra)
        except KeyError:
            print("error")
    def get_duplica(self):
        return self._duplica_palabra
    def get_triplica(self):
        return self._triplica_palabra

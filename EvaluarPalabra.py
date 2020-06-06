from pattern.es import spelling as sp
from pattern.es import lexicon as le
from pattern.es import verbs
from pattern.es import parse



def EvaluarPalabra(palabra,nivel):
    nivel=nivel.upper()
    pal=parse(palabra).split("/")
    aux=pal[1]
    if nivel == "facil":
        if palabra in sp or palabra in le :
            return True
        else:
            return False
    if nivel == "medio":
        if aux=="VB" or aux=="JJ":
            return True
        else:
            return False
    if nivel != "facil" and nivel != "medio":
        if aux == nivel:
            return True
        else:
            return False
#if __name__ == '__main__':
    EvaluarPalabra("lindo","JJ")

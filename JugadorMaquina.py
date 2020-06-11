from pattern.es import spelling as sp
from pattern.es import lexicon
from pattern.es import verbs
from pattern.es import parse
from random import choice



def __init__(self):
    self.__nada=[]


def EncontrarPalabraDeVerbos(lista):
    pal=""
    ya_usadas=[]
    i=6500
    num=len(lexicon.keys())
    lista_palabras=list(lexicon.keys())
    while True :
        i+=1
        if i>=num:
            break
        pal=lista_palabras[i].lower()
        sirve=True
        ya_usadas=[]
        print(pal)
        for j in pal:
            if j in lista:
                ya_usadas.append(j)
                lista.remove(j)
            else:
                sirve=False
        if sirve:
            break
        else:
            for h in ya_usadas:
                lista.append(h)
    return pal,ya_usadas















lista=["r","c","e","r","o","r","a"]
a=EncontrarPalabraDeVerbos(lista)
print("laaaa enontreeeee",a)

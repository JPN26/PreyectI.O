from operator import indexOf
from re import A
import re
from ssl import RAND_add
from turtle import shape
from colorama import Fore, init
init()
from colorama import Back, init
init()

from numpy import rint, true_divide

sumaoferta=0
sumademanda=0
destinos2=0
origenes2=0
def getValores(opc,ORI,DES):
    global valores,destinos2,origenes2
    if(opc==1):
        destinos2=DES   
        origenes2=ORI
        valores=[[ORI * DES for x in range(DES)] for y in range(ORI)]
        for x in range(ORI):
          for y in range(DES):
            valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
    elif(opc==2):
        destinos2=DES   
        origenes2=ORI+1
        valores=[[(ORI+1) * DES for x in range(DES)] for y in range(ORI+1)]
        for x in range(ORI+1):
          for y in range(DES):
            if(x==(ORI)):
                valores[x][y]=0
            else:
                valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
    else:
        destinos2=DES+1
        origenes2=ORI
        valores=[[ORI * (DES+1) for x in range(DES+1)] for y in range(ORI)]
        for x in range(ORI):
          for y in range(DES+1):
            if(y==(DES)):
                valores[x][y]=0
            else:
                valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
def getOferta(num):
    global sumaoferta
    oferta = []
    for x in range(num):
        aux = int(input(f'\t\t\t\tIntroducir la oferta del origen {x}= '))
        sumaoferta+=aux
        oferta.append(aux)
    return oferta

def getDemandas(num):
    global sumademanda
    demanda = []
    for x in range(num):
        aux = int(input(f'\t\t\t\tIntroducir la demanda del destino {x}= '))
        sumademanda+=aux
        demanda.append(aux)
    return demanda

def getComparar(num2,num1):
    if(num2==num1):return 1
    else:
        if(num2>num1):
            oferta.append(num2-num1)
            return 2
        else:
            demanda.append(num1-num2)
            return 3

def imprimirValores(origenes, destinos, valores, oferta, demanda):
     for x in range(origenes+2):
        for y in range(destinos+2):
            if x==0:
                if y==0:
                    print('', end="\t")
                elif y==(destinos+1):
                    print('  Oferta')
                else:
                    print(f'  Destino {y}', end="\t")
            elif x==(origenes+1):
                if y==0:
                    print('Demanda ', end=" ")
                elif(y == destinos + 1):
                    print('\n')
                else:
                    print(f'  {demanda[y-1]}\t', end="\t")
            else:
                if y==0:
                    print(f'Origen {x}', end=" ")
                elif y==(destinos+1):
                    print(f'  {oferta[x-1]}', end="\n")
                else:
                    print(f'  {valores[x-1][y-1]}\t', end="\t")

def esquinaNoroeste(origenes, destinos, valores, oferta, demanda):
    res = []
    val = []
    x = 0
    y = 0
    while (x < origenes and y < destinos):
        #Se consigue la esquina noroeste
        nor = valores[x][y]
        print(f'La esquina noroeste en este caso es: {nor}')
        if(oferta[x] > demanda[y]):
            #La oferta es mayor que la demanda en este caso
            oferta[x] = oferta[x] - demanda[y]
            res.append(valores[x][y])
            print(f'La demanda {demanda[y]} se elimina')
            val.append(demanda[y])
            #Se sigue a la siguiente columna
            y += 1
        elif(oferta[x] < demanda[y]):
            #La demanda es mayor que la oferta en este caso
            demanda[y] = demanda[y] - oferta[x]
            res.append(valores[x][y])
            print(f'La oferta {oferta[x]} se elimina')
            val.append(oferta[x])
            #Se sigue a la siguiente columna
            x += 1


        elif(oferta[x] == demanda[y]):
            #La demanda y la oferta son iguales
            res.append(valores[x][y]) #Se guarda el valor de esta esquina noroeste
            val.append(oferta[x])#Se guarda el valor de oferta demanda usado
            print(f'La demanda y la oferta se elimina')
            #Se sigue con la siguiente columna e hilera
            x += 1
            y += 1

    res.extend(val)
    return res

def imprimirResultados(res):
    y = int(len(res)/2)
    mitad = y
    n = 0
    print(f'La mitad de {len(res)} es {y}')
    print(f'El resultado es:\n')
    for x in range(y):
        if(x == 0):
            print(f'z = ({res[x]} * {res[y]}) ', end="")
            n += res[x] * res[y]
        elif(x == mitad - 1):
            y += 1
            n += res[x] * res[y]
            print(f'+ ({res[x]} * {res[y]}) = {n}', end='\n')
        else:
            y += 1
            print(f'+ ({res[x]} * {res[y]}) ', end='')
            n += res[x] * res[y]

def Esquina():

    origenes=int(input(Fore.RED +"\t\t\t\tIntroducir el numero de origenes.  "))
    destinos=int(input(Fore.RED +"\t\t\t\tIntroducir el numero de destino.   "))
    oferta=getOferta(origenes)
    demanda=getDemandas(destinos)
    comparativa=getComparar(sumademanda,sumaoferta)
    valores=getValores(comparativa,origenes,destinos)
    print(comparativa)
    print("origenes ",origenes," destinos ",destinos2)
    imprimirValores(origenes2, destinos2, valores, oferta, demanda)
    resultados=esquinaNoroeste(origenes2, destinos2, valores, oferta, demanda)
    imprimirResultados(resultados)
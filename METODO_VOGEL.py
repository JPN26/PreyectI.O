from ctypes.wintypes import PINT
from colorama import Fore, init


import numpy as np
import heapq
sumaoferta=0
sumademanda=0
destinos2=0
origenes2=0
res = []
val = []
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

def MetodoVogel(origenes, destinos, valores, oferta, demanda):
    global res 
    global val 
    while(origenes>1 and destinos>1):
        x=0
        posiciondeoferta=0
        posiciondedemanda=0
        y=0
        menor=valores[0][0]
        penalizacionfilas=[]
        penalizacioncolumnas=[]
        p1filas=[]
        p1columas=[]
        mayor=0

        for x in range(destinos):
            for y in range(origenes):
                penalizacionfilas.append(valores[y][x])
            penalizacionfilas=(heapq.nsmallest(2,penalizacionfilas))
            penalizacionfilas=penalizacionfilas[1]-penalizacionfilas[0]
            p1filas.append(penalizacionfilas)
            penalizacionfilas=[]
        print(f'filas p1 {p1filas}')
        for y in range(origenes):
            for x in range(destinos):
                penalizacioncolumnas.append(valores[y][x])
            penalizacioncolumnas=(heapq.nsmallest(2,penalizacioncolumnas))
            penalizacioncolumnas=penalizacioncolumnas[1]-penalizacioncolumnas[0]
            p1columas.append(penalizacioncolumnas)
            penalizacioncolumnas=[]
        print(f'columa p1 {p1columas}')
        if(heapq.nlargest(1,p1filas)>heapq.nlargest(1,p1columas)):
            mayor=heapq.nlargest(1,p1filas)
            indice=p1filas.index(mayor[0])
            print(f'el numero mayor esta en columna {heapq.nlargest(1,p1filas)}  en la posicion {indice}')
            for y in range(origenes):
                if valores[y][indice]<=menor:
                    menor=valores[y][indice]
                    posiciondeoferta=y
                    posiciondedemanda=indice
            print(f'el numero menor es {menor}  en la posicion x {posiciondedemanda} y posy {posiciondeoferta}')        
        else:
            mayor=heapq.nlargest(1,p1columas)
            indice=p1columas.index(mayor[0])
            print(f'el numero mayor esta en columna {heapq.nlargest(1,p1columas)}  en la posicion {indice}')
            for x in range(destinos):
                if valores[indice][x]<=menor:
                    menor=valores[indice][x]
                    posiciondeoferta=indice
                    posiciondedemanda=x
            print(f'el numero menor es {menor}  en la posicion x {posiciondedemanda} y posy {posiciondeoferta}')
        if(demanda[posiciondedemanda]>oferta[posiciondeoferta]):
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(oferta[posiciondeoferta])
            demanda[posiciondedemanda]=demanda[posiciondedemanda]-oferta[posiciondeoferta]
            oferta.remove(oferta[posiciondeoferta])
            valores=np.delete(valores,posiciondeoferta, axis=0)
            origenes-=1
        elif(demanda[posiciondedemanda]<oferta[posiciondeoferta]):
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(demanda[posiciondedemanda])
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            oferta[posiciondeoferta]=oferta[posiciondeoferta]-demanda[posiciondedemanda]
            demanda.remove(demanda[posiciondedemanda])
            valores=np.delete(valores,posiciondedemanda, axis=1)
            destinos-=1   
        else:
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(demanda[posiciondedemanda])
            demanda.remove(demanda[posiciondedemanda])
            oferta.remove(oferta[posiciondeoferta])
            valores=np.delete(valores,posiciondedemanda, axis=1)
            valores=np.delete(valores,posiciondeoferta, axis=0)
            destinos-=1
            origenes-=1
    resto(valores,demanda,oferta,origenes,destinos)

def resto(valores,demanda,oferta,origenes,destinos):
    x=0
    posiciondeoferta=0
    posiciondedemanda=0
    y=0
    menor=valores[0][0]
    while(origenes>0 and destinos>0):
        x=0
        posiciondeoferta=0
        posiciondedemanda=0
        y=0
        menor=valores[0][0]
        for y in range(origenes):
            for x in range(destinos):
                if valores[y][x]<=menor:
                    menor=valores[y][x]
                    posiciondeoferta=y
                    posiciondedemanda=x
        if(demanda[posiciondedemanda]>oferta[posiciondeoferta]):
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(oferta[posiciondeoferta])
            demanda[posiciondedemanda]=demanda[posiciondedemanda]-oferta[posiciondeoferta]
            oferta.remove(oferta[posiciondeoferta])
            valores=np.delete(valores,posiciondeoferta, axis=0)
            origenes-=1
        elif(demanda[posiciondedemanda]<oferta[posiciondeoferta]):
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(demanda[posiciondedemanda])
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            oferta[posiciondeoferta]=oferta[posiciondeoferta]-demanda[posiciondedemanda]
            demanda.remove(demanda[posiciondedemanda])
            valores=np.delete(valores,posiciondedemanda, axis=1)
            destinos-=1   
        else:
            print(f"valor: {valores[posiciondeoferta][posiciondedemanda]}")
            res.append(valores[posiciondeoferta][posiciondedemanda])
            val.append(demanda[posiciondedemanda])
            demanda.remove(demanda[posiciondedemanda])
            oferta.remove(oferta[posiciondeoferta])
            valores=np.delete(valores,posiciondedemanda, axis=1)
            valores=np.delete(valores,posiciondeoferta, axis=0)
            destinos-=1
            origenes-=1


def resultado_final(resulatos,multiplo):
    neto=0
    sumatotal=0
    for i in range(len(resulatos)):
        neto=resulatos[i]*multiplo[i]
        sumatotal+=neto
        print(f"{resulatos[i]} * {multiplo[i]}]")
    print(f"costo minimo: {sumatotal}")
            
def vogel():

    origenes=int(input(Fore.RED +"\t\t\t\tIntroducir el numero de origenes.  "))
    destinos=int(input(Fore.RED+"\t\t\t\tIntroducir el numero de destino.   "))
    oferta=getOferta(origenes)
    demanda=getDemandas(destinos)
    comparativa=getComparar(sumademanda,sumaoferta)
    valores=getValores(comparativa,origenes,destinos)
    print(comparativa)
    print("origenes ",origenes," destinos ",destinos2)
    imprimirValores(origenes2, destinos2, valores, oferta, demanda)
    MetodoVogel(origenes2, destinos2, valores, oferta, demanda)
    resultado_final(res,val)
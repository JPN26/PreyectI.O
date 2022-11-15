from pulp import *
lineal= LpProblem("Problema_de_Otimizacion_Simplex",LpMaximize)
x1=LpVariable("X1", lowBound=0, cat='Integer')
x2=LpVariable("X2", lowBound=0, cat='Integer')

#Funcio Objetivo
lineal += 300*x1+400*x2

#Restricciones 
lineal += 3*x1+3*x2<=120
lineal += 3*x1+6*x2<=180 

lineal.solve()
def total():

    print(f"\t\tEl valor de X1 es: {x1.varValue}  El valor de X2 es {x2.varValue}" )
    print(f"\t\tEl resultado es {300*x1.varValue+400*x2.varValue}")

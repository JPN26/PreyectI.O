def imprimir():


    landa= int(input("Ingrese el ritmo promedio de llegada:  "))
    miu= int(input("Ingrese el ritmo de servisio:  "))


    print (" 1-Probabilida de  N clientes en el sistema")
    n = int(input("Ingrese N: "))
    pn = ((1-(landa/miu))*((landa/miu)**n))
    print (f"El resultado de la probabilidad de clientes en el sistema es:  {pn*100}%")

    print (" 2-Utilizacion promedio del Sistema")
    p = ((landa/miu)*100)
    print (f"El resultado de utilizacion del sistema es: {p} %")

    print (" 3-Numero Promedio de clientes en Sistema")
    l=(landa/(miu-landa))
    print (f"El numero promedio de clientes en el sistema es: {l} ")

    print (" 4-Numero Promedio de clientes en la Fila")
    lq= ((landa**2)/(miu*(miu-landa)))
    print (f"El numero promedio de clientes en la fila es: {round (lq,0)} ")

    print (" 5-Tiempo Promedio Transcurrido en el Sistema")
    w=(1/(miu-landa))
    print (f"El Tiempo Promedio Transcurrido en el Sistema en horas es: {w} hrs o en minutos {w*60} min ")

    print (" 6-Tiempo Promedio de Espera en la fila")
    wq=lq/landa
    print (f"El Tiempo Promedio Transcurrido en la fila en horas es: {wq} hrs o en minutos {wq*60} min ")

from colorama import Fore, init
import os
import simplex,colas,Costo_Minimo,esquina_Noreste,dijstra,METODO_VOGEL

Band=True
os.system('cls')
while (Band==True):

    print(Fore.RED+"\t\t\t\t            ")
    print(Fore.RED+"\t\t\t\t Simulador Metodos de Investigacion de Operaciones")
    print(Fore.RED+"\t\t\t\t                       Atom")
    print(Fore.RED+"\t\t\t\t             Jeison David Pérez Navarro")
    print(Fore.RED+"\t\t\t\t            ")
    print(Fore.RED+"\t\t\t\t                       Menu")
    print(Fore.RED+"\t\t\t\t            ")
    print(Fore.RED+"\t\t\t\t                 1-Metodo Simplex ")
    print(Fore.RED+"\t\t\t\t                 2-Teoria de Colas ")
    print(Fore.RED+"\t\t\t\t                 3-Metodo Esquina Noroeste  ")
    print(Fore.RED+"\t\t\t\t                 4-Costo Minimo  ")
    print(Fore.RED+"\t\t\t\t                 5-Metodo Vogel ")
    print(Fore.RED+"\t\t\t\t                 6-Metodo Dijstra")
    print(Fore.RED+"\t\t\t\t                 7-Salir")
    Opccion = int(input("\t\t\t\t Eliga su Opcion: "))

   
    if (Opccion==1):
        os.system('cls')
        simplex.total()
    elif(Opccion==2):
        os.system('cls')
        colas.imprimir()
    elif(Opccion==3):
        os.system('cls')
        esquina_Noreste.Esquina()
    elif(Opccion==4):
        os.system('cls')
        Costo_Minimo.minimo()
    elif(Opccion==5):
        os.system('cls')
        METODO_VOGEL.vogel()
    elif(Opccion==6):
        os.system('cls')
        dijstra.main()
    elif(Opccion==7):
        os.system('cls')
        Band=False
    else:
        print("Opcion Incorrecta Vuleva A Intentarlo")
        









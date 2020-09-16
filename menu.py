import os


def problema1():
    print("hola mundo")
    
def problema2():
    print("problema2")

def problema3():
    print("problema3")


def menu():
    os.system("pause")
    os.system("cls")
    
    while(True):
        print(" ___________________________________")
        print("|    Servicio de  Estado de Cuenta  |")
        print("|                                   |")
        print("|  ¿Que deseas hacer?               |")
        print("|                                   |")
        print("|  1. problema1                     |")
        print("|  2. problema2                     |")
        print("|  3. problema3                     |")
        print("|  4. salir                         |")
        print("|                                   |")
        print("|   por favor elige una opción      |")
        print("|                                   |")
        print("|___________________________________|")

        opc= int(input("elige una opcion => "))
        if opc == 1:
            problema1()
        elif opc == 2:
            problema2()
        elif opc == 3:
            problema3()  
        elif opc== 4:
            print("hasta luego")
            break
        else:
            print("hasta luego")
            break
   
        os.system("pause")
        os.system("cls")




def main():
    menu()

if __name__ == "__main__":
    pass
    main()
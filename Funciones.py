from os import system
import random

clientes=[]

def pausa():
    input("Pulse enter para continuar.....")

def registrar_pedido():
    while True:
        id=random.randint(000000,999999)
        print(f"Id del pedido: {id}")
        while True:
            name=input("Ingrese el nombre y apellido del cliente: ")
            if " " in name and name.count(" ")==1:
                cliente=name.split(" ")
                if all(nm.isalpha() for nm in cliente):
                    print("Dato valido")
                    pausa()
                    system("cls")
                    break
                else:
                    print("El nombre y apellido deben ser Alphanumericos!!!")
            else:
                print("Dato no valido")
        while True:
            direccion=str(input("Ingrese la dirección del cliente: "))
            if " " in direccion and direccion.count(" ")<=2 or direccion.count(" ")==0:
                if len(direccion) > 2 and direccion != "":
                    print("Dato valido")
                    pausa()
                    system("cls")
                    break
            else:
                print("Dato no valido")
        while True:
            print("""
            Ingrese el sector del cleinte
                  
            1. Concepción
            2. Chiguayante
            3. Talcahuano
            4. Hualpén
            5. San Pedro
            """)
            opcion=input("Ingrese el sector del cliente: ")
            veinte=""
            match opcion:
                case "1":
                    sector="Concepción"
                    print(f"Sector asignado: {sector}")
                    pausa()
                    system("cls")
                    break
                case "2":
                    sector="Chiguayante"
                    print(f"Sector asignado: {sector}")
                    pausa()
                    system("cls")
                    break
                case "3":
                    sector="Talcahuano"
                    print(f"Sector asignado: {sector}")
                    pausa()
                    system("cls")
                    break
                case "4":
                    sector="Hualpén"
                    print(f"Sector asignado: {sector}")
                    pausa()
                    system("cls")
                    break
                case "5":
                    sector="San Pedro"
                    print(f"Sector asignado: {sector}")
                    pausa()
                    system("cls")
                    break
                case other:
                    print("Opcion no valída")
        while True:
            seislts=input("Ingrese la cantidad de dispensadores de 6 lts: ")
            if seislts.isnumeric():
                seislts=int(seislts)
                print("Dato valido")
                pausa()
                system("cls")
            else:
                print("El valor debe se númerico!!")
            diezlts=input("Ingrese la cantidad de dispensadores de 10 lts: ")
            if diezlts.isnumeric():
                diezlts=int(diezlts)
                print("Dato valido")
                pausa()
                system("cls")
                break
            else:
                print("El valor debe se númerico!!")
            veinte=input("Ingrese la cantidad de dispensadores de 20 lts: ")
            if veinte.isnumeric():
                veinte=int(veinte)
                print("Dato valido")
                pausa()
                system("cls")
                break
            else:
                print("El valor debe se númerico!!")

        veintelts=veinte
        clientes.append([id, cliente, direccion, sector, seislts, diezlts, veintelts])

def listar_pedidos():
    if len(clientes) != 0:
        print
        ("""
        ID      Cliente     Dirección       Sector      Disp.6lts       Disp.10lts      Disp.20lts
        """)
        for cliente in cliente:
            print
        (f"""
        {cliente[0]}    {cliente[1][0]:.1f}     {cliente[2]:.1f}    {cliente[3]:.1f}    {cliente[4]:.1f}    {cliente[5]:.1f}    {cliente[6]:.1f}    {cliente[7]:.1f}
                        {cliente[1][1]:.1f}
        """)
        pausa()
        system("cls")


            




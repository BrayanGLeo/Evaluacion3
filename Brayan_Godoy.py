from os import system
import Funciones as f
system("cls")

# Link Github https://github.com/BrayanGLeo/Evaluacion3

while True:
    print("""
    Bienvenido/a a la intranet de CleanWasser
          
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
    """)
    op=input("Ingrese la opción deseada: ")
    match op:
        case "1":
            f.registrar_pedido()
        case "2":
            f.listar_pedidos()
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del programa")
            input("Presione enter para continuar......") 
        case other:
            print("Opción no valída")
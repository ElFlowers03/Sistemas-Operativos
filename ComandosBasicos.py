import subprocess


def ejecutar(comando):
    subprocess.run(comando,shell=True)

opc="1"
while opc!="6":
    print("1. Crear un archivo 'misnotas.txt'")
    print("2. Crear una carpeta 'Calificaciones'")
    print("3. Crear una carpeta dentro de 'Calificaciones' llamada 'Primer Parcial'")
    print("4. Mover archivo 'misnotas.txt' a la carpeta 'Calificaciones'")
    print("5. Mover archivo 'CalculadoraBasica.py' a la carpeta 'Primer Parcial'")
    print("6. Salir")

    opc=str(input("Seleccione una opcion: "))

    if opc=="1":
        ejecutar("touch misnotas.txt")
    elif opc=="2":
        ejecutar("mkdir Calificaciones")
    elif opc=="3":
        ejecutar("mkdir Calificaciones/Primer_Parcial")
    elif opc=="4":
        ejecutar("mv misnotas.txt Calificaciones")
    elif opc=="5":
        ejecutar("mv CalculadoraBasica.py Calificaciones/Primer_Parcial")
    elif opc=="6":
        print("Saliendo del programa")
        break
    else:
        print("Ponga una opcion valida")
    


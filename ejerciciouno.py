""" Escribe un programa en Python que genere un menú con las siguientes opciones:
1. Insertar cola
2. Borrar en cola
3. Listar cola
4. Salir """

cola = []
repetir = "s"

while repetir == "s":
    opcion = 0

    while opcion !=4:
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            elemento = input("Ingrese un elemento para agregar a la cola: ")
            cola.append(elemento)
            print(f"Elemento '{elemento}' agregado a la cola")
        
        elif opcion == 2:
            if len(cola) > 0:
                elemento_borrado = cola.pop(0)
                print(f"Elemento '{elemento_borrado}' borrado de la cola")
            else:
                print("La cola está vacía, no hay elementos para borrar")
        
        elif opcion == 3:
            if len(cola) > 0:
                print("Elementos en la cola:", cola)
            else:
                print("La cola está vacía")
        
        elif opcion == 4:
            print("Saliendo del programa...")
        
        else:
            print("Opción inválida")

    repetir = input(" quieres repetir el programa? (s/n): "
    ).lower()

print("Programa finalizado.")

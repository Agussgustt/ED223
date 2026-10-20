pila = []
repetir = "s"

while repetir == "s":
    opcion = 0

    while opcion !=4:
        print("1. Insertar pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            elemento = input("Ingrese un elemento para agregar a la pila: ")
            pila.append(elemento)
            print(f"Elemento '{elemento}' agregado a la pila")
        
        elif opcion == 2:
            if len(pila) > 0:
                elemento_borrado = pila.pop()
                print(f"Elemento '{elemento_borrado}' borrado de la pila")
            else:
                print("La pila está vacía, no hay elementos para borrar")
        
        elif opcion == 3:
            if len(pila) > 0:
                print("Elementos en la pila:", pila)
            else:
                print("La pila está vacía")
        
        elif opcion == 4:
            print("Saliendo del programa...")
        
        else:
            print("Opción inválida")

    repetir = input(" quieres repetir el programa? (s/n): "
    ).lower()
print("Programa finalizado.")
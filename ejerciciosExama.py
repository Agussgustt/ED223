matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]   
]

#mostrar la fila 2
print("Fila 2:", matriz[1])

#recorrer la matriz y buscar el numero 27
for i in matriz:
    if 27 in i:
        print(f"El numero 27 se encuentra en la fila {matriz.index(i)} y columna {i.index(27)}")

#recorrer todos loa elementos de la matriz y buscar el numero 3
for fila in matriz:
    for elemento in fila:
        if elemento == 3:
            print(f"El numero 3 se encuentra en la fila {matriz.index(fila)} y columna {fila.index(3)}")

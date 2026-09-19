""" #definiendo el array
numeros = [10, 20, 30, 40, 50]

#imprimiendo el valor de la p. 2
print(numeros[2])

#reasignar el valor de la p. 3 a 15
numeros[3] = 15
print(numeros[3])

#agregando un nuevo valor al final del array
numeros.append(60)
print(numeros)

#eliminando por indice
numeros.pop(1)
print(numeros)

#eliminando por valor
numeros.remove(30)
print(numeros) """

""" #arreglo de strings
frutas = ["manzana", "platano", "mango", "pera", "fresa", "uva"]

#eliminando por valor
frutas.remove("mango")
print(frutas)

#eliminando por indice
frutas.pop(2)
print(frutas)

#agregando un nuevo valor al final del array
frutas.append("kiwi")
print(frutas)   

#reemplazando un valor
frutas[1] = "naranja"
print(frutas) """

#declarando un arreglo vacío
arreglo = []

#agregando valores al arreglo
n = int(input("Ingresa el tamaño del arreglo: "))
n1 = int(input("Ingresa el valor a agregar: "))
arreglo.append(n1)
print(arreglo)
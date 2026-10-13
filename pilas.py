# 1. crear una pila vacia
historial = []

#2. apilar / push
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("historial:", historial)

#3. ver elemento superior
pagina_Actual = historial[2]
print("pagina actual:", pagina_Actual)

#4. desapilar/ pop
pagina_salida = historial.pop()
print("saliendo de:", pagina_salida)

print("historial actualizado:", historial)
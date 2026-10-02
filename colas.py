from collections import deque

cola = deque(["ana", "carlos"])

cola.append("Jorge")
cola.append("Andres")
print("cola actual:", cola)

atendido = cola.popleft()
print(f"se antendio a: {atendido}")

print("cola restante:", cola)

atendido = cola.popleft()
print(f"se antendio a: {atendido}")
print("cola restante:", cola)
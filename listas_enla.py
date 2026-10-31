class Nodo:

    def __init__(self, numero):
        #valor que tendra el nodo
        self.numero = numero

    #apunta a nuestro siguiente valor
        self.siguiente = None

class listasEnlazadas:
    def __init__(self):

        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self,numero):

        nuevo_nodo = Nodo(numero)

        if(self.cabeza is None):

            self.cabeza = Nodo(numero)

            return

        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):

        nuevo_nodo = Nodo(numero)

        if(self.cabeza == None):

            self.cabeza = nuevo_nodo

            return

        actual = self.cabeza

        while(actual.siguiente):

            actual = actual.siguiente

        actual.siguiente = nuevo_nodo


        """ eliminar nodo al inicio """
    def Eliminar_Nodo_al_Inicio(self):
        if self.cabeza is None:
            return None

        nodo_borrado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        nodo_borrado.siguiente = None
        return nodo_borrado.numero
    

        """ Eliminar_Nodo_al_Finial """
    def Eliminar_Nodo_al_Final(self):
        if self.cabeza is None:
            return None

        if self.cabeza.siguiente is None:
            nodo_borrado = self.cabeza
            self.cabeza = None
            return nodo_borrado.numero

        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

        nodo_borrado = actual.siguiente
        actual.siguiente = None
        return nodo_borrado.numero

    def Imprimir_ListaEnlazada(self):

        actual = self.cabeza

        while(actual):

            print(actual.numero, " -> ", end=" ")

            actual = actual.siguiente
        print("None")

Mi_lista = listasEnlazadas()
Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Final()
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()
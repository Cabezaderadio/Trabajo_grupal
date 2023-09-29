class Nodo:
    
    def __init__(self, valor):
        self.dato  = valor
        self.siguiente = None
        
        
class Lista:
    
    def  __init__(self, cabecera = None): #Si no le digo el valor de cabecera sera tomado como None, en caso que no exista valor definido será ubicado por defecto como None
        self.primero = cabecera # Da los valores en None
        
    def Imprimir(self):
        print("LKSITA DE NOMBRES")
        nodo_actual = self.primero
        while(nodo_actual):
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
    
    def insertar (self , valor): #valor para nuevo nodo
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo
        
nombres = Lista()


juan = Nodo("Juan")
efmamjjasond = Nodo("efmamjjasond")
Nomin = Nodo("Nomin") #Para indicar la posición en la lista debemos odificar el tipo en la lista dandole a entender cual es el primero en la lista

nombres.primero = Nomin
Nomin.siguiente= efmamjjasond
efmamjjasond.siguiente = juan



nombres.insertar("Pepito")
nombres.Imprimir()0
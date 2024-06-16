#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - Ordenamiento de árbol

# El ordenamiento de árbol es un algoritmo de ordenamiento que se basa en la estructura de datos de árbol binario. es decir, se utiliza un árbol binario de búsqueda para almacenar los elementos a ordenar.

class Node:     # Clase para crear nodos
    def __init__(self, key):    # Constructor
        self.left = None    # Inicializar hijo izquierdo
        self.right = None       # Inicializar hijo derecho
        self.val = key    # Inicializar valor

def insert(root, key):  # Función para insertar un nuevo nodo con un valor dado
    if root is None:        # Si el árbol está vacío, se crea un nuevo nodo
        return Node(key)        # Se regresa el nodo creado
    else:       
        if root.val < key:      # Si el valor es mayor que la raíz, se inserta a la derecha
            root.right = insert(root.right, key)    # Se inserta el nodo a la derecha
        else:
            root.left = insert(root.left, key)  # Si el valor es menor que la raíz, se inserta a la izquierda
    return root     # Se regresa la raíz

def inorder_traversal(root):        # Función para recorrer el árbol en orden
    if root:                        # Si la raíz no es nula
        inorder_traversal(root.left)        # Se recorre el subárbol izquierdo
        print(root.val, end=" ")        # Se imprime el valor de la raíz
        inorder_traversal(root.right)    # Se recorre el subárbol derecho

# Ordenamiento de fechas de lanzamiento de videojuegos
# Crear el árbol
root = None     # Árbol vacío
fechas_lanzamiento = [19971115, 20011114, 20070313, 20130917, 20201110]  # Formato AAAAMMDD

# Insertar fechas en el árbol
for fecha in fechas_lanzamiento:    # Recorrer la lista de fechas
    root = insert(root, fecha)      # Insertar la fecha en el árbol

# Mostrar fechas ordenadas
print("Fechas de lanzamiento de videojuegos ordenadas:")    # se imprime el mensaje
inorder_traversal(root)             # Recorrer el árbol en orden
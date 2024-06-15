#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - Inserción (InsertionSort).
#La inserción es un algoritmo de ordenamiento que construye una matriz ordenada uno a la vez. Es menos eficiente en grandes listas que algoritmos más avanzados como quicksort, heapsort o merge sort.


def insertion_sort_videojuegos(lista_videojuegos):  # Función que ordena una lista de videojuegos alfabéticamente
    # Recorremos cada videojuego de la lista
    for i in range(1, len(lista_videojuegos)):  # se usa len() para obtener la longitud de la lista
        juego_actual = lista_videojuegos[i]     # Seleccionamos el videojuego actual
        j = i-1                                 # Inicializamos el índice del videojuego anterior al actual
        # Mover los nombres de los videojuegos que son alfabética  mente mayores que el juego actual a una posición adelante de su posición actual
        while j >=0 and juego_actual < lista_videojuegos[j]:        # Comparamos el videojuego actual con el videojuego anterior
                lista_videojuegos[j+1] = lista_videojuegos[j]       # Si el videojuego actual es menor que el videojuego anterior, movemos el videojuego anterior a una posición adelante
                j -= 1                                              # Disminuimos el índice para comparar con el siguiente videojuego
        lista_videojuegos[j+1] = juego_actual                       # Insertamos el videojuego actual en su posición correcta

lista_videojuegos = ["Zelda", "Mario Bros", "Sonic", "Final Fantasy", "Minecraft"]  # Lista de videojuegos desordenada
insertion_sort_videojuegos(lista_videojuegos)   # Llamamos a la función insertion_sort_videojuegos() para ordenar la lista de videojuegos
print("Lista de videojuegos ordenada:", lista_videojuegos)  # Imprimimos la lista de videojuegos ordenada
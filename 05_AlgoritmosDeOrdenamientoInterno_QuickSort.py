#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - QuickSort.

# QuickSort es un algoritmo de ordenamiento muy eficiente que utiliza la técnica de divide y vencerás para ordenar elementos.

def quick_sort(arr):  # Función que implementa el algoritmo de ordenamiento QuickSort

    if len(arr) <= 1:   # Si la lista tiene un solo elemento o está vacía, se regresa la lista
        return arr      # Se regresa la lista
    else:
        pivot = arr[len(arr) // 2]              # Seleccionamos el pivote como el elemento en la mitad de la lista
        left = [x for x in arr if x < pivot]    # Seleccionamos los elementos menores que el pivote
        middle = [x for x in arr if x == pivot] # Seleccionamos los elementos iguales al pivote
        right = [x for x in arr if x > pivot]   # Seleccionamos los elementos mayores que el pivote
        return quick_sort(left) + middle + quick_sort(right)    # Se regresa la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":      # Función principal
    puntuaciones = [23, 45, 12, 89, 37, 56, 99, 48] # Lista de puntuaciones
    print("Puntuaciones originales:", puntuaciones) # Mostramos las puntuaciones originales
    puntuaciones_ordenadas = quick_sort(puntuaciones)   # Ordenamos las puntuaciones
    print("Puntuaciones ordenadas:", puntuaciones_ordenadas)    # Mostramos las puntuaciones ordenadas

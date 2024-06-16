#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - MergeSort.

#MergeSort es un algoritmo que sigue la técnica de dividir y conquistar. Divide la lista en dos mitades, ordena las dos mitades y luego las fusiona.

def merge_sort(arr):    # Función que implementa el algoritmo de ordenamiento MergeSort

    if len(arr) <= 1:   # Si la lista tiene un solo elemento o está vacía, se regresa la lista
        return arr    # Se regresa la lista

    mid = len(arr) // 2             # Se obtiene el índice medio de la lista
    left = merge_sort(arr[:mid])    # Se ordena la primera mitad de la lista
    right = merge_sort(arr[mid:])   # Se ordena la segunda mitad de la lista

    return merge(left, right)    # Se fusionan las dos mitades ordenadas

def merge(left, right):     # Función para fusionar dos listas ordenadas
    result = []    # Lista para almacenar el resultado
    i = j = 0       # Índices para recorrer las dos listas

    while i < len(left) and j < len(right):   # Mientras no se haya llegado al final de alguna de las dos listas
        if left[i] < right[j]:      # Si el elemento de la primera lista es menor
            result.append(left[i])  # Se agrega el elemento a la lista resultante
            i += 1              # Se incrementa el índice de la primera lista
        else:
            result.append(right[j])     # Si el elemento de la segunda lista es menor, se agrega a la lista resultante
            j += 1                      # Se incrementa el índice de la segunda lista

    result.extend(left[i:])     # Se agregan los elementos restantes de la primera lista. extend() agrega los elementos de una lista a otra
    result.extend(right[j:])    # Se agregan los elementos restantes de la segunda lista

    return result           # Se regresa la lista resultante

if __name__ == "__main__":
    # Lista de ingresos mensuales
    ingresos = [2500, 4200, 3100, 5000, 2800, 4700]
    print("Ingresos originales:", ingresos)  # Mostramos los ingresos originales
    ingresos_ordenados = merge_sort(ingresos)   # Ordenamos los ingresos
    print("Ingresos ordenados:", ingresos_ordenados)    # Mostramos los ingresos ordenados

#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - RadixSort.

# RadixSort es un algoritmo de ordenamiento que se basa en el ordenamiento por conteo. este algoritmo ordena los elementos de una lista basándose en los dígitos de los números que la componen. Para ello, se ordenan los números de acuerdo a cada dígito, comenzando por el dígito menos significativo y avanzando hacia el más significativo. En cada iteración, se utiliza el ordenamiento por conteo para ordenar los números en función del dígito correspondiente.


def counting_sort(arr, exp):        # Función que implementa el algoritmo de ordenamiento por conteo
    n = len(arr)                # Obtenemos la cantidad de elementos en la lista
    output = [0] * n            # Creamos una lista de salida con la misma cantidad de elementos que la lista original
    count = [0] * 10            # Creamos una lista de conteo con 10 elementos (0-9)

    for i in range(n):          # Recorremos la lista para contar la cantidad de elementos con el mismo dígito
        index = arr[i] // exp   # Obtenemos el dígito correspondiente al número actual
        count[index % 10] += 1  # Incrementamos el contador del dígito

    for i in range(1, 10):      # Recorremos la lista de conteo para obtener la posición de cada dígito
        count[i] += count[i - 1]    # Sumamos el contador actual con el anterior

    i = n - 1           # Inicializamos el índice en la última posición de la lista
    while i >= 0:       # Recorremos la lista en orden inverso para ordenar los elementos
        index = arr[i] // exp   # Obtenemos el dígito correspondiente al número actual
        output[count[index % 10] - 1] = arr[i]  # Insertamos el número en la posición correspondiente
        count[index % 10] -= 1      # Decrementamos el contador del dígito
        i -= 1        # Decrementamos el índice

    for i in range(n):      # Copiamos los elementos ordenados a la lista original
        arr[i] = output[i]  # Copiamos el elemento en la posición correspondiente

def radix_sort(arr):    # Función que implementa el algoritmo de ordenamiento RadixSort

    max1 = max(arr)          # Obtenemos el número máximo de la lista
    exp = 1                 # Inicializamos el exponente en 1
    while max1 // exp > 0:  # Mientras haya dígitos en el número máximo
        counting_sort(arr, exp) # Ordenamos la lista por el dígito correspondiente
        exp *= 10           # Incrementamos el exponente

    return arr  # Regresamos la lista ordenada

if __name__ == "__main__":  # Función principal
    # Lista de números de teléfono
    telefonos = [5551234, 5554321, 5556789, 5559876, 5552468]
    print("Números de teléfono originales:", telefonos)     # Mostramos los números de teléfono originales
    telefonos_ordenados = radix_sort(telefonos)             # Ordenamos los números de teléfono
    print("Números de teléfono ordenados:", telefonos_ordenados)    # Mostramos los números de teléfono ordenados

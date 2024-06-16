#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - Selección (SelectionSort).

# el algoritmo de ordenamiento por selección es un algoritmo de ordenamiento que consiste en dividir la lista de elementos en dos partes: una parte ordenada y una parte no ordenada. 
# El algoritmo busca el menor elemento en la parte no ordenada y lo intercambia con el primer elemento de la parte no ordenada. Luego, el algoritmo busca el segundo menor elemento en la parte no ordenada y lo intercambia con el segundo elemento de la parte no ordenada, y así sucesivamente hasta que la lista esté completamente ordenada.

def selection_sort(arr):    # Función que implementa el algoritmo de ordenamiento por selección
    n = len(arr)    # Obtenemos la cantidad de elementos en la lista
    
    # Recorremos la lista desde el primer elemento hasta el penúltimo
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        
        # Recorremos el resto de la lista para encontrar el menor precio
        for j in range(i+1, n): 
            if arr[j] < arr[min_idx]:   # Si encontramos un precio menor
                min_idx = j            # Actualizamos el índice del menor precio
        
        # Intercambiamos el menor precio encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]     #
    
    return arr

if __name__ == "__main__":  # Función principal
    # Lista de precios de artículos de papelería
    precios = [1.50, 3.20, 0.99, 2.49, 4.50, 2.99]      # Precios originales
    print("Precios originales:", precios)   # Mostramos los precios originales
    precios_ordenados = selection_sort(precios)   # Ordenamos los precios
    print("Precios ordenados:", precios_ordenados)  # Mostramos los precios ordenados

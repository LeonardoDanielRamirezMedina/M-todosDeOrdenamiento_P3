#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento externos - Balanced multiway merging.


import heapq    #importamos la librería heapq para trabajar con colas de prioridad

def balanced_multiway_merging(data, k): #esta función recibe una lista de datos y un número k de particiones

    def merge_k_way(lists): #esta función recibe una lista de listas 
      
        min_heap = []               #creamos un heap vacío. heapq es una cola de prioridad que se implementa como un heap binario
        for i, lst in enumerate(lists):     #recorremos la lista de listas
            if lst:                        #si la lista no está vacía
                heapq.heappush(min_heap, (lst[0], i, 0))    #agregamos el primer elemento de la lista al heap
        
        result = []     #creamos una lista vacía para guardar el resultado
        while min_heap:     #mientras el heap no esté vacío
            val, list_idx, element_idx = heapq.heappop(min_heap)    #sacamos el elemento con menor valor del heap
            result.append(val)                        #agregamos el elemento a la lista de resultados
            if element_idx + 1 < len(lists[list_idx]):      #si no hemos llegado al final de la lista
                next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)  #creamos una tupla con el siguiente elemento de la lista
                heapq.heappush(min_heap, next_tuple)            #agregamos la tupla al heap
        
        return result

    chunk_size = len(data) // k + 1     #calculamos el tamaño de los chunks
    chunks = [sorted(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size)]      #dividimos la lista en chunks y los ordenamos

    return merge_k_way(chunks)          #devolvemos el resultado de la función merge_k_way con los chunks ordenados


if __name__ == "__main__":
    # Lista de productos vendidos en diferentes sucursales
    productos = [5, 3, 8, 4, 6, 2, 7, 1, 9]
    k = 3  # Número de sucursales
    print("Productos originales:", productos)   #imprimimos la lista original
    productos_ordenados = balanced_multiway_merging(productos, k)   #llamamos a la función balanced_multiway_merging
    print("Productos ordenados:", productos_ordenados)  #imprimimos la lista ordenada

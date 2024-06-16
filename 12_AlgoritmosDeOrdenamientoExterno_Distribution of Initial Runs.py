#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento externos - Polyphase sort.

# este algoritmo de ordenamiento externo se basa en la distribución de los datos en sublistas de tamaño fijo, ordenarlas y mezclarlas hasta obtener la lista ordenada completa.

from heapq import merge   #Importar la función merge de la librería heapq 
def distribution_of_initial_runs(data):     #Función que implementa el algoritmo de ordenamiento externo Polyphase sort

    # Dividir los datos en sublistas de tamaño fijo y ordenarlas
    run_size = 4    # Tamaño de las sublistas
    runs = [sorted(data[i:i + run_size]) for i in range(0, len(data), run_size)]    #Dividir los datos en sublistas de tamaño fijo y ordenarlas
    
    # Mezclar las sublistas ordenadas

    while len(runs) > 1:        #Mientras haya más de una sublista
        new_runs = []    #Crear una lista vacía
        for i in range(0, len(runs), 2):    #Para cada par de sublistas
            if i + 1 < len(runs):           #Si hay dos sublistas
                new_runs.append(list(merge(runs[i], runs[i + 1])))  #Mezclar las sublistas y agregar el resultado a la lista de sublistas
            else:   
                new_runs.append(runs[i])    #Si solo hay una sublista, agregarla a la lista de sublistas
        runs = new_runs   #Actualizar la lista de sublistas
    
    return runs[0]      #Retornar la lista de sublistas ordenadas

if __name__ == "__main__":  #Función principal
    # Lista de cantidades de productos en inventario
    inventario = [20, 5, 15, 10, 25, 30, 5, 10]   #Lista de cantidades de productos en inventario
    print("Inventario original:", inventario)       #Imprimir la lista de cantidades de productos en inventario
    inventario_ordenado = distribution_of_initial_runs(inventario)  #Ordenar la lista de cantidades de productos en inventario
    print("Inventario ordenado:", inventario_ordenado)  #Imprimir la lista de cantidades de productos en inventario ordenada

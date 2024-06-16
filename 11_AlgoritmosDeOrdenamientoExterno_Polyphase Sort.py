#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento externos - Polyphase sort.

#Polyphase sort es un algoritmo de ordenamiento externo que se basa en la mezcla de archivos ordenados. En este algoritmo, se dividen los archivos en dos partes: archivos de entrada y archivos de salida.

def polyphase_sort(data):

    # usaremos una implementación básica basada en la idea de Polyphase Sort
    from heapq import merge # importa la función merge de la biblioteca heapq para combinar dos listas ordenadas

    def split_into_runs(data):  # divide la lista en subsecuencias ordenadas
        runs = []             # cada subsecuencia es un "run". un run es una lista ordenada
        new_run = [data[0]]  # comienza un nuevo run
        for i in range(1, len(data)):       # recorre la lista
            if data[i] >= data[i - 1]:  # si el elemento actual es mayor o igual al anterior
                new_run.append(data[i]) # agrega el elemento al run actual
            else:
                runs.append(new_run)    # si no, el run actual está completo
                new_run = [data[i]]    # comienza un nuevo run
        runs.append(new_run)      # agrega el último run
        return runs         # devuelve la lista de runs

    runs = split_into_runs(data)        # divide la lista en runs
    while len(runs) > 1:                # mientras haya más de un run
        new_runs = []                   # crea una nueva lista de runs
        for i in range(0, len(runs), 2):        # combina los runs en pares
            if i + 1 < len(runs):       # si hay un run adicional   
                new_runs.append(list(merge(runs[i], runs[i + 1])))  # combina los runs
            else:
                new_runs.append(runs[i])    # si no, agrega el run sin combinar
        runs = new_runs             # actualiza la lista de runs

    return runs[0]      # devuelve la lista ordenada


if __name__ == "__main__":  # ejemplo de uso

    horas_trabajadas = [7, 5, 8, 6, 7, 9, 4, 6, 8]  # lista de horas trabajadas
    print("Horas trabajadas originales:", horas_trabajadas) # imprime la lista original
    horas_ordenadas = polyphase_sort(horas_trabajadas)  # ordena la lista
    print("Horas trabajadas ordenadas:", horas_ordenadas)   # imprime la lista ordenada

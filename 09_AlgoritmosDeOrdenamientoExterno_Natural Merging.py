#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento externos - Natural Merging 

# El ordenamiento natural es un algoritmo de ordenamiento externo que consiste en dividir la lista en secuencias ordenadas y combinarlas en una sola lista ordenada.

def merge(left, right):     #Esta funcion mezcla dos listas ordenadas. merge() combina dos listas ordenadas en una sola lista ordenada.
    result = []             #Se crea una lista vacía.
    i = j = 0               #Se inicializan los índices de las listas en 0.

    while i < len(left) and j < len(right):     #Mientras los índices no lleguen al final de las listas.
        if left[i] <= right[j]:                 #Si el elemento de la lista izquierda es menor o igual al de la derecha.
            result.append(left[i])              #Se agrega el elemento de la lista izquierda a la lista resultante.
            i += 1                              #Se incrementa el índice de la lista izquierda.
        else:
            result.append(right[j])             #Se agrega el elemento de la lista derecha a la lista resultante.
            j += 1                              #Se incrementa el índice de la lista derecha.

    result.extend(left[i:])                     #Se agregan los elementos restantes de la lista izquierda.
    result.extend(right[j:])                    #Se agregan los elementos restantes de la lista derecha.

    return result

def natural_merging(data):  #Esta funcion ordena una lista de datos usando el algoritmo de ordenamiento Natural Merging.

    def find_runs(data):                #Esta funcion encuentra las secuencias ordenadas en la lista de datos.
        runs = []                       #Se crea una lista vacía para almacenar las secuencias ordenadas.
        new_run = [data[0]]             #Se crea una nueva secuencia con el primer elemento de la lista.
        for i in range(1, len(data)):   #Se recorre la lista de datos.
            if data[i] >= data[i - 1]:  #Si el elemento actual es mayor o igual al anterior.
                new_run.append(data[i]) #Si el elemento actual es mayor o igual al anterior, se agrega a la secuencia actual.
            else:
                runs.append(new_run)    #Si el elemento actual es menor al anterior, se agrega la secuencia actual a la lista de secuencias.
                new_run = [data[i]]     #Se crea una nueva secuencia con el elemento actual.
        runs.append(new_run)            #Se agrega la última secuencia a la lista de secuencias.
        return runs                     #Se regresa la lista de secuencias. 

    runs = find_runs(data)          #Se encuentran las secuencias ordenadas en la lista de datos.
    while len(runs) > 1:            #Mientras haya más de una secuencia en la lista.
        new_runs = []                   #Se crea una lista vacía para almacenar las nuevas secuencias.
        for i in range(0, len(runs), 2):    #Se recorren las secuencias de dos en dos.
            if i + 1 < len(runs):           #Si hay dos secuencias para combinar.
                new_runs.append(merge(runs[i], runs[i + 1]))    #Se combinan las dos secuencias y se agrega la secuencia resultante a la lista de nuevas secuencias.
            else:   
                new_runs.append(runs[i])    #Si solo hay una secuencia, se agrega tal cual a la lista de nuevas secuencias.
        runs = new_runs         #Se actualiza la lista de secuencias con las nuevas secuencias.

    return runs[0]            #Se regresa la lista ordenada.


if __name__ == "__main__":  #Función principal
    # Lista de temperaturas registradas durante un mes
    temperaturas = [15, 16, 17, 14, 13, 14, 18, 19, 17, 16, 20, 21]
    print("Temperaturas originales:", temperaturas) #Mostramos las temperaturas originales
    temperaturas_ordenadas = natural_merging(temperaturas)  #Ordenamos las temperaturas
    print("Temperaturas ordenadas:", temperaturas_ordenadas)    #Mostramos las temperaturas ordenadas

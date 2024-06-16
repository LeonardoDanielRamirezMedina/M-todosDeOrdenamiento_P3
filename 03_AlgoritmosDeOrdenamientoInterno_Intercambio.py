#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento internos - Intercambio.

#Este algoritmo funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. El pase completo a través de la lista se repite hasta que no se requieren intercambios, lo que indica que la lista está ordenada.


def bubble_sort(arr):   #Definimos la función bubble_sort que recibe un arreglo como parámetro
    n = len(arr)    #Obtenemos la longitud del arreglo
    
    # Recorremos la lista varias veces
    for i in range(n):
        # Flag para detectar si hubo algún intercambio
        swapped = False #Inicializamos la variable swapped en False. swapped es una variable que nos ayudará a saber si hubo algún intercambio en la lista.
        
        # Recorremos la lista desde el inicio hasta n-i-1
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if arr[j] > arr[j+1]:                   #Si el elemento actual es mayor que el siguiente, intercambiamos los elementos.
                arr[j], arr[j+1] = arr[j+1], arr[j] #Intercambiamos los elementos.
                swapped = True                      #Cambiamos el valor de la variable swapped a True.
        
        # Si no hubo ningún intercambio en la pasada, la lista está ordenada
        if not swapped: 
            break
    
    return arr

if __name__ == "__main__":  #Función principal
    # Lista de artículos de papelería con sus precios
    precios = [1.50, 3.20, 0.99, 2.49, 4.50, 2.99]  #Definimos una lista de precios de artículos de papelería.
    print("Precios originales:", precios)       #Imprimimos la lista de precios original.
    precios_ordenados = bubble_sort(precios)        #Llamamos a la función bubble_sort y le pasamos la lista de precios como argumento.
    print("Precios ordenados:", precios_ordenados)  #Imprimimos la lista de precios ordenada.

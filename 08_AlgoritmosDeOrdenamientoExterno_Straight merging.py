#       MÉTODOS DE ORDAMIENTO    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Algoritmos de ordenamiento externos - Straight merging.

# Straight Merging es un algoritmo de ordenamiento externo que consiste en dividir la lista en dos partes y ordenarlas recursivamente.

def straight_merging(data): # Función que ordena una lista de datos usando el algoritmo de ordenamiento Straight Merging.

    if len(data) <= 1:      # Si la longitud de la lista es menor o igual a 1, se regresa la lista tal cual.
        return data         # Regresa la lista tal cual.

    mid = len(data) // 2        # Se obtiene el índice medio de la lista.
    left = straight_merging(data[:mid])     # Se divide la lista en dos partes y se ordenan recursivamente.
    right = straight_merging(data[mid:])        # Se divide la lista en dos partes y se ordenan recursivamente.

    return merge(left, right)       # Se regresa la lista ordenada.

def merge(left, right):     # Función que mezcla dos listas ordenadas.
    result = []             # Se crea una lista vacía.
    i = j = 0               # Se inicializan los índices de las listas en 0.

    while i < len(left) and j < len(right):     # Mientras los índices no lleguen al final de las listas.
        if left[i] < right[j]:                  # Si el elemento de la lista izquierda es menor al de la derecha.
            result.append(left[i])              # Se agrega el elemento de la lista izquierda a la lista resultante.
            i += 1                              # Se incrementa el índice de la lista izquierda.
        else:
            result.append(right[j])             # Se agrega el elemento de la lista derecha a la lista resultante.
            j += 1                              # Se incrementa el índice de la lista derecha.

    result.extend(left[i:])             # Se agregan los elementos restantes de la lista izquierda.
    result.extend(right[j:])            # Se agregan los elementos restantes de la lista derecha.
    
    return result                # Se regresa la lista resultante.

if __name__ == "__main__":
    # Lista de ventas diarias en una tienda
    ventas_diarias = [500, 300, 800, 400, 600, 200, 700]        # Lista de ventas diarias en una tienda.
    print("Ventas diarias originales:", ventas_diarias)     # Se imprime la lista original.
    ventas_ordenadas = straight_merging(ventas_diarias)     # Se ordena la lista de ventas diarias.
    print("Ventas diarias ordenadas:", ventas_ordenadas)        # Se imprime la lista ordenada.

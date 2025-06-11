# Lista de números para probar los algoritmos
numeros = [64, 34, 25, 12, 22, 11, 90]

def ordenamiento_burbuja(lista: list):
    """
    Algoritmo de ordenamiento burbuja que ordena la lista original.
    Compara elementos adyacentes y los intercambia si están en orden incorrecto.
    El elemento más grande "burbujea" hacia el final en cada pasada.
    """
    largo_lista = len(lista)
    
    # Recorremos toda la lista varias veces
    for indice_a in range(largo_lista):
        # En cada pasada, comparamos pares adyacentes
        # Después de cada pasada completa, el mayor queda al final (como una burbuja)
        for indice_b in range(0, largo_lista - indice_a - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[indice_b] > lista[indice_b + 1]:
                lista[indice_b], lista[indice_b + 1] = lista[indice_b + 1], lista[indice_b]

def quick_sort(lista):
    """
    Algoritmo Quick Sort que usa divide y vencerás.
    Elige un pivote, divide la lista en menores, iguales y mayores,
    ordena recursivamente y combina los resultados.
    No modifica la lista original, devuelve una nueva lista ordenada.
    """
    # Caso base: lista vacía o de un solo elemento ya está ordenada
    if len(lista) <= 1:
        return lista.copy()  # devolvemos copia para no alterar la original
    
    # Elegimos el pivote como el primer elemento
    pivot = lista[0]
    
    # Creamos las tres sublistas para clasificar los elementos
    menores = []
    iguales = []
    mayores = []
    
    # Clasificamos cada elemento según su relación con el pivote
    for elemento in lista:
        if elemento < pivot:
            menores.append(elemento)
        elif elemento == pivot:
            iguales.append(elemento)
        else:
            mayores.append(elemento)
    
    # Ordenamos recursivamente las sublistas de menores y mayores
    lista_menores = quick_sort(menores)
    lista_mayores = quick_sort(mayores)
    
    # Concatenamos: menores ordenados + iguales + mayores ordenados
    resultado = []
    for x in lista_menores:
        resultado.append(x)
    for x in iguales:
        resultado.append(x)
    for x in lista_mayores:
        resultado.append(x)
    
    return resultado

def probar_bubble_sort():
    """
    Ejecuta y muestra el resultado del algoritmo Bubble Sort.
    """
    print(f"\n📊 BUBBLE SORT")
    print(f"Lista original: {numeros}")
    
    # Creamos una copia para no modificar la lista original
    lista_copia = numeros.copy()
    ordenamiento_burbuja(lista_copia)
    
    print(f"Lista ordenada: {lista_copia}")
    print("ℹ️  Nota: Bubble Sort modifica la lista original")

def probar_quick_sort():
    """
    Ejecuta y muestra el resultado del algoritmo Quick Sort.
    """
    print(f"\n QUICK SORT")
    print(f"Lista original: {numeros}")
    
    lista_ordenada = quick_sort(numeros)
    
    print(f"Lista ordenada: {lista_ordenada}")
    print("ℹ️  Nota: Quick Sort devuelve una nueva lista sin modificar la original")

# ALGORITMOS DE BUSQUEDA #

def busqueda_lineal(lista_numerica: list, dato_a_buscar: int):
    """
    Búsqueda lineal que recorre toda la lista elemento por elemento.
    Busca de forma secuencial hasta encontrar el elemento o llegar al final.
    Funciona con listas ordenadas y desordenadas.
    """
    # Recorremos cada posición de la lista
    for i in range(len(lista_numerica)):
        if dato_a_buscar == lista_numerica[i]:
            return i  # Retornamos la posición donde se encontró
    return -1  # Retornamos -1 si no se encontró

def busqueda_binaria(lista_numerica: list, dato_a_buscar: int):
    """
    Búsqueda binaria que divide la lista por la mitad en cada iteración.
    Solo funciona con listas ordenadas. Es más eficiente que la búsqueda lineal.
    Usa divide y vencerás: compara con el elemento del medio y descarta la mitad.
    """
    # Caso base: lista vacía
    if len(lista_numerica) == 0:
        return -1
    
    # Encontramos el elemento del medio
    mitad_lista = len(lista_numerica) // 2
    
    # Si encontramos el elemento, retornamos su posición
    if dato_a_buscar == lista_numerica[mitad_lista]:
        return mitad_lista
    # Si el dato es mayor, buscamos en la segunda mitad
    elif dato_a_buscar > lista_numerica[mitad_lista]:
        segunda_parte_lista = lista_numerica[mitad_lista + 1:]
        resultado = busqueda_binaria(segunda_parte_lista, dato_a_buscar)
        # Si se encontró, ajustamos la posición real
        return resultado + mitad_lista + 1 if resultado != -1 else -1
    # Si el dato es menor, buscamos en la primera mitad
    elif dato_a_buscar < lista_numerica[mitad_lista]:
        primera_parte_lista = lista_numerica[:mitad_lista]
        return busqueda_binaria(primera_parte_lista, dato_a_buscar)
    
    return -1

def probar_busqueda_lineal():
    """
    Ejecuta y muestra el resultado de la búsqueda lineal.
    """
    print(f"\n BÚSQUEDA LINEAL")
    print(f"Lista: {numeros}")
    

    numero_buscar = int(input("Ingresa el número a buscar: "))
    posicion = busqueda_lineal(numeros, numero_buscar)
    
    if posicion != -1:
        print(f" Número {numero_buscar} encontrado en la posición {posicion}")
    else:
        print(f" Número {numero_buscar} no se encontró en la lista")
    
    print("ℹ  Nota: La búsqueda lineal funciona con listas ordenadas y desordenadas")

def probar_busqueda_binaria():
    """
    Ejecuta y muestra el resultado de la búsqueda binaria.
    """
    print(f"\n BÚSQUEDA BINARIA")
    lista_ordenada = sorted(numeros)
    print(f"Lista ordenada: {lista_ordenada}")

    numero_buscar = int(input("Ingresa el número a buscar: "))
    posicion = busqueda_binaria(lista_ordenada, numero_buscar)
    
    if posicion != -1:
        print(f" Número {numero_buscar} encontrado en la posición {posicion}")
    else:
        print(f" Número {numero_buscar} no se encontró en la lista")
    
    print("  Nota: La búsqueda binaria requiere que la lista esté ordenada")

def mostrar_menu():
    """
    Muestra las opciones disponibles para el usuario.
    """
    print("\n" + "="*50)
    print("🔢 ALGORITMOS DE ORDENAMIENTO Y BÚSQUEDA")
    print("="*50)
    print("ORDENAMIENTO:")
    print("1. Bubble Sort (Ordenamiento Burbuja)")
    print("2. Quick Sort")
    print("3. Búsqueda Lineal")
    print("4. Búsqueda Binaria")
    print("\n5. Salir")
    print("-"*50)

def main():
    """
    Función principal que maneja el menú interactivo.
    Permite al usuario elegir qué algoritmo probar.
    """
    print("¡Bienvenido al programa de algoritmos de ordenamiento y búsqueda!")
    
    while True:
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            probar_bubble_sort()
        elif opcion == "2":
            probar_quick_sort()
        elif opcion == "3":
            probar_busqueda_lineal()
        elif opcion == "4":
            probar_busqueda_binaria()
        elif opcion == "5":
            print("\n ¡Gracias por usar el programa!")
            break
        else:
            print(" Opción no válida. Por favor, elige entre 1 y 5.")

        input("\nPresiona Enter para continuar...")

# Ejecutar el programa
main()
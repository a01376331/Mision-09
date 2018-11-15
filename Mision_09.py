# Rubén Villalpando Bremont
# Misión 09

def extraerPares(lista): # Función que recibe una lista de números y regresa otra lista con los pares de la primera
    listaNueva = []
    for x in lista:
        if x % 2 == 0:
            listaNueva.append(x)
    return listaNueva


def extraerMayoresPrevio(lista): # Función que recibe una lista y regresa una nueva que contiene los números que son mayores al previo.
    listaMayores = []
    for x in range(1, len(lista)):
        if lista[x] > lista[x-1]:
            listaMayores.append(lista[x])
    return listaMayores


def intercambiarParejas(lista): # Función que intercambia los lugares de parejas de números que están juntos.
    parejasPorCambiar = len(lista)//2
    listaParejasInvertidas = lista[:]
    for x in range(1, parejasPorCambiar*2, 2):
        listaParejasInvertidas[x] = lista[x-1]
        listaParejasInvertidas[x-1] = lista[x]
    return listaParejasInvertidas


def intercambiarMM(lista): # Función que intercambia de lugar el mayor número con el menor
    if lista:
        a = lista.index(max(lista))
        b = lista.index(min(lista))
        c = lista[a]
        d = lista[b]
        print(a, b)
        lista[a] = d
        lista[b] = c
    return lista


def promediarCentro(lista): # Función que calcula el promedio de una lista de números sin tomar en cuenta el mayor y el menor
    if len(lista) >= 3:
        lista.remove(max(lista))
        lista.remove(min(lista))
        return sum(lista)/len(lista)
    return 0


def calcularEstadistica(lista): # Función que calcula la media y la desviación estándar de una lista de datos.
    if len(lista) > 1:
        media = sum(lista)/len(lista)
        sumatoria = 0
        for x in range(len(lista)):
            sumatoria += (lista[x] - media)**2
        desviacionEstandar = (sumatoria/(len(lista)-1)) ** 0.5
        return media, desviacionEstandar
    return 0, 0


def calcularSuma(lista): # Función que regresa la suma de todos los números que no son o están alado de un 13.
    x = [i for i, j in enumerate(lista) if j == 13]
    suma = 0
    indicesPorSaltar = []
    for k in x:
        indicesPorSaltar.append(k - 1)
        indicesPorSaltar.append(k)
        indicesPorSaltar.append(k + 1)
    for n in range(len(lista)):
        if n in indicesPorSaltar:
            continue
        suma += lista[n]
    return suma


def main(): # Función principal que hace pruebas de las funciones.
    a = [1, 2, 4, 6, 3, 435, 65, 23, 7, 4, 8, 234, 5433, 1, 4, 5, 3]
    b = [1, 3, 5, 7, 9, 6573647361]
    c = []
    d = [2, 1, 4, 5, 7, 3, 8]
    d2 = d[:]
    e = [1, 2, 3, 4, 5, 6]
    f = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    g = [13,49]
    h = [5, 2, 13, 4, 1, 6, 1, 8, 4, 13, 5]
    print("Problema 1. Regresa una lista nueva con los valores pares de la lista original")
    print("La lista", a, "Regresa la lista", extraerPares(a))
    print("La lista", b, "Regresa la lista", extraerPares(b))
    print("La lista", c, "Regresa la lista", extraerPares(c))
    print("")
    print("Problema 2. Regresa un alista nueva con los valores que sean mayores que el previo")
    print("La lista", a, "Regresa la lista", extraerMayoresPrevio(a))
    print("La lista", b, "Regresa la lista", extraerMayoresPrevio(b))
    print("La lista", c, "Regresa la lista", extraerMayoresPrevio(c))
    print("")
    print("Problema 3. Regresa una lista nueva con las parejas de datos invertidas.")
    print("La lista", a, "Regresa la lista", intercambiarParejas(a))
    print("La lista", b, "Regresa la lista", intercambiarParejas(b))
    print("La lista", c, "Regresa la lista", intercambiarParejas(c))
    print("")
    print("Problema 4. Modifica una lista intercambiando de lugar el valor menor con el mayor")
    print("la lista", d, "Modificada es", intercambiarMM(d2))
    print("la lista", c, "Modificada es", intercambiarMM(c))
    print("la lista", d, "Modificada es", intercambiarMM(d2))
    print("")
    print("Problema 5. Regresa el promedio centro de una lista de números")
    print("La lista", a, "tiene un promedio centro de", promediarCentro(a))
    print("La lista", b, "tiene un promedio centro de", promediarCentro(b))
    print("La lista", c, "tiene un promedio centro de", promediarCentro(c))
    print("")
    print("Problema 6. Regresa la media y la desviación estándar de una lista de números")
    print("La lista", e, "Tiene un promedio y media de", calcularEstadistica(e))
    print("La lista", f, "Tiene un promedio y media de", calcularEstadistica(f))
    print("La lista", c, "Tiene un promedio y media de", calcularEstadistica(c))
    print("")
    print("Problema 7. Regresa la suma de todos los numeros excepto los que estan a lado de un 13")
    print("La lista", g, "Regresa la suma", calcularSuma(g))
    print("La lista", h, "Regresa la suma", calcularSuma(h))



main()

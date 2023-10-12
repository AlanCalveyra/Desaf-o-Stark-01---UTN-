#ALUMNO: ALAN JOEL CALVEYRA
#DIVISIÓN: E

# Desafío 01:

# Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
"""
# A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
"""
def imprimir_nombre_heroe_genero_m(lista_personajes: list[dict]) -> str:
    
    

    for heroe in lista_personajes:
        heroe_genero_m = heroe.get("genero", "No tiene genero")
        # nombre_heroe_m = heroe.get("nombre")
        if heroe_genero_m == "M":
            print(heroe["nombre"])
        
# print(imprimir_nombre_heroe_genero_m(lista_personajes))
""" 
# B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
"""
def imprimir_nombre_heroe_genero_f(lista_personajes: list[dict]) -> str:
    
    

    for heroe in lista_personajes:
        heroe_genero_f = heroe.get("genero", "No tiene genero")
        
        if heroe_genero_f == "F":
            print(heroe["nombre"])
        
""" 
# C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
""" 
def obtener_heroe_mas_alto_genero_m(lista_personajes: list[dict]) ->str:
    altura_maxima_m = float("-inf")
    heroe_mas_alto = ""

    for heroe in lista_personajes:
        heroe_genero_m = heroe.get("genero", "No tiene genero")
        if heroe_genero_m == "M":
            altura = float(heroe["altura"])
            if altura > altura_maxima_m:
                altura_maxima_m = altura
                heroe_mas_alto = heroe["nombre"]
    print(heroe_mas_alto)

"""
# D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
"""

def obtener_heroina_mas_alta_genero_f(lista_personajes: list[dict]) ->str:
    altura_maxima_f = float("-inf")
    heroina_mas_alta = ""

    for heroe in lista_personajes:
        heroe_genero_f = heroe.get("genero", "No tiene genero")
        if heroe_genero_f == "F":
            altura = float(heroe["altura"])
            if altura > altura_maxima_f:
                altura_maxima_f = altura
                heroina_mas_alta = heroe["nombre"]
    print(heroina_mas_alta)

"""
# E) Recorrer la lista y determinar cuál es el superhéroe más bajo de género M 
"""

def encontrar_altura_minima_heroe(lista_personajes: list[dict])->str:
    minima_altura = float("inf")
    heroe_altura_minima = ""

    for heroe in lista_personajes:
        heroe_genero_m = heroe.get("genero", "No tiene genero")
        if heroe_genero_m == "M":
            altura = float(heroe["altura"])
            if altura < minima_altura:
                minima_altura = altura
                if altura == minima_altura:
                    heroe_altura_minima = heroe["nombre"]
    print(heroe_altura_minima) 
"""
# F) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
"""
def encontrar_altura_minima_heroina(lista_personajes: list[dict])->str:
    minima_altura = float("inf")
    heroina_altura_minima = ""
    for heroe in lista_personajes:
        heroe_genero_f = heroe.get("genero", "No tiene genero")
        if heroe_genero_f == "F":
            altura = float(heroe["altura"])
            if altura < minima_altura:
                minima_altura = altura
                heroina_altura_minima = heroe["nombre"]
    print(heroina_altura_minima) 
"""
# G) Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
"""
def obtener_altura_promedio_heroe_genero_m(lista_personajes: list) -> str:
    acumulador_altura_m = 0
    contador_m = 0
    for heroe in lista_personajes:
        genero_heroe_m = heroe.get("genero", "No tiene genero")
        altura_m = float(heroe["altura"])    
        if genero_heroe_m == "M":
            acumulador_altura_m += altura_m
            contador_m += 1
    promedio_m = acumulador_altura_m / contador_m
    print(f"La altura promedio de los heroes es: {promedio_m}")

"""
# H) Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
"""
def obtener_altura_promedio_heroe_genero_f(lista_personajes: list) -> dict:
    acumulador_altura_f = 0
    contador_f = 0
    for heroe in lista_personajes:
        genero_heroe_f = heroe.get("genero", "No tiene genero")
        altura_f = float(heroe["altura"]) 
        if genero_heroe_f == "F":
            acumulador_altura_f += altura_f
            contador_f += 1
    promedio_f = acumulador_altura_f / contador_f
    
    print(f"La altura promedio de los heroes es: {promedio_f}")
"""
# I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F).
"""
def nombre_heroe_items_c_a_f(lista_personajes: list[dict]) -> str:
    obtener_heroe_mas_alto_genero_m(lista_personajes)
    obtener_heroina_mas_alta_genero_f(lista_personajes)
    encontrar_altura_minima_heroe(lista_personajes)
    encontrar_altura_minima_heroina(lista_personajes)
"""
# J) Determinar cuántos superhéroes tienen cada tipo de color de ojos.
"""
def obtener_cantidad_color_ojos_por_heroe(lista_personajes: list) -> int:

    cantidad_color_ojos = {}

    for heroe in lista_personajes:
        color = heroe.get("color_ojos", "Sin color")
        if not color in cantidad_color_ojos.values():
            cantidad_color_ojos[color] = 1
        else: 
            cantidad_color_ojos[color] += 1

    print(cantidad_color_ojos)
"""
# K) Determinar cuántos superhéroes tienen cada tipo de color de pelo.
"""
def obtener_cantidad_color_pelo_por_heroe(lista_personajes: list) -> int:

    cantidad_color_pelo = {}

    for heroe in lista_personajes:
        color_pelo = heroe.get("color_pelo", "Sin color")
        if not color_pelo in cantidad_color_pelo.values():
            cantidad_color_pelo[color_pelo] = 1
        else: 
            cantidad_color_pelo[color_pelo] += 1

    print(cantidad_color_pelo)
"""
# L) Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
"""
def obtener_cantidad_tipo_inteligencia_por_heroe(lista_personajes: list) -> str:

    cantidad_tipo_inteligencia = {"No tiene": 0}

    for heroe in lista_personajes:
        inteligencia = heroe.get("inteligencia", "No tiene")
        if not inteligencia in cantidad_tipo_inteligencia.keys():
            cantidad_tipo_inteligencia[inteligencia] = 1
        else: 
            cantidad_tipo_inteligencia[inteligencia] += 1

    print(cantidad_tipo_inteligencia)

"""
# M) Listar todos los superhéroes agrupados por color de ojos.
"""
def imprimir_todos_heroes_por_color_ojos(lista_personajes: list) -> list:
    diccionario_color_ojos = {}
    for heroe in lista_personajes:
        
        color_ojos = heroe.get("color_ojos").capitalize()
        nombre_color_ojos = heroe.get("nombre")

        if color_ojos in diccionario_color_ojos:
            diccionario_color_ojos[color_ojos].append(nombre_color_ojos)
        else:
            diccionario_color_ojos[color_ojos] = [nombre_color_ojos]

    # return diccionario_color_ojos
    print(diccionario_color_ojos)
    #     resultado = imprimir_heroes_por_color_ojos(lista_personajes)
    # print(resultado)
"""
# N) Listar todos los superhéroes agrupados por color de pelo.
"""
def imprimir_cantidad_color_pelo_todos_heroes(lista_personjaes: list) -> dict:
    diccionario_color_pelo = {}
    for heroe in lista_personjaes:
        color_pelos = heroe.get("color_pelo").capitalize()
        nombre_color_pelo = heroe.get("nombre")

        if color_pelos in diccionario_color_pelo:
            diccionario_color_pelo[color_pelos].append(nombre_color_pelo)
        else:
            diccionario_color_pelo[color_pelos] = [nombre_color_pelo]
    # return diccionario_color_pelo
    print(diccionario_color_pelo)
"""
# O) Listar todos los superhéroes agrupados por tipo de inteligencia
"""
def imprimir_cantidad_tipo_inteligencia_todos_heroes(lista_personjaes: list) -> dict:
    diccionario_tipo_inteligencia = {}
    for heroe in lista_personjaes:
        inteligencia = heroe.get("inteligencia").capitalize()
        nombre_inteligencia = heroe.get("nombre")

        if inteligencia in diccionario_tipo_inteligencia:
            diccionario_tipo_inteligencia[inteligencia].append(nombre_inteligencia)
        else:
            diccionario_tipo_inteligencia[inteligencia] = [nombre_inteligencia]
    
    # return diccionario_tipo_inteligencia
    print(diccionario_tipo_inteligencia)
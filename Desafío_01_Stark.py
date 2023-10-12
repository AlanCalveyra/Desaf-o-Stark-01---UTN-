
from biblioteca_stark_01 import *
#Estuve repasando el STARK PARA PODER HACERLO DE MANERA MÁS OPTIMIZADA Y NO ME SALEN LOS EJERCICIOS CON MINIMO. ADEMÁS EL MENÚ PARA SELECCIONAR QUE EJERCICIO VISUALIZAR ME DA ERROR EN VARIOS. 
# I) Ordenar el código implementando una función para cada uno de los valores informados.
# Función principal que muestra el menú y llama a las funciones correspondientes
def main_app(lista_personajes: list[dict]):
    while True:

        opcion = mostrar_menu()

        match opcion:
            case "1":
                imprimir_nombre_heroe_genero_m(lista_personajes)
            case "2":
                imprimir_nombre_heroe_genero_f(lista_personajes)
            case "3":
                obtener_heroe_mas_alto_genero_m(lista_personajes)
            case "4":
                obtener_heroina_mas_alta_genero_f(lista_personajes)

            case "5":
                encontrar_altura_minima_heroe(lista_personajes)
            case "6":
                encontrar_altura_minima_heroina(lista_personajes)

            case "7":
                obtener_altura_promedio_heroe_genero_m(lista_personajes)

            case "8":
                obtener_altura_promedio_heroe_genero_f(lista_personajes)

            case "9":
                nombre_heroe_items_c_a_f(lista_personajes)

            case "10":
                obtener_cantidad_color_ojos_por_heroe(lista_personajes)

            case "11":
                obtener_cantidad_color_pelo_por_heroe(lista_personajes)

            case "12":
                obtener_cantidad_tipo_inteligencia_por_heroe(lista_personajes)

            case "13":
                imprimir_todos_heroes_por_color_ojos(lista_personajes)
            case "14":
                imprimir_cantidad_color_pelo_todos_heroes(lista_personajes)
            case "15":
                imprimir_cantidad_tipo_inteligencia_todos_heroes(lista_personajes)

            case "16":
                break

            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                
def perdir_opcion_menu() -> str:
    opcion = input("Elegí una opción: ")
    return opcion

def mostrar_menu()-> str:
    Menu = \
    """
        "1. Imprimir el nombre de cada superhéroe de género M"
        "2. Imprimir el nombre de cada superhéroe de género F"
        "3. Encontrar superhéroe más alto de género M "
        "4. Encontrar superhéroe más alto de género F "
        "5. Encontrar superhéroe más bajo de género M "
        "6. Encontrar superhéroe más bajo  de género F"
        "7. Calcular promedio de los  superhéroes de género M"
        "8. Calcular promedio de los  superhéroes de género F"
        "9. Mostrar el Nombre del superhéroe asociado a cada uno de los indicadores "anteriores (ítems C a F).
        "10. Calcular cuántos superhéroes tienen cada tipo de color de ojos."
        "11. Calcular cuántos superhéroes tienen cada tipo de color de pelo."
        "12. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene). 
        "13. Listar todos los superhéroes agrupados por color de ojos."
        "14. Listar todos los superhéroes agrupados por color de pelo."
        "15. Listar todos los superhéroes agrupados por tipo de inteligencia"
        "16. Salir"
    """
    print(Menu)
    return perdir_opcion_menu()
#Ejecutar el menú principal

#Mostrar todos los datos



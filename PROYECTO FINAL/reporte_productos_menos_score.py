from lifestore_file import *
from operator import itemgetter

# obtener_nombre_producto tiene como propósito devolver el nombre del producto
# Tomando como argumento un product_id, el cual es el que será analizado
def obtener_nombre_producto(product_id):
    for producto in lifestore_products:
        if product_id == producto[0]:
            product_name = producto[1]
            break
    return product_name

# "generar_lista_productos_evaluados" Esta función genera una lista de los productos que tienen reseña
# Omite todos aquellos que no tienen reseñas
def generar_lista_productos_evaluados():
    list_products = []
    for product in lifestore_sales:
        list_products.append(product[1])
    list_products = list(dict.fromkeys(list_products))
    return list_products


# "generar_lista_productos_score" Esta función genera una lista con la siguiente forma lista_productos_score[producto_id, average_score, total_evaluaciones]
# La lista generada es desordenada
def generar_lista_productos_score():
    # lista_productos_general = generar_lista_productos_general()
    lista_productos_evaluados = generar_lista_productos_evaluados()
    lista_productos_score = []
    for producto in lista_productos_evaluados:
        suma_score = 0
        total_evaluaciones = 0
        for evaluacion in lifestore_sales:
            if producto == evaluacion[1]:
                suma_score += evaluacion[2]
                total_evaluaciones += 1
        lista_productos_score.append([producto,suma_score/total_evaluaciones,total_evaluaciones])
    return lista_productos_score

# "generar_lista_ordenada_menor_score" ordena de menor a mayor los productos tomando como parámetro para ordenar el average_score
def generar_lista_ordenada_menor_score():
    lista_productos_score = generar_lista_productos_score()
    lista_productos_score_ordenada = []
    lista_productos_score_ordenada = sorted(lista_productos_score, key=itemgetter(1))
    return lista_productos_score_ordenada
    

# "generar_reporte_menos_score" genera el reporte de los 5 productos peor evaluados (menor score)
# Para obtener una lista más detallada (más elementos) editar la condicional if i < 6: modificando el número de acuerdo al total de elementos que se desean en el reporte
def generar_reporte_menos_score():
    lista_productos_score_ordenada = generar_lista_ordenada_menor_score()
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Listado de productos con PEORES reseñas")
    i = 1
    for producto in lista_productos_score_ordenada:
        if i < 6:
            print(str(i) + ".- " + str(obtener_nombre_producto(producto[0])) + " ||||    score: " + str(producto[1]) + "    ||||  , ||||    total_evaluaciones: " + str(producto[2]) + "    ||||")
        else:
            break
        i += 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
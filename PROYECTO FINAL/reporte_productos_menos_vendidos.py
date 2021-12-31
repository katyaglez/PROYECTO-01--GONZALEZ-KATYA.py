from lifestore_file import *
from operator import itemgetter

# Genera una lista dinámica que almacena únicamente el product_id de los producto vendidos
def generar_lista_productos_vendidos_general():
    list_sold_products = []
    for sale in lifestore_sales:
        list_sold_products.append(sale[1])
    return list_sold_products

# obtener_nombre_producto tiene como propósito devolver el nombre del producto
# Tomando como argumento un product_id, el cual es el que será analizado
def obtener_nombre_producto(product_id):
    for producto in lifestore_products:
        if product_id == producto[0]:
            product_name = producto[1]
            break
    return product_name

# Genera una lista que almacena las diferentes categorías de los productos
def generar_lista_categorias():
    lista_categorias = []
    for producto in lifestore_products:
        lista_categorias.append(producto[3])
    lista_categorias = list(dict.fromkeys(lista_categorias))
    return lista_categorias


# "generar_lista_productos_categoria" Estas función genera listas categorizadas con los productos que pertenecen a cada categoría.
# Esta lista no incluye ventas por producto
def generar_lista_productos_categoria():
    lista_categorias = generar_lista_categorias()
    listado_productos = []
    i = 0
    for categoria in lista_categorias:
        listado_productos.append([])
        listado_productos[i].append(categoria)
        for producto in lifestore_products:
            # El índice "3" representa la categoría del producto en la lista original de lifestore_products
            if str(producto[3]) == str(categoria):
                listado_productos[i].append(producto[0])
        i+=1
    return listado_productos


# "generar_lista_productos_vendidos" genera la lista por categoria de cada producto con las unidades vendidas
# Esta lista genera las listas por categoría donde se incluyen los productos y sus ventas DESORDENADOS
def generar_lista_productos_vendidos():
    listado_productos_vendidos_general = generar_lista_productos_vendidos_general()
    listado_productos = generar_lista_productos_categoria()
    listado_productos_vendidos_categoria = []
    lista_unitaria_producto_vendidos = []
    # "j" es el contador que lleva el registro de categorias
    j = 0
    for lista_por_categoria in listado_productos:
        # i es el contador que lleva el registro de total de productos por categoria
        i = 0
        for producto in lista_por_categoria:
            lista_unitaria_producto_vendidos = []
            if i != 0:
                total_vendidos = listado_productos_vendidos_general.count(producto)
                lista_unitaria_producto_vendidos.append(producto)
                lista_unitaria_producto_vendidos.append(total_vendidos)                
                listado_productos_vendidos_categoria[j].append(lista_unitaria_producto_vendidos)
            else:
                listado_productos_vendidos_categoria.append([])
                listado_productos_vendidos_categoria[j].append([producto,0])
            i += 1
        j += 1
    return listado_productos_vendidos_categoria


# "Ordenar_lista_productos_vendidos_categoria" permite ordenar por categoria cada uno de los productos de acuerdo al número de ventas que tuvieron
#Estos son ordenados de menor a mayor con el fin de obtener los MENOS vendidos de manera ascendente hasta llegar a los MAS vendidos
def ordenar_lista_productos_vendidos_categoria():
    listado_productos_desordenados = generar_lista_productos_vendidos()
    listado_productos_ordenados = []
    listado_productos_ordenados_categoria = []
    for lista_productos_categoria in listado_productos_desordenados:
        listado_productos_ordenados_categoria = sorted(lista_productos_categoria, key=itemgetter(1))
        listado_productos_ordenados.append(listado_productos_ordenados_categoria)
    return listado_productos_ordenados


# "generar_reporte_productos_menos_vendido" genera el reporte, es decir imprime en pantalla los 5 productos menos vendidos por categoria.
# Si se quiere obtener más o menos productos vendidos por categoría modificar la condicional if j > 5 donde el número indica los elementos a mostrar
def generar_reporte_productos_menos_vendidos():
    listado_productos_ordenados = ordenar_lista_productos_vendidos_categoria()
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Reporte de productos con menores ventas por categorías")
    for lista_por_categoria in listado_productos_ordenados:
        # La variable "j" indicará unicamente la categoría, 0 al ser la primer posición de la lista, es la categoría de los productos
        j = 0
        for lista_producto in lista_por_categoria:            
            if j == 0:
                print("****************************************************************************************************************************************")
                print("****************************************************************************************************************************************")
                print("Categoría: " + lista_producto[0])
            else:
                if j > 5:
                    break
                print(str(j) + ".- " + str(obtener_nombre_producto(lista_producto[0])) +  " el cual se vendió " + str(lista_producto[1]) + " veces")
            j += 1
        print("****************************************************************************************************************************************")
        print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
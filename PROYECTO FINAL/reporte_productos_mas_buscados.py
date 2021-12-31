from lifestore_file import *

# Genera una lista dinámica que almacena únicamente el product_id de los productos buscados
def generar_lista_productos_buscados():
    list_searched_products = []
    for search in lifestore_searches:
        list_searched_products.append(search[1])
    return list_searched_products

# obtener_nombre_producto tiene como propósito devolver el nombre del producto
# Tomando como argumento un product_id, el cual es el que será analizado
def obtener_nombre_producto(product_id):
    for producto in lifestore_products:
        if product_id == producto[0]:
            product_name = producto[1]
            break
    return product_name

# Esta función se encarga de obtener el producto más repetido (más buscado) 
# Recibe como parámetro un producto que puede ya haber sido evaluado o no
def obtener_productos_mas_buscados(productos_evaluados_buscados = []):
    productos_buscados = generar_lista_productos_buscados()
    productos_evaluados = []

    # Esta condiciona evalua si ya hay productos evaluados en la lista de buscados
    # Si ya los hay, los agrega a la lista de "productos_evaluados" cuyo propósito es excluir los productos anteriormente analizados
    # Si no hay productos analizados, el flujo salta únicamente la condicional
    if productos_evaluados_buscados:
        for producto in productos_evaluados_buscados:
            productos_evaluados.append(producto)

    # moda = [product_id, repeticiones]
    moda = [0,0]
    i = 0
    for producto_actual in productos_buscados:
        if producto_actual not in productos_evaluados:
            productos_evaluados.append(productos_buscados[i])
            repeticiones = productos_buscados.count(producto_actual)
            if repeticiones > moda[1]:
                moda[0] = producto_actual
                moda[1] = repeticiones
        else:
            productos_buscados.pop(i)
    return moda

# Esta función genera la salida (reporte) de los productos más buscados
# Para obtener una lista mayor, modificar la variable "productos_a_obtener"
# Por defecto esta variable fue seteada a 10
def generar_reporte_productos_mas_buscados():
    productos_a_obtener = 10
    contador = 0
    # reporte_productos almacena los productos más buscados así como el número de veces que cada producto se buscó
    # reporte_productos = [product_id, # de veces buscado]
    reporte_productos = []
    #productos_evaluados almacena únicamente los productos más buscados
    productos_evaluados_buscados = []
    while contador < productos_a_obtener:
        if productos_evaluados_buscados:
            reporte_productos.append(obtener_productos_mas_buscados(productos_evaluados_buscados))
        else:
            reporte_productos.append(obtener_productos_mas_buscados())
        productos_evaluados_buscados.append(reporte_productos[contador][0])
        contador += 1
    i = 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Lista de los " + str(productos_a_obtener) + " más buscados")
    for reporte_unitario_producto in reporte_productos:
        product_name = obtener_nombre_producto(reporte_unitario_producto[0])

        print(str(i) + ".- " + product_name + " el cual se buscó " + str(reporte_unitario_producto[1]) + " veces")
        i += 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
from lifestore_file import *

# Genera una lista dinámica que almacena únicamente el product_id de los producto vendidos
def generar_lista_productos_vendidos():
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

# Esta función se encarga de obtener el producto más repetido (más vendido) 
# Recibe como parámetro un producto que puede ya haber sido evaluado o no
def obtener_productos_mas_vendidos(productos_evaluados_vendidos = []):
    productos_vendidos = generar_lista_productos_vendidos()
    productos_evaluados = []

    # Esta condiciona evalua si ya hay productos evaluados en la lista de vendidos
    # Si ya los hay, los agrega a la lista de "productos_evaluados" cuyo propósito es excluir los productos anteriormente analizados
    # Si no hay productos analizados, el flujo salta únicamente la condicional
    if productos_evaluados_vendidos:
        for producto in productos_evaluados_vendidos:
            productos_evaluados.append(producto)

    # moda = [product_id, repeticiones]
    moda = [0,0]
    i = 0
    for producto_actual in productos_vendidos:
        if producto_actual not in productos_evaluados:
            productos_evaluados.append(productos_vendidos[i])
            repeticiones = productos_vendidos.count(producto_actual)
            if repeticiones > moda[1]:
                moda[0] = producto_actual
                moda[1] = repeticiones
        else:
            productos_vendidos.pop(i)
    return moda

# Esta función genera la salida (reporte) de los productos más vendidos
# Para obtener una lista mayor, modificar la variable "productos_a_obtener"
# Por defecto esta variable fue seteada a 5
def generar_reporte_productos_mas_vendidos():
    productos_a_obtener = 5
    contador = 0
    # reporte_productos almacena los productos más vendidos así como el número de veces que cada producto se vendió
    # reporte_productos = [product_id, # de veces vendido]
    reporte_productos = []
    #productos_evaluados almacena únicamente los productos más vendidos
    productos_evaluados_vendidos = []
    while contador < productos_a_obtener:
        if productos_evaluados_vendidos:
            reporte_productos.append(obtener_productos_mas_vendidos(productos_evaluados_vendidos))
        else:
            reporte_productos.append(obtener_productos_mas_vendidos())
        productos_evaluados_vendidos.append(reporte_productos[contador][0])
        contador += 1
    i = 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Lista de los " + str(productos_a_obtener) + " más vendidos")
    for reporte_unitario_producto in reporte_productos:
        product_name = obtener_nombre_producto(reporte_unitario_producto[0])

        print(str(i) + ".- " + product_name + " el cual se vendió " + str(reporte_unitario_producto[1]) + " veces")
        i += 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
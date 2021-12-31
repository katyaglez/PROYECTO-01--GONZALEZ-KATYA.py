from lifestore_file import *
from operator import itemgetter

def generar_ingresos_anuales():
    count_2019 = 0
    count_2020 = 0
    count_ingresos_2019 = 0
    count_ingresos_2020 = 0

    for venta in lifestore_sales:
        date_split = venta[3].split("/")
        year_split = str(int(date_split[2]))
        product_id = venta[1]
        precio = 0
        # For para obtener el precio del articulo
        for product in lifestore_products:
            if product_id == product[0]:
                precio = product[2]
                break
        if year_split == "2020":
            count_2020 += 1
            count_ingresos_2020 += precio
        elif year_split == "2019":
            count_2019 += 1
            count_ingresos_2019 += precio
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Ventas totales anuales")
    print("Total de ventas en 2019: " + str(count_2019) + " articulos vendidos")
    print("Total de ventas en 2020: " + str(count_2020) + " articulos vendidos")
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Ingresos totales anuales")
    print("Total de ingresos en 2019: " + str(count_ingresos_2019))
    print("Total de ingresos en 2020: " + str(count_ingresos_2020))
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
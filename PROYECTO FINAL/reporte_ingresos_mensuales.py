from lifestore_file import *
from operator import itemgetter

def generar_ingresos_mensuales():
    product_id = 0
    month = ""
    # Se establece una variable fija para cada mes, debido a que los meses no son variables
    # Un año siempre tendrá 12 meses
    count_jan = 0
    count_feb = 0
    count_mar = 0
    count_apr = 0
    count_may = 0
    count_jun = 0
    count_jul = 0
    count_aug = 0
    count_sep = 0
    count_oct = 0
    count_nov = 0
    count_dec = 0
    for venta in lifestore_sales:
        date_split = venta[3].split("/")
        month = str(int(date_split[1]))
        product_id = venta[1]
        precio = 0

        # For para obtener el precio del articulo
        for product in lifestore_products:
            if product_id == product[0]:
                precio = product[2]
                break
        # Se establece una condicional fija para cada mes, debido a que los meses no son variables
        # Un año siempre tendrá 12 meses
        if month == '1':
            count_jan += precio
        elif month == '2':
            count_feb += precio
        elif month == '3':
            count_mar += precio
        elif month == '4':
            count_apr += precio
        elif month == '5':
            count_may += precio
        elif month == '6':
            count_jun += precio
        elif month == '7':
            count_jul += precio
        elif month == '8':
            count_aug += precio
        elif month == '9':
            count_sep += precio
        elif month == '10':
            count_oct += precio
        elif month == '11':
            count_nov += precio
        elif month == '12':
            count_dec += precio
    lista_ingresos_meses = []
    lista_ingresos_meses.append(["Enero",count_jan])
    lista_ingresos_meses.append(["Febrero",count_feb])
    lista_ingresos_meses.append(["Marzo",count_mar])
    lista_ingresos_meses.append(["Abril",count_apr])
    lista_ingresos_meses.append(["Mayo",count_may])
    lista_ingresos_meses.append(["Junio",count_jun])
    lista_ingresos_meses.append(["Julio",count_jul])
    lista_ingresos_meses.append(["Agosto",count_aug])
    lista_ingresos_meses.append(["Septiembre",count_sep])
    lista_ingresos_meses.append(["Octubre",count_oct])
    lista_ingresos_meses.append(["Noviembre",count_nov])
    lista_ingresos_meses.append(["Diciembre",count_dec])
    print("Reporte ingresos totales mensuales")
    print("Ingresos en Enero: " + str(count_jan))
    print("Ingresos en Febrero: " + str(count_feb))
    print("Ingresos en Marzo: " + str(count_mar))
    print("Ingresos en Abril: " + str(count_apr))
    print("Ingresos en Mayo: " + str(count_may))
    print("Ingresos en Junio: " + str(count_jun))
    print("Ingresos en Julio: " + str(count_jul))
    print("Ingresos en Agosto: " + str(count_aug))
    print("Ingresos en Septiembre: " + str(count_sep))
    print("Ingresos en Octubre: " + str(count_oct))
    print("Ingresos en Noviembre: " + str(count_nov))
    print("Ingresos en Diciembre: " + str(count_dec))


    # En esta parte se calculan los meses con mayores ingresos.
    lista_ingresos_meses_sorted = []
    lista_ingresos_meses_sorted = sorted(lista_ingresos_meses, key=itemgetter(1))
    lista_ingresos_meses_sorted = lista_ingresos_meses_sorted[::-1]
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
    print("Reporte de meses con mayores ingresos")
    i = 1
    for meses in lista_ingresos_meses_sorted:
        print(str(i) + ".- " + meses[0] + " || Ingresos: " + str(meses[1]))
        i += 1
    print("****************************************************************************************************************************************")
    print("****************************************************************************************************************************************")
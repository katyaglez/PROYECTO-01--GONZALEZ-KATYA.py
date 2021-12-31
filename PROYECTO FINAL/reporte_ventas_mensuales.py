from lifestore_file import *

def generar_numero_ventas_mensual():
    lista_ventas_anuales = []
    month = ""
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
        if month == '1':
            count_jan += 1
        elif month == '2':
            count_feb += 1
        elif month == '3':
            count_mar += 1
        elif month == '4':
            count_apr += 1
        elif month == '5':
            count_may += 1
        elif month == '6':
            count_jun += 1
        elif month == '7':
            count_jul += 1
        elif month == '8':
            count_aug += 1
        elif month == '9':
            count_sep += 1
        elif month == '10':
            count_oct += 1
        elif month == '11':
            count_nov += 1
        elif month == '12':
            count_dec += 1
    
    print("Reporte ventas totales mensuales")
    print("Ventas en Enero: " + str(count_jan))
    print("Ventas en Febrero: " + str(count_feb))
    print("Ventas en Marzo: " + str(count_mar))
    print("Ventas en Abril: " + str(count_apr))
    print("Ventas en Mayo: " + str(count_may))
    print("Ventas en Junio: " + str(count_jun))
    print("Ventas en Julio: " + str(count_jul))
    print("Ventas en Agosto: " + str(count_aug))
    print("Ventas en Septiembre: " + str(count_sep))
    print("Ventas en Octubre: " + str(count_oct))
    print("Ventas en Noviembre: " + str(count_nov))
    print("Ventas en Diciembre: " + str(count_dec))
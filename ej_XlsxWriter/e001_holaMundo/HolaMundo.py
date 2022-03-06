#Primer ejemplo de uso de la libreria xlswriter
from xlsxwriter import Workbook

#creando un librode calculo
libro=Workbook("Hola.xlsx")

#creando hoja en el libro de calculo
NuevaHoja=libro.add_worksheet("Hoja")

#escribiendo mensaje hola mundo
NuevaHoja.write("A1","Hola mundo! :)")

#cerrando la hoja y guardando los cambios
libro.close()

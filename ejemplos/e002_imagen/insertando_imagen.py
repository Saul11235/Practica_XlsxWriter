#ejemplo insertando una imagen
from xlsxwriter import Workbook

#creando libro y hojas
libro=Workbook("LibroConImagen.xlsx")
hoja=libro.add_worksheet("HojaNueva")

#Colocando nueva imagen
hoja.insert_image("B2","EjemploImagen.png")

#grabando el libro
libro.close()


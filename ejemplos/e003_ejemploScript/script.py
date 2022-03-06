#ejemplo de script 
print("\nPrograma de ejemplo 4 elementos\n")
print("indicar 4 ingredientes y crearemos el presupuesto total")
lista=[["ELEMENTO","PRECIO"]] #elemento con la cabecera
#--leyendo elementos ----------------------------------
for x in range(4):
    print("elemento : "+str(x+1))
    nombre=input("\tNombre : ")
    try:
        precio=float(input("\tPrecio : "))
    except:
        print("  Error, pero diremos que es "+str(x))
        precio=x
    lista.append([nombre,precio])
#------------------------------------------------------    
#creando libro
from xlsxwriter import Workbook
archivo=Workbook("ejemplo.xlsx")
#creando hoja 
hoja=archivo.add_worksheet("Hoja de trabajo")
hoja.write(1,1,"TABLA DE CALCULO")
#colocando los elementos de la tabla
contador=0
for x in  lista:
    hoja.write(3+contador,1,x[0])
    if contador==0:
        hoja.write(3,2,x[1])
    else:
        hoja._write_number(3+contador,2,int(x[1]))
    contador+=1
#-Escribiendo la suma de todo    
hoja.write(3+contador,1,"TOTAL->")
hoja.write_formula(3+contador,2,"=SUM(C5:C8)")
#cerrando libro y guardando
archivo.close()
#------------------------------------------------------
#abriendo automaticamente el libro
from os import system
system("ejemplo.xlsx")

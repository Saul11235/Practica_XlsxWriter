#ujemplo de uso de temas
from xlsxwriter import Workbook

#creando objetos libro y hoja
libro=Workbook("ejemplo.xlsx")
hoja=libro.add_worksheet("Hoja")

#Creando estilos, ver todos los elementos disponibles
tema1=libro.add_format({"bold":True,"font_color":"red","bg_color":"yellow"})
tema2=libro.add_format({"underline":True,"font_size":18,"font_color":"blue"})

#escribiendo
hoja.write(1,1,"Hola soy un comentario con un tema",tema1)
hoja.write(3,1,"Hola soy otro comentario",tema2)


libro.close()
#Abriendo hoja de calculo-----------------
from os import system
system("ejemplo.xlsx")


# referencia format
#
#  https://xlsxwriter.readthedocs.io/format.html
#
# Font 	
#   Font type 	      'font_name' 	
#  	Font size 	      'font_size' 
#  	Font color 	      'font_color' 	
#  	Bold      	      'bold' 
#  	Italic            'italic'
#  	Underline         'underline'
#  	Strikeout 	      'font_strikeout' 	
#  	Super/Subscript   'font_script'
#
# Number
#   Numeric format    'num_format'
#
# Protection 
#   Lock cells 	      'locked' 
#  	Hide formulas 	  'hidden'
#
# Alignment 
#   Horizontal align  'align'
#  	Vertical align    'valign'
#  	Rotation          'rotation'
#  	Text wrap         'text_wrap'
#  	Reading order 	  'reading_order'
#  	Justify last 	  'text_justlast' 
#  	Center across 	  'center_across' 
#  	Indentation 	  'indent'
#  	Shrink to fit 	  'shrink'
#
# Pattern 
#   Cell pattern      'pattern'
#  	Background color  'bg_color' 
#  	Foreground color  'fg_color'
#
# Border 
#   Cell border 	  'border' 
#  	Bottom border 	  'bottom' 
#  	Top border 	      'top' 
#  	Left border       'left' 
#  	Right border 	  'right' 
#  	Border color 	  'border_color' 
#  	Bottom color 	  'bottom_color' 
#  	Top color 	      'top_color' 
#  	Left color 	      'left_color' 
#  	Right color 	  'right_color' 	
#
#

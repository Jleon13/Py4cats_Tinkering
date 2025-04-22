import py4cats

from py4cats.var.pairTypes import Interval
from py4cats.lbl.higstract import higstract
# Define el rango de números de onda
x_limits = Interval(2100., 2150.)  # Ajusta el rango según tus necesidades

# Ruta al archivo en formato HITRAN
line_file = 'CO_HITRAN_fixed.txt'  # Asegúrate de que este archivo exista y tenga el formato correcto

# Nombre de la molécula
molecule = 'CO'

# Leer los datos con higstract
dll = higstract(line_file, x_limits, molecule=molecule)

# Imprime los datos cargados
print(dll)

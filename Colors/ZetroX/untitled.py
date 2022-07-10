OK =   '\033[92m' # Verde
WARN = '\033[93m' # Amarillo
FAIL = '\033[91m' # Rojo
ENDC = '\033[0m'  # ENDC significa END COLOR
print( "{}Success!{}".format(OK,ENDC) )
# En el siguiente caso solo la parte de "Error:" tendrá color rojo, el resto será el que tenga por defecto la terminal
print( "{}Error:{} File not found.".format(FAIL ,ENDC) )

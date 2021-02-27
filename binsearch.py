import os
from os import remove, path
import argparse
import sys

dir = 'Bincodes/'
elementsT = []
numbincode = []


print("""
    ..........................................................................................
    :########::'####:'##::: ##::'######::'########::::'###::::'########:::'######::'##::::'##:
    :##.... ##:. ##:: ###:: ##:'##... ##: ##.....::::'## ##::: ##.... ##:'##... ##: ##:::: ##:
    :##:::: ##:: ##:: ####: ##: ##:::..:: ##::::::::'##:. ##:: ##:::: ##: ##:::..:: ##:::: ##:
    :########::: ##:: ## ## ##:. ######:: ######:::'##:::. ##: ########:: ##::::::: #########:
    :##.... ##:: ##:: ##. ####::..... ##: ##...:::: #########: ##.. ##::: ##::::::: ##.... ##:
    :##:::: ##:: ##:: ##:. ###:'##::: ##: ##::::::: ##.... ##: ##::. ##:: ##::: ##: ##:::: ##:
    :########::'####: ##::. ##:. ######:: ########: ##:::: ##: ##:::. ##:. ######:: ##:::: ##:
    ........:::....::..::::..:::......:::........::..:::::..::..:::::..:::......:::..:::::..:: 
                                                             
""")

if path.exists("Resultado.txt"):
    remove("Resultado.txt")

#Bucle para recorrer los ficheros dentro de un directorio
with os.scandir(dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]

#Bucle para recorrer las lineas dentro de cada fichero
for archivo in ficheros:
    with open(dir + archivo, 'r') as file:
        for line in file:
            #print(line)
            numbincode.append(line.rstrip('\n'))

#Carga los elementos del txt tarjetas
with open("tarjetas.txt", 'r', 1,"UTF-8") as ficheroT:
    for line in ficheroT:
        elementsT.append(line.rstrip('\n'))

# Comparar los datos de tarketas.txt con los ficheros
# dentro del directorio Bincodes
def comparativa(verbose, beginning):
    
    #Comienzo del programa
    print("\nBuscando, espere un momento....\n")       

    #Abrir fichero para los resultados
    resultado = open("Resultado.txt", "a", 10, "utf-8")
       
    #Bucle para recorrer las lineas de cada fichero
    for archivo in ficheros:
        # pretty se usa para escribir el nombre del cliente en el txt resultado
        pretty = archivo.rstrip('.txt').lstrip('bincode')
        if verbose == True:
            print("Resultados de " + pretty + ":")
            
        resultado.write("----------------------------------------" + pretty + "----------------------------------------\n")
        with open(dir + archivo, 'r') as file:
            for linea in file:
                linea = linea.rstrip('\n')
                #Bucle para recorrer las tarjetas en tarjets.txt
                for tarjeta in elementsT:
                    # Bucle para recorrer los bines dentro de cada fichero de bins.txt
                    for bins in numbincode:
                        # Habilitar la búsqueda por los 6 primeros dígitos
                        if beginning == True:
                            if tarjeta[0:6].find(bins) != -1 and linea.find(bins) != -1:
                                if verbose == True:
                                    archivo = archivo.rstrip('.txt').lstrip('bincode')
                                    print("Bincode de " + archivo + " " + bins + " la tarjeta es: "+ tarjeta)
                                resultado.write(tarjeta + "\n")
                        else:
                        # Si la tarjeta encuentra un bin en bines y en las lineas del archivo se encuentra el bin entonces
                            if tarjeta.find(bins) != -1 and linea.find(bins) != -1:
                                if verbose == True:
                                    archivo = archivo.rstrip('.txt').lstrip('bincode')
                                    print("Bincode de " + archivo + " " + bins + " la tarjeta es: "+ tarjeta)
                                resultado.write(tarjeta + "\n")
        resultado.write("----------------------------------------------------------------------------------------------------\n\n\n")
        if verbose == True:
            print("\n")
    resultado.close()
    print("¡LISTO! Comprueba los resultados en Resultado.txt\n")                  


def main(argv):
    """ FUNCTION MAIN """

    parser = argparse.ArgumentParser(
        description="This tool facilitates the search of the 6 digits of the Bincodes by pasting the text in a document with txt extension.")
    parser.add_argument(
        "-v", "--verbose", help="Enable verbose", action="store_true")
    parser.add_argument(
        '-b', '--beginning', help="Enable search from the beginning", action="store_true")
    args = parser.parse_args()
    #Expresiones booleanas de si existe el parametro que se ha pasado
    verbose = args.verbose
    beginning = args.beginning
    
    comparativa(verbose, beginning)


if __name__ == "__main__":
    main(sys.argv[1:])
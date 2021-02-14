#descargar colorama:  pip install colorama
from atexit import register
from colorama import Fore, Back, Style, init
from os import remove, path

init() #Importante para el colorama!

#array para los bincodes guardados en los txt de cada empresa
#tarjetas
elementsT = []
#davivienda
bincodeD = []
#bancolombia
bincodeB = []
#Cajamar
bincodeC = []
#Bancamia
bincodeBancaM = []
#Credito Agricola
bincodeCred = []
#BBVA
bincodeBBVA = []


#Búsqueda para los 6 PRIMEROS NÚMEROS
startlock = 0
stoplock = 6

#Habilitar output por consola true = si, false = no
#modificar en caso de mostrar contenido por consola
output = True

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

#Funcion para comparar bincodes
def comparativa():
    
    print("Buscando, espere un momento....")

    for tarjeta in elementsT:
        for binCaja in bincodeC:
            # Si en los 6 primeros caracteres de la tarjeta encuentra el bincode entra
            if tarjeta[startlock:stoplock].find(binCaja)!= -1:
                #Creación de un output verificando que es correcto
                if output == True:
                    print('\nBincode Cajamar ' + Back.GREEN + binCaja + Style.RESET_ALL + ' la tarjeta es: ' + Back.GREEN + tarjeta + Style.RESET_ALL)
                #Generación de un archivo para trabajar de forma más ordenada
                file = open("resultadoCajamar.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()

        for binDavi in bincodeD:
            if tarjeta[startlock:stoplock].find(binDavi)!= -1:
                if output == True:
                    print('\nBincode Davivienda ' + Back.RED + binDavi + Style.RESET_ALL + ' la tarjeta es: ' + Back.RED + tarjeta + Style.RESET_ALL)
                file = open("resultadoDavivienda.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()

        for binBan in bincodeB:
            if tarjeta[startlock:stoplock].find(binBan)!= -1:
                if output == True:
                    print('\nBincode Bancolombia ' + Back.BLUE+ binBan + Style.RESET_ALL + ' la tarjeta es: ' + Back.BLUE + tarjeta + Style.RESET_ALL)
                file = open("resultadoBancolombia.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()

        for binBancamia in bincodeBancaM:
            if tarjeta[startlock:stoplock].find(binBancamia)!= -1:
                if output == True:
                    print('\nBincode Bancamia ' + Back.BLACK+ binBancamia + Style.RESET_ALL + ' la tarjeta es: ' + Back.BLACK + tarjeta + Style.RESET_ALL)
                file = open("resultadoBancamia.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()

        for binCred in bincodeCred:
            if tarjeta[startlock:stoplock].find(binCred)!= -1:
                if output == True:
                    print('\nBincode Credito Agricola ' + Back.CYAN + binCred + Style.RESET_ALL + ' la tarjeta es: ' + Back.CYAN + tarjeta + Style.RESET_ALL)
                file = open("resultadoCreditoAgricola.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()

        for binBBVA in bincodeBBVA:
            if tarjeta[startlock:stoplock].find(binBBVA)!= -1:
                if output == True:
                    print('\nBincode BBVA ' + Back.YELLOW + Fore.BLACK + binBBVA + Style.RESET_ALL + ' la tarjeta es: ' + Back.YELLOW + Fore.BLACK + tarjeta + Style.RESET_ALL)
                file = open("resultadoBBVA.txt", "a", 10, "utf-8")
                file.write(tarjeta + "\n")
                file.close()
    
    print("\n"+ Back.BLACK + Fore.RED+ "            Programa Completado                " + Style.RESET_ALL) 

#Función para imprimir todos los resultados en un mismo txt
def compactar():
    resultado = open("Resultado.txt", "a", 10, "utf-8")
    resultado.write("----------------------------DAVIVIENDA----------------------------\n")
    #Estructura with for para leer lineas dentro de un archivo
    if path.exists("resultadoDavivienda.txt"):
        with open ("resultadoDavivienda.txt", "r") as fichero_result:
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoDavivienda.txt")

    if path.exists("resultadoCajamar.txt"):
        with open ("resultadoCajamar.txt", "r") as fichero_result:
            resultado.write("------------------------------CAJAMAR-----------------------------\n")
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoCajamar.txt")

    if path.exists("resultadoBancamia.txt"):
        with open ("resultadoBancamia.txt", "r") as fichero_result:
            resultado.write("-----------------------------BANCAMÍA-----------------------------\n")
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoBancamia.txt")

    if path.exists("resultadoCreditoAgricola.txt"):
        with open ("resultadoCreditoAgricola.txt", "r") as fichero_result:
            resultado.write("-------------------------CREDITO AGRICOLA-------------------------\n")
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoCreditoAgricola.txt")


    if path.exists("resultadoBancolombia.txt"):
        with open ("resultadoBancolombia.txt", "r") as fichero_result:
            resultado.write("----------------------------BANCOLOMBIA---------------------------\n")
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoBancolombia.txt")

    if path.exists("resultadoBBVA.txt"):
        with open ("resultadoBBVA.txt", "r") as fichero_result:
            resultado.write("--------------------------BBVA Colombia---------------------------\n")
            for line in fichero_result:
                resultado.write(line)
            resultado.write("------------------------------------------------------------------\n\n")
        remove("resultadoBBVA.txt")

    resultado.close()
        

    print(Back.BLACK + Fore.RED+ "      Revisa el fichero Resultado.txt          " + Style.RESET_ALL + "\n")


#Carga los elementos a revisar en Davivienda
with open("Bincodes/bincodeDavivienda.txt", 'r') as fichero:
    for line in fichero:
        bincodeD.append(line.rstrip('\n'))
    
#Carga los elementos a revisar en Bancolombia
with open("Bincodes/bincodeBancolombia.txt", 'r') as fichero:
    for line in fichero:
        bincodeB.append(line.rstrip('\n'))

#Carga los elementos a revisar en Cajamar
with open("Bincodes/bincodeCajamar.txt", 'r') as fichero:
    for line in fichero:
        bincodeC.append(line.rstrip('\n'))

#Carga los elementos a revisar en Bancamia
with open("Bincodes/bincodeBancamia.txt", 'r') as fichero:
    for line in fichero:
        bincodeBancaM.append(line.rstrip('\n'))
        
#Carga los elementos a revisar en Credito Agricola
with open("Bincodes/bincodeCreditoAgricola.txt", 'r') as fichero:
    for line in fichero:
        bincodeCred.append(line.rstrip('\n'))

#Carga los elementos a revisar en BBVA
with open("Bincodes/bincodeBBVA.txt", 'r') as fichero:
    for line in fichero:
        bincodeBBVA.append(line.rstrip('\n'))
        
#Carga los elementos del txt tarjetas
with open("tarjetas.txt", 'r', 1,"UTF-8") as ficheroT:
    for line in ficheroT:
        elementsT.append(line.rstrip('\n'))

        

comparativa()
compactar()
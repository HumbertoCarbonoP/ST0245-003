desicion = 'Y'
nArchivo = None
archivos = []

def guardarCSV(nombre):
    archivo = open(nombre, "r")
    lineas = archivo.readlines()
    return lineas

try:
    nArchivo = input('Escriba el nombre del arcivo .csv que desea almacenar: ')
    archivos.append(guardarCSV(nArchivo))
    esicion = input('¿Desea agregar otro archivo? escriba "Y" para agregar otro, de lo contrario escriba "N": ')

    while desicion=='Y':
        nArchivo = input('Esbriba el nombre del siguiente archivo: ')
        archivos.append(guardarCSV(nArchivo))
        desicion = input('¿Desea agregar otro archivo? escriba "Y" para agregar otro, de lo contrario escriba "N": ')
    print(archivos)

except:
    print('El nombre del archivo es incorrecto.')
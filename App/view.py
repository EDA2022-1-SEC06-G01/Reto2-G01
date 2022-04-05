"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
import model



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ====================================================
# Inicializacion de la comunicacion con el controlador
# ====================================================

def newCatalog():
    """
    Se crea una instancia del controlador
    """
    control = controller.newCatalog()
    return control




# ===================================
# Funciones para imprimir resultados
# ===================================





# ================================
# Funcion para inicializar el menu
# ================================

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- req 1")
    print("3- req 2")
    print("4- req 3")

catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = newCatalog()
        delta_time, delta_memory = controller.loadData(catalog)
        print(mp.size(catalog['model']['albums_id']))
        print(mp.size(catalog['model']['artists_id']))
        print(mp.size(catalog['model']['tracks_id']))
        
    elif int(inputs[0]) == 2:
        year = int(input("Introduzca el anio que desea consultar: "))
        albumsLST, lst_size = controller.requerimiento1(catalog, year)
        print(lt.firstElement(albumsLST))
        print(lt.lastElement(albumsLST))
        print(lst_size)

    elif int(inputs[0]) == 3:
        popularity = int(input("Introduzca la popularidad que desea consultar: "))
        albumsLST, lst_size = controller.requerimiento2(catalog, popularity)
        print(lt.firstElement(albumsLST))
        print(lt.lastElement(albumsLST))
        print(lst_size)

    elif int(inputs[0]) == 4:
        popularity = int(input("Ingrese la popularidad que desea consultar (0-100):"))
        tracks, lstsize = controller.requerimiento3(catalog, popularity)
        print(lt.firstElement(tracks))
        print(lt.lastElement(tracks))
        print(lstsize)
        
    elif int(inputs[0]) == 5:
        artista = input("Introduzca el artista que desea consultar: ")
        mercado = input("Introduzca el mercado que desea consultar: ")
        print(lt.firstElement(model.requerimiento4(catalog, artista, mercado)))

    elif int(inputs[0]) == 6:
        artista = input("Introduzca el artista que desea consultar: ")
        albums_artista, listaCancionesPopulares, album_sencillo, album_recopilacion, album_album = model.requerimiento5(catalog, artista)
        print(album_recopilacion)
        print(album_sencillo)
        print(album_album)

    else:
        sys.exit(0)
sys.exit(0)

# Various Artists
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
from prettytable import PrettyTable



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

def printRequerimiento1(lst, cantidad_albumes, year):
    print("========= Req No. 1 Inputs =========")
    print(f"Albums released in {year}")
    print()
    print("========= Req No. 1 Answer =========")
    print(f"There are {cantidad_albumes} albums released in {year}")
    print()
    print(f"The first 3 and last 3 albums in {year} are...")
    table = PrettyTable()
    table.field_names = ["name", "release_date", "total_tracks", "album_type", "artist_album_name", "external_urls"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["name"], current_lst["release_date"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"][13:-2]])

    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])

    for _ in range(cantidad_albumes - 2, cantidad_albumes + 1):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["name"], current_lst["release_date"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"][13:-2]])
    return table.get_string()


def printRequerimiento2(lst, cantidad_artistas, popularity):
    print("========= Req No. 2 Inputs =========")
    print(f"The artists with popularity rating of: {popularity}")
    print()
    print("========= Req No. 2 Answer =========")
    print(f"There are {cantidad_artistas} artists with {popularity}")
    print()
    print(f"The first 3 and last 3 artists with {popularity} are...")
    table = PrettyTable()
    table.field_names = ["artist_popularity", "followers", "name", "relevant_track_name", "genres"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), current_lst["genres"]])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(cantidad_artistas - 2, cantidad_artistas + 1):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), current_lst["genres"]])
        
    return table.get_string()


# ================================
# Funcion para inicializar el menu
# ================================

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Examinar los albumes en un anio de interes | Requerimiento 1")
    print("3- Encontrar los artistas por popularidad | Requerimiento 2 (Individual)")
    print("4- Encontrar las canciones por popularidad | Requerimiento 3 (Individual)")
    print("5- Encontrar la cancion mas popular de un artista | Requerimiento 4")
    print("6- Encontrar la discografia de un artista | Requerimiento 5")
    print("7- Clasificar las canciones de artistas con mayor distribucion")


catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n> ')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = newCatalog()
        delta_time, delta_memory = controller.loadData(catalog)
        #print(mp.size(catalog['model']['albums_id']))
        #print(mp.size(catalog['model']['artists_id']))
        #print(mp.size(catalog['model']['tracks_id']))
        
    elif int(inputs[0]) == 2:
        year = int(input("Introduzca el anio que desea consultar: "))
        albumsLST, cantidad_albumes = controller.requerimiento1(catalog, year)
        #print(lt.firstElement(albumsLST))
        #print(lt.lastElement(albumsLST))
        #print(cantidad_albumes)
        print(printRequerimiento1(albumsLST, cantidad_albumes, year))
        print("cargo")

    elif int(inputs[0]) == 3:
        popularity = int(input("Introduzca la popularidad que desea consultar: "))
        artistLST, numero_canciones = controller.requerimiento2(catalog, popularity)
        #print(lt.firstElement(artistLST))
        #print(lt.lastElement(artistLST))
        #print(numero_canciones)
        print(printRequerimiento2(artistLST, numero_canciones, popularity))
        print(lt.lastElement(artistLST))

    elif int(inputs[0]) == 4:
        popularity = int(input("Ingrese la popularidad que desea consultar (0-100):"))
        tracks, lstsize = controller.requerimiento3(catalog, popularity)
        #print(lt.firstElement(tracks))
        #print(lt.lastElement(tracks))
        #print(lstsize)
        
    elif int(inputs[0]) == 5:
        artista = input("Introduzca el artista que desea consultar: ")
        mercado = input("Introduzca el mercado que desea consultar: ")
        canciones = controller.requerimiento4(catalog, artista, mercado)
        #print(lt.firstElement(canciones))

    elif int(inputs[0]) == 6:
        artista = input("Introduzca el artista que desea consultar: ")
        albums_artista, listaCancionesPopulares, album_sencillo, album_recopilacion, album_album = controller.requerimiento5(catalog, artista)
        #print(album_recopilacion)
        #print(album_sencillo)
        #print(album_album)
        # Falta debug sorting

    elif int(inputs[0]) == 7:
        pass
        #print(f"Cantidad albums_id: {mp.size(catalog['model']['albums_id'])}")
        #print(f"Cantidad artists_id: {mp.size(catalog['model']['artists_id'])}")
        #print(f"Cantidad artistsName_id: {mp.size(catalog['model']['artistsName_id'])}")
        #print(f"Cantidad tracks_id: {mp.size(catalog['model']['tracks_id'])}")
        #print(f"Cantidad anio_albumID: {mp.size(catalog['model']['anio_albumID'])}")
        #print(f"Cantidad artistPopularity_artistID: {mp.size(catalog['model']['artistPopularity_artistID'])}")
        #print(f"Cantidad canciones_por_artistas: {mp.size(catalog['model']['canciones_por_artistas'])}")
        #print(f"Cantidad albumes_por_artistas: {mp.size(catalog['model']['albumes_por_artistas'])}")

    else:
        sys.exit(0)
sys.exit(0)

# Various Artists
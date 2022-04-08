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
import pycountry
import pandas



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
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(cantidad_artistas - 2, cantidad_artistas + 1):
        current_lst = lt.getElement(lst, _)
        
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])
    return table.get_string()


def printRequerimiento3(lst, size, popularity):
    print("========= Req No. 3 Inputs =========")
    print(f"The trakcs with popularity rating of: {popularity}")
    print()
    print("========= Req No. 3 Answer =========")
    print(f"There are {size} tracks with {popularity}")
    print()
    print(f"The first 3 and last 3 tracks with {popularity} are...")
    table = PrettyTable()
    table.field_names= ['popularity','duration_ms','name_track', 'disc_number', 'track_number', 'album_name', 'artists_names', 'href', 'lyrics']
    for i in range(1, 4):
        current_lst = lt.getElement(lst, i)
        table.add_row([current_lst['value']['popularity'], current_lst['value']['duration_ms'], current_lst['value']['name'], current_lst['value']['disc_number'],current_lst['value']['track_number'],current_lst['value']['album_id'],current_lst['value']['artists_id'],current_lst['value']['href'],current_lst['value']['lyrics'][0:10]])
   
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
   
    for _ in range(size - 2, size + 1):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst['value']['popularity'], current_lst['value']['duration_ms'], current_lst['value']['name'], current_lst['value']['disc_number'],current_lst['value']['track_number'],current_lst['value']['album_id'],current_lst['value']['artists_id'],current_lst['value']['href'],current_lst['value']['lyrics'][0:10]])
   
    return table.get_string()


def printRequerimiento4(lst, number_of_tracks, number_of_albums, artista, mercado):
    country_name = pycountry.countries.get(alpha_2=mercado)
    print("========= Req No. 4 Inputs =========")
    print(f"'{artista}' Discrography metrics in {country_name} Code: {mercado}")
    print()
    print("========= Req No. 4 Answer =========")
    print(f"'{artista}' available discography in {country_name} ({mercado})")
    print(f"Unique available Albums: {number_of_albums}")
    print(f"Unique available Albums: {number_of_tracks}")
    print()
    print(f"The first and last 3 tracks in the range are...")
    table = PrettyTable()
    table.field_names = ["popularity", "duration_ms", "name", "album_type", "available_markets"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        available_markets = f"{current_lst['available_markets'][0]}, {current_lst['available_markets'][1]}, {current_lst['available_markets'][2]}, ... , {current_lst['available_markets'][-3]}, {current_lst['available_markets'][-2]}, {current_lst['available_markets'][-1]}"
        table.add_row([current_lst["popularity"], current_lst["duration_ms"], current_lst["name"], controller.albumID_to_albumType(catalog, current_lst["album_id"]), available_markets])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(number_of_tracks - 2, number_of_tracks + 1):
        current_lst = lt.getElement(lst, _)
        available_markets = f"{current_lst['available_markets'][0]}, {current_lst['available_markets'][1]}, {current_lst['available_markets'][2]}, ... , {current_lst['available_markets'][-3]}, {current_lst['available_markets'][-2]}, {current_lst['available_markets'][-1]}"
        table.add_row([current_lst["popularity"], current_lst["duration_ms"], current_lst["name"], controller.albumID_to_albumType(catalog, current_lst["album_id"]), available_markets])

    return table.get_string()

def printRequerimiento5(albums_artista, numberItems_AlbumsArtista, artista, compilations, singles, discography, firstAndLastThree_TrackId, firstAndLastThree_AlbumName):
    print("========= Req No. 5 Inputs =========")
    print(f"Discography metrics from {artista}")
    print()
    print("========= Req No. 5 Answer =========")
    print(f"Number of 'compilations': {compilations}")
    print(f"Number of 'singles': {singles}")
    print(f"Number of 'Discography': {discography}")
    print()
    print("+++ Albums Details +++")
    print("The first and last 3 tracks in the range are...")
    table = PrettyTable()
    table.field_names = ["release_date", "album_name", "total_tracks", "album_type", "artist_album_name", "external_urls"]
    for _ in range(1, 4):
        current_lst = lt.getElement(albums_artista, _)
        table.add_row([current_lst["release_date"], current_lst["name"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"]])

    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])

    for _ in range(numberItems_AlbumsArtista - 2, numberItems_AlbumsArtista + 1):
        current_lst = lt.getElement(albums_artista, _)
        table.add_row([current_lst["release_date"], current_lst["name"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"]])
    print(table.get_string())

    print()
    print("+++ Tracks Details +++")
    for _ in range(1, 7):
        currentTrack = controller.trackID_to_trackValue(catalog, lt.getElement(firstAndLastThree_TrackId, _))
        print(f"Most popular track in '{lt.getElement(firstAndLastThree_AlbumName, _)}'")
        table = PrettyTable()
        table.field_names = ["popularity", "duration_ms", "name_track", "track_number", "artists_names", "preview_url", "href"]
        if currentTrack == None: 
            table.add_row(["Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found"])
        else:
            artists = ""
            for _ in currentTrack["artists_id"]:
                artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
            table.add_row([currentTrack["popularity"], currentTrack["duration_ms"], currentTrack["name"], currentTrack["track_number"], artists, currentTrack["preview_url"], currentTrack["href"]])
        print(table.get_string())
    

def printCargaDatos(sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks):
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"artists ID count: {sizeArtists}")
    print(f"albums ID count: {sizeAlbums}")
    print(f"tracks ID count: {sizeTracks}")
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print()
    print("The first 3 and last 3 artists in the range are...")
    table = PrettyTable()
    table.field_names = ["name", "artist_popularity", "followers", "relevant_track_name", "genres"]
    for _ in range(1, 4):
        current_lst = lt.getElement(FirstThreeArtists, _)
        table.add_row([current_lst["name"], current_lst["artist_popularity"], current_lst["followers"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(3 - 2, 3 + 1):
        current_lst = lt.getElement(LastThreeArtists, _)
        table.add_row([current_lst["name"], current_lst["artist_popularity"], current_lst["followers"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])
    print(table.get_string())

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
        delta_time, delta_memory, sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks = controller.loadData(catalog)
        printCargaDatos(sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks)
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

    elif int(inputs[0]) == 4:
        popularity = int(input("Ingrese la popularidad que desea consultar (0-100):"))
        tracks, lstsize = controller.requerimiento3(catalog, popularity)
        #print(lt.firstElement(tracks))
        print(printRequerimiento3(tracks, lstsize, popularity))
        #print(lt.lastElement(tracks))
        #print(lstsize)
        
    elif int(inputs[0]) == 5:
        artista = input("Introduzca el artista que desea consultar: ")
        mercado = input("Introduzca el mercado que desea consultar: ")
        lst_canciones, number_of_tracks, number_of_albums = controller.requerimiento4(catalog, artista, mercado)
        #print(lt.firstElement(canciones))
        print(printRequerimiento4(lst_canciones, number_of_tracks, number_of_albums, artista, mercado))

    elif int(inputs[0]) == 6:
        artista = input("Introduzca el artista que desea consultar: ")
        albums_artista, numberItems_AlbumsArtista, firstAndLastThree_TrackId, firstAndLastThree_AlbumName, album_sencillo, album_recopilacion, album_album = controller.requerimiento5(catalog, artista)
        #print(album_recopilacion)
        #print(album_sencillo)
        #print(album_album)
        # Falta debug sorting
        print(printRequerimiento5(albums_artista, numberItems_AlbumsArtista, artista, album_recopilacion, album_sencillo, album_album, firstAndLastThree_TrackId, firstAndLastThree_AlbumName))

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
"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from genericpath import exists
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime
import csv
csv.field_size_limit(2147483647)
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort

# =======================
# Construccion de modelos
# =======================

def newCatalog():
    """
    comment
    """
    catalog = {
        'albums_id': None,
        'artists_id': None,
        'tracks_id': None,
        'artistsName_id': None,
        'anio_albumID': None,
        'artistPopularity_artistID': None,
        'canciones_por_artistas': None,
        'albumes_por_artistas': None}

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['albums_id'] = mp.newMap(76000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=None)

    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['artists_id'] = mp.newMap(57000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)

    
    catalog['artistsName_id'] = mp.newMap(56000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)


    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['tracks_id'] = mp.newMap(102000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)
    

    catalog['anio_albumID'] = mp.newMap(100,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)
    
    catalog['artistPopularity_artistID'] = mp.newMap(100,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)

    catalog['canciones_por_artistas'] = mp.newMap(57000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)
    
    catalog['albumes_por_artistas'] = mp.newMap(40000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=None)


    return catalog




# ==============================================
# Funciones para agregar informacion al catalogo
# ==============================================

    # ========================
    # Carga General Album
    # ========================
def cargaAlbum(catalog, album):
    album['total_tracks'] = float(album['total_tracks'])
    album['available_markets'] = list((album['available_markets'].replace("[", "").replace("]", "").replace("'", "").replace('"', "").replace(" ", "")).split(","))
    album['release_date'] = datetime.datetime.strptime(album['release_date'], "%Y-%m-%d") if (len(album['release_date']) == 10) else (datetime.datetime.strptime(album['release_date'][:4] + "19" + album['release_date'][-2:], "%b-%Y") if (len(album['release_date']) == 6) else (datetime.datetime.strptime(album['release_date'], '%Y')))
    add_albumsID_albumsNames(catalog, album)
    carga_requerimiento1(catalog, album)
    albumes_por_artistas(catalog, album)
    

    # ========================
    # Carga General Artists
    # ========================
def cargaArtists(catalog, artist):
    artist['artist_popularity'] = float(artist['artist_popularity'])
    artist['genres'] = (artist['genres'].replace("[", "").replace("]", "").replace("'", "")).split(",")
    artist['followers'] = float(artist['followers'])
    add_artistsID_artistsNames(catalog, artist)
    carga_requerimiento2(catalog, artist) 
    add_artistsName_id(catalog, artist)


    # ========================
    # Carga General Tracks
    # ========================
def cargaTracks(catalog, track):
    track['artists_id'] = (track['artists_id'].replace("[", "").replace("]", "").replace("'", "").replace(" ", "")).split(",")
    track['popularity'] = float(track['popularity'])
    track['liveness'] = int(float(track['liveness']))
    track['tempo'] = float(track['tempo'])
    track['duration_ms'] = float(track['duration_ms'])
    track['available_markets'] = list((track['available_markets'].replace("[", "").replace("]", "").replace("'", "").replace('"', "")).replace(" ", "").split(","))
    track['disc_number'] = float(track['disc_number'])
    add_tracksID_tracksNames(catalog, track)
    canciones_por_artistas(catalog, track)




# ========================
# Funciones aniadir datos
# ========================

def add_albumsID_albumsNames(catalog, album):
    mp.put(catalog['albums_id'], album['id'], album)


def add_artistsID_artistsNames(catalog, artist):
    mp.put(catalog['artists_id'], artist['id'], artist)


def add_tracksID_tracksNames(catalog, track):
    mp.put(catalog['tracks_id'], track['id'], track)


def add_artistsName_id(catalog, artist):
    mp.put(catalog['artistsName_id'], artist['name'], artist["id"])




# ========================
# Funciones requerimientos
# ========================

    # =========================
    # Funciones Requerimiento 1
    # =========================
def carga_requerimiento1(catalog, album):
    anio_albumID = catalog['anio_albumID']
    year = album['release_date'].year
    existYear = mp.contains(anio_albumID, year)

    if existYear:
        entry = mp.get(anio_albumID, year)
        lst = me.getValue(entry)

    else:
        lst = lt.newList(datastructure='ARRAY_LIST')
        mp.put(anio_albumID, year, lst)

    lt.addLast(lst, album['id'])

def requerimiento1(catalog, year):
    mapa = catalog['model']['anio_albumID']
    mapa_albumes = catalog['model']['albums_id']
    lst_albumsID = me.getValue(mp.get(mapa, year))
    albumsLST = lt.newList(datastructure='ARRAY_LIST')
    
    for album_id in lt.iterator(lst_albumsID):
        album = mp.get(mapa_albumes, album_id)
        lt.addLast(albumsLST, album)

    albumsLST = shellsort.sort(albumsLST, cmpAlbumsName)
    cantidad_albumes = lt.size(albumsLST)
    return albumsLST, cantidad_albumes


    # =========================
    # Funciones Requerimiento 2
    # =========================

def carga_requerimiento2(catalog, artist):
    artistPopularity_artistID = catalog['artistPopularity_artistID']
    popularity = artist['artist_popularity']
    existPopularity = mp.contains(artistPopularity_artistID, popularity)

    if existPopularity:
        entry = mp.get(artistPopularity_artistID, popularity)
        lst = me.getValue(entry)

    else:
        lst = lt.newList(datastructure='ARRAY_LIST')
        mp.put(artistPopularity_artistID, popularity, lst)

    lt.addLast(lst, artist['id'])

def requerimiento2(catalog, artist):
    mapa = catalog['model']['artistPopularity_artistID']
    mapa_artists = catalog['model']['artists_id']
    lst_artistID = me.getValue(mp.get(mapa, artist))
    artistLST = lt.newList(datastructure='ARRAY_LIST')
    for artist_id in lt.iterator(lst_artistID):
        artist = me.getValue(mp.get(mapa_artists, artist_id))
        lt.addLast(artistLST, artist)
    artistLST = shellsort.sort(artistLST, cmpArtistPopularity)
    return artistLST, lt.size(artistLST)


    # =========================
    # Funciones Requerimiento 3
    # =========================

def carga_requerimiento3(catalog, track):
    trackPopularity_trackID = catalog['trackPopularity_trackID']
    popularity = track['popularity']
    exist = mp.contains(trackPopularity_trackID,popularity)

    if exist:
        entry = mp.get(trackPopularity_trackID, popularity)
        lst = me.getValue(entry)
    else:
        lst = lt.newList(datastructure='ARRAY_LIST')
        mp.put(trackPopularity_trackID, popularity, lst)
    lt.addLast(lst, track['id'])

def requerimiento3(catalog, track):
    mapa = catalog['model']['trackPopularity_trackID']
    mapa_canciones = catalog['model']['tracks_id']
    lst_trackID = mp.get(mapa, track)['value']
    trackLST = lt.newList(datastructure='ARRAY_LIST')
    for track_id in lt.iterator(lst_trackID):
        track = mp.get(mapa_canciones, track_id)
        lt.addLast(trackLST, track)
    trackLST = shellsort.sort(trackLST, cmpTrackByDuration)
    numero_canciones = lt.size(trackLST)
    return trackLST, numero_canciones

    # =========================
    # Funciones Requerimiento 4
    # =========================
def canciones_por_artistas(catalog, track):
    canciones_por_artistas = catalog['canciones_por_artistas']
    for artista in track['artists_id']:
        existe = mp.contains(canciones_por_artistas, artista)
        if existe == True:
            entry = mp.get(canciones_por_artistas, artista)
            lst = me.getValue(entry)
        else:
            lst = lt.newList(datastructure='ARRAY_LIST')
            mp.put(canciones_por_artistas, artista, lst)
        lt.addLast(lst, track['id'])


def cancionesArtistas_filtradasMercado(catalog, artista, mercado):
    canciones_por_artistas = catalog['model']['canciones_por_artistas']
    artistID = ArtistName_to_artistValue(catalog, artista)['id']
    tracks_id = catalog['model']['tracks_id']
    cancionesArtista = me.getValue(mp.get(canciones_por_artistas, artistID))
    lst = lt.newList(datastructure='ARRAY_LIST')
    for cancion_id in lt.iterator(cancionesArtista):
        cancion = me.getValue(mp.get(tracks_id, cancion_id))
        mercados = cancion['available_markets']
        if mercado in mercados:
            lt.addLast(lst, cancion)
    return lst

def requerimiento4(catalog, artista, mercado):
    canciones = cancionesArtistas_filtradasMercado(catalog, artista, mercado)
    canciones = shellsort.sort(canciones, cmpRequerimiento4)
    return canciones
    

    # =========================
    # Funciones Requerimiento 5
    # =========================

def albumes_por_artistas(catalogo, album):
    albumes_por_artistas = catalogo['albumes_por_artistas']
    artista = album['artist_id']
    existe = mp.contains(albumes_por_artistas, artista)
    if existe == True:
        entry = mp.get(albumes_por_artistas, artista)
        lst = me.getValue(entry)
    else:
        lst = lt.newList(datastructure='ARRAY_LIST')
        mp.put(albumes_por_artistas, artista, lst)
    lt.addLast(lst, album)

def listaAlbums_cancionesPopulares(catalogo, lista_albumes):
    lst = lt.newList(datastructure='ARRAY_LIST')
    for album in lt.iterator(lista_albumes):
        track = album["track_id"]
        lt.addLast(lst, trackID_to_trackValue(catalogo, track))
    lst = shellsort.sort(lst, cmpCanciones)
    return lst

def requerimiento5(catalogo, artista):
    albumes_por_artistas = catalogo['model']['albumes_por_artistas']
    artistID = ArtistName_to_artistValue(catalogo, artista)['id']
    albums_artista = me.getValue(mp.get(albumes_por_artistas, artistID))
    album_sencillo = 0
    album_recopilacion = 0
    album_album = 0
    for album in lt.iterator(albums_artista):
        if album["album_type"] == "single":
            album_sencillo += 1
        elif album["album_type"] == "compilation":
            album_recopilacion += 1
        else:
            album_album += 1
    listaCancionesPopulares = listaAlbums_cancionesPopulares(catalogo, albums_artista)
    return albums_artista, listaCancionesPopulares, album_sencillo, album_recopilacion, album_album



    
# ================================
# Funciones para creacion de datos
# ================================



# =====================
# Funciones de consulta
# =====================

def artistID_to_artistValue(catalog, artistID):
    return me.getValue(mp.get(catalog['model']['artists_id'], artistID))


def ArtistName_to_artistValue(catalog, artistName):
    mapa = catalog['model']['artistsName_id']
    artistID = me.getValue(mp.get(mapa, artistName))
    return me.getValue(mp.get(catalog['model']['artists_id'], artistID))


def trackID_to_trackValue(catalog, trackID):
    try:
        return me.getValue(mp.get(catalog['model']['tracks_id'], trackID))
    except:
        print(f"No se encontro valor {trackID}")




# ================================================================
# Funciones utilizadas para comparar elementos dentro de una lista
# ================================================================

def cmpAlbumsName(album1, album2):
    return album1["name"] > album2["name"]

def cmpArtistPopularity(artist1, artist2):
    if artist1["followers"] == artist2["followers"]:
        return artist1["name"] > artist2["name"]
    else:
        return artist1["followers"] > artist2["followers"]

def cmpTrackByDuration(track1, track2):
    if track1['value']['duration_ms'] == track2['value']['duration_ms']:
        return track1['value']['name'] > track2['value']['name']
    else:
        return track1['value']['duration_ms'] > track2['value']['duration_ms']

def cmpRequerimiento4(track1, track2):
    # error
    if track1['popularity'] != track2['popularity']:
        return track1['popularity'] > track2['popularity']
    elif track1['duration_ms'] != track2['duration_ms']:
        return track1['duration_ms'] > track2['duration_ms']
    else:
        return track1['name'] > track2['name']

def cmpCanciones(track1, track2):
    #revisar los nones que aparecen
    if track1 == None or track2 == None:
        return
    elif track1['popularity'] != track2['popularity']:
        return track1['popularity'] > track2['popularity']
    elif track1['duration_ms'] != track2['duration_ms']:
        return track1['duration_ms'] > track2['duration_ms']
    else:
        return track1['name'] > track2['name']

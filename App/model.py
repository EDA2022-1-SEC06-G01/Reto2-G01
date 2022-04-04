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
        'anio_albumID': None,
        'artistPopularity_artistID': None,
        'nomArtist_artistID': None}

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['albums_id'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   comparefunction=None)

    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['artists_id'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=4,
                                 comparefunction=None)

    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['tracks_id'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=4,
                                 comparefunction=None)
    

    catalog['anio_albumID'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=4,
                                 comparefunction=None)
    
    catalog['artistPopularity_artistID'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=4,
                                 comparefunction=None)


    catalog['nomArtist_artistID'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=4,
                                 comparefunction=None)

    return catalog




# ==============================================
# Funciones para agregar informacion al catalogo
# ==============================================

# Carga general albums
def cargaAlbum(catalog, album):
    album['total_tracks'] = float(album['total_tracks'])
    album['available_markets'] = (album['available_markets'].replace("[", "").replace("]", "").replace("'", "").replace('"', "")).split(",")
    album['release_date'] = datetime.datetime.strptime(album['release_date'], "%Y-%m-%d") if (len(album['release_date']) == 10) else (datetime.datetime.strptime(album['release_date'][:4] + "19" + album['release_date'][-2:], "%b-%Y") if (len(album['release_date']) == 6) else (datetime.datetime.strptime(album['release_date'], '%Y')))
    add_albumsID_albumsNames(catalog, album)
    carga_requerimiento1(catalog, album)
    


# Carga general artists
def cargaArtists(catalog, artist):
    artist['artist_popularity'] = float(artist['artist_popularity'])
    artist['genres'] = (artist['genres'].replace("[", "").replace("]", "").replace("'", "")).split(",")
    artist['followers'] = float(artist['followers'])
    add_artistsID_artistsNames(catalog, artist)
    carga_requerimiento2(catalog, artist)
    carga_requerimiento4(catalog, artist)


# Carga general tracks
def cargaTracks(catalog, track):
    track['artists_id'] = (track['artists_id'].replace("[", "").replace("]", "").replace("'", "").replace(" ", "")).split(",")
    track['popularity'] = float(track['popularity'])
    track['liveness'] = float(track['liveness'])
    track['tempo'] = float(track['tempo'])
    track['duration_ms'] = float(track['duration_ms'])
    track['available_markets'] = (track['available_markets'].replace("[", "").replace("]", "").replace("'", "").replace('"', "")).split(",")
    track['disc_number'] = float(track['disc_number'])
    add_tracksID_tracksNames(catalog, track)


def add_albumsID_albumsNames(catalog, album):
    mp.put(catalog['albums_id'], album['id'], album)


def add_artistsID_artistsNames(catalog, artist):
    mp.put(catalog['artists_id'], artist['id'], artist)


def add_tracksID_tracksNames(catalog, track):
    mp.put(catalog['tracks_id'], track['id'], track)


def carga_requerimiento1(catalog, album):
    anio_albumID = catalog['anio_albumID']
    year = album['release_date'].year
    existYear = mp.contains(anio_albumID, year)

    if existYear:
        entry = mp.get(anio_albumID, year)
        lst = me.getValue(entry)

    else:
        lst = newList()
        mp.put(anio_albumID, year, lst)

    lt.addLast(lst, album['id'])


def carga_requerimiento2(catalog, artist):
    artistPopularity_artistID = catalog['artistPopularity_artistID']
    popularity = artist['artist_popularity']
    existPopularity = mp.contains(artistPopularity_artistID, popularity)

    if existPopularity:
        entry = mp.get(artistPopularity_artistID, popularity)
        lst = me.getValue(entry)

    else:
        lst = newList()
        mp.put(artistPopularity_artistID, popularity, lst)

    lt.addLast(lst, artist['id'])


def carga_requerimiento4(catalog, artist):
    nomArtist_artistID = catalog['nomArtist_artistID']
    mp.put(nomArtist_artistID, artist['name'], artist['id'])
    # revisar que puede que el nombre de los artistas se repita




# ================================
# Funciones para creacion de datos
# ================================

def newList():
    return lt.newList(datastructure='ARRAY_LIST')

# =====================
# Funciones de consulta
# =====================

def map_size(mapa):
    return mp.size(mapa)


def lst_size(lst):
    return lt.size(lst)

def lst_addLast(lst, value):
    return lt.addLast(lst, value)

def lst_iterator(lst):
    lt.iterator(lst)


def get_mapa(mapa, llave):
    return mp.get(mapa, llave)




# ================================================================
# Funciones utilizadas para comparar elementos dentro de una lista
# ================================================================

def cmpAlbumsName(album1, album2):
    return album1['value']["name"] > album2['value']["name"]

def cmpArtistPopularity(artist1, artist2):
    if artist1['value']["followers"] == artist2['value']["followers"]:
        return artist1['value']["name"] > artist2['value']["name"]
    else:
        return artist1['value']["followers"] > artist2['value']["followers"]

# =========================
# Funciones de ordenamiento
# =========================

def ordenamientoSelection(lst, cmpfunction):
    return selectionsort.sort(lst, cmpfunction)
    
def ordenamientoInsetion(lst, cmpfunction):
    return insertionsort.sort(lst, cmpfunction)

def ordenamientoShell(lst, cmpfunction):
    return shellsort.sort(lst, cmpfunction)

def ordenamientoMerge(lst, cmpfunction):
    return mergesort.sort(lst, cmpfunction)

def ordenamientoQuick(lst, cmpfunction):
    return quicksort.sort(lst, cmpfunction)
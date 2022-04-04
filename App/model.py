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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime
import csv
csv.field_size_limit(2147483647)


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
        'tracks_id': None}

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


# Carga general artists
def cargaArtists(catalog, artist):
    artist['artist_popularity'] = float(artist['artist_popularity'])
    artist['genres'] = (artist['genres'].replace("[", "").replace("]", "").replace("'", "")).split(",")
    artist['followers'] = float(artist['followers'])
    add_artistsID_artistsNames(catalog, artist)


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




# ================================
# Funciones para creacion de datos
# ================================

# =====================
# Funciones de consulta
# =====================

# ================================================================
# Funciones utilizadas para comparar elementos dentro de una lista
# ================================================================

# =========================
# Funciones de ordenamiento
# =========================

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

def add_albumsID_albumsNames(catalog, album):
    mp.put(catalog['albums_id'], album['id'], album['name'])


def add_artistsID_artistsNames(catalog, album):
    mp.put(catalog['artists_id'], album['id'], album['name'])


def add_tracksID_tracksNames(catalog, album):
    mp.put(catalog['tracks_id'], album['id'], album['name'])




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

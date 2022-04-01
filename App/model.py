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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'datos': None}
    catalog['datos'] = mp.newMap(70, maptype='CHAINING', loadfactor=4, comparefunction=compareFunction)

    return catalog

def compareFunction(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def add_artist(catalog, artist):
    artist["genres"] = list(artist["genres"].split(","))
    for _ in range (0, len(artist["genres"])):
        artist['genres'][_] = artist['genres'][_].replace('[', '').replace(']', '').replace("'", '').replace(' ', '')

    for _ in artist["genres"]:
        exists = mp.contains(catalog['model']["datos"], _)
        if exists: 
            entry = mp.get(catalog['model']["datos"], _)
            x = me.getValue(entry)
        else:
            x = new_artist_genre(_)
            mp.put(catalog['model']["datos"], _, x)
        lt.addLast(x["artists"], artist)


def new_artist_genre(artists_genre):
    diccionario = {"genero": "", "artists": None}
    diccionario["genero"] = artists_genre
    diccionario["artists"] = lt.newList(datastructure='ARRAY_LIST')
    return diccionario
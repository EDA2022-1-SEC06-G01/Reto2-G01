﻿"""
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
 """

import config as cf
import model
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


def loadData(ctrlr):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # TODO: modificaciones para medir el tiempo y memoria
    # inicializa el proceso para medir memoria
    tracemalloc.start()

    # toma de tiempo y memoria al inicio del proceso
    start_time = getTime()
    start_memory = getMemory()

    load_data(ctrlr)

    # toma de tiempo y memoria al final del proceso
    stop_memory = getMemory()
    stop_time = getTime()
    # finaliza el proceso para medir memoria
    tracemalloc.stop()

    # calculando la diferencia de tiempo y memoria
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)

    return delta_time, delta_memory


def load_data(catalog):
    artistsfile = r"C:\Users\josed\Desktop\Reto2EDA\Reto2-G01\Data\spotify-artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for _ in input_file:
        model.add_artist(catalog, _)
    return catalog['model']["datos"]





# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

'''
Project scenario: Obtener los datos de quienes son los futbolistas que más goles han echo en la historia del futbol. ordenados de mayor a menor

pasos a seguir: 
-definir una funcion para extraer
-definir una funcion para CARGAR la data a una base de datos
- definir una función para cargar los datos a un archivo cvs
-crear archivo txt registrando cada proceso


URL: https://es.wikipedia.org/wiki/Goleador_(fútbol)

'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import sqlite3
import logging

url = "https://es.wikipedia.org/wiki/Goleador_(fútbol)"
table_attribs= ['Player', 'Goals']
database_name = 'Ammount_Goals.db'
cvs_path = '/Players_Goals.cvs'
table_name = 'Players_Goals'


def extract(url, table_attribs): #nombre de la función, parametros (url, nombre de las tablas)
    web = requests.get(url).text
    data = BeautifulSoup(web,'html.parser')


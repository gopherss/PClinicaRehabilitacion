from psycopg2 import connect
from os import environ

cadena_conexion = connect(
    database=environ.get('pgdatabase'),
    user=environ.get('pguser'),
    password=environ.get('pgpassword'),
    host=environ.get('pghost'),
    port=environ.get('pgport')
)


def obtener_datos(consulta: str, valores: tuple):
    with cadena_conexion:
        with cadena_conexion.cursor() as mi_cursor:
            mi_cursor.execute(consulta, valores)
            datos = mi_cursor.fetchall()
            return datos


def crud_datos(consulta: str, valores: tuple):
    with cadena_conexion:
        with cadena_conexion.cursor() as mi_cursor:
            mi_cursor.execute(consulta, valores)



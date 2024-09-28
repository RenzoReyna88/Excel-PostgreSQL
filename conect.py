from config import HOST, USER, PASSWORD, NAME
import psycopg2
from psycopg2 import DatabaseError


def connect_to_db():
    try:
        conexion= psycopg2.connect(
                                    host= f'{HOST}', 
                                    user= f'{USER}', 
                                    password= f'{PASSWORD}',
                                    dbname= f'{NAME}',
                                    port= 5432
                                    )    
        if conexion is not None:

            print("Conexión Exitosa")
            return conexion
               
    except DatabaseError as ex:
            
            print("Error al realizar la conexión:", ex)
            return None
    
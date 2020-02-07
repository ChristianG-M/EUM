#!/usr/bin/python3
import psycopg2
import json

# Postgres
PSQL_HOST = "127.0.0.1"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "root"
PSQL_DB   = "CajerOk"

try:
	connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
	conn = psycopg2.connect(connstr)
	cur = conn.cursor()
	sqlquery = "INSERT INTO products (DATA) VALUES (null,'{"Name": "Laptop","Price": "500.00"}');"
	cur.execute(sqlquery)
	cur.commit()
	cur.close()
	conn.close()
except:
	print("Error de base de datos")




import psycopg2
from psycopg2.extras import Json
import json


def insert_into_table(data):
    # preparing geometry json data for insertion
    for item in data:
        item['geom'] = Json(item['geometry'])

    with psycopg2.connect(database='testdb', user='postgres', password='password', host='localhost') as conn:
        with conn.cursor() as cursor:
            query = """
                INSERT into 
                    data_load 
                    (iso_code, l_postcode, r_postcode, link_id, geom) 
                VALUES 
                    (%(iso_code)s, %(l_postcode)s, %(r_postcode)s, %(link_id)s, st_geomfromgeojson(%(geom)s));
            """
            cursor.executemany(query, data)

        conn.commit()


for di in user_data:
    new_dict[di['idTarifa']]={}
    for k in di.keys():
        if k =='idTarifa': continue
        new_dict[di['idTarifa']][k]=di[k]
print(categoria)





#!/usr/bin/python3
import psycopg2
import json
import psycopg2.extras
import sys

# Postgres
PSQL_HOST = "127.0.0.1"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "root"
PSQL_DB   = "CajerOk"


with open('config.json', 'r') as f:
    data = json.load(f)

#print(data)

connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
conn = psycopg2.connect(connstr)
cur = conn.cursor()
q = "INSERT INTO public.\"TARIFA\" \
     VALUES(%(idTarifa)s, %(plaza)s, %(fec_ini)s, %(hor_ini)s, %(hor_fin)s, %(dia_sem)s, %(des_tar)s, %(costo)s, %(int_1)s, %(int_2)s, %(estado)s, %(prioridad)s, %(descuento)s)"
cur.execute(q, data)
con.commit()
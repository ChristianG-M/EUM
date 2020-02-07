#!/usr/bin/python3
import psycopg2
import json
import psycopg2.extras
import sys
from time import sleep

# Postgres
PSQL_HOST = "127.0.0.1"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "root"
PSQL_DB   = "CajerOk"

class insert():
	def __init__(self):
		pass


	def conectarDB(self):
		try:
			connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
			conn = psycopg2.connect(connstr)
			return conn
		except Exception as error:
			print ("Exception:", error)

	
	def dropTable(self, conn):
		try:
			cur = conn.cursor()
			drop = "TRUNCATE \"TARIFA\" CASCADE;"
			cur.execute(drop)
			comit = conn.commit()
			print("Tabla Truncada")
			sleep(5)
		except Exception as error:
			print ("Exception:", error)


	def openJson(self):
		try:
			with open('config.json', 'r') as f:
				data = json.loads(f.read())
				return data
		except Exception as error:
			print ("Exception:", error)


	def insertDB(self, conn, data):
		try:
			cur = conn.cursor()
			for value in data['TARIFAS']:
				q = "INSERT INTO public.\"TARIFA\" VALUES(%(idTarifa)s, %(plaza)s, %(fec_ini)s, %(fec_fin)s, %(hor_ini)s, %(hor_fin)s, %(dia_sem)s, %(des_tar)s, %(costo)s, %(int_1)s, %(int_2)s, %(estado)s, %(prioridad)s, %(descuento)s)"
				cur.execute(q, value)
				conn.commit()
				print("Insert realizado")
		except Exception as error:
			print ("Exception:", error)


	def closeDB(self, conn):
		try:
			cur = conn.cursor()
			cur.close()
			conn.close()
		except Exception as error:
			print ("Exception:", error)


	def insertProcess(self):
		try:
			conector = self.conectarDB()
			self.dropTable(conector)
			datos = self.openJson()
			self.insertDB(conector, datos)
			self.closeDB(conector)
		except Exception as error:
			print ("Exception:", error)		


def main():
	try:
		newInsert = insert()
		newInsert.insertProcess()
	except Exception as error:
		print ("Exception:", error)
	

if __name__ == "__main__":
	main()
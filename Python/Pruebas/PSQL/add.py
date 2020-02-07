#!/usr/bin/python3
import psycopg2
import json

with open('final.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['TARIFAS'] 
  
    # python object to be appended 
    y = {"idTarifa":2,
        "plaza":1,
        "fec_ini":None,
        "fec_fin":"null",
        "hor_ini":"null",
        "hor_fin":"null",
        "dia_sem":"tarifa de 1 a 2 horas",
        "des_tar":"5",
        "costo":1,
        "int_1":2,
        "int_2":1,
        "estado":1,
        "prioridad":1,
        "descuento":"null"
        }   
    print(y)     
  
    # appending data to emp_details  
    temp.append(y)

with open('final.json','w') as f: 
	json.dump(data, f, indent=4) 
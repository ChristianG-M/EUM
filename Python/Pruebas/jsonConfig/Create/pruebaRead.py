#!/usr/bin/python3
import json
import re

contents = []
categoria = []
campo = []
final = []
final2 = []
campoFinal = []
try:
	with open("./config.json", 'r+') as configuracion:
		contents = json.load(configuracion)
except Exception as e:
	print(e)

print(contents['PATHS'])


for key in contents.keys():
	categoria += [key]

for (k, v) in contents.items():
   campo += [v]


for i in range( 0, len(campo) ):
	final += [re.split(r'\,+', str(campo[i]))]

for x in range(0, len(final)):
	for y in range(0, len(final[x])):
		final2 += [re.split(r'\'+', str(final[x][y]))]

for a in range(0, len(final2)):
	for b in range(0, len(final2[a])):
		if( '{' in final2[a][b] or '}' in final2[a][b] or ':' in final2[a][b] or not final2[a][b] or "\\t" in final2[a][b] or "/" in final2[a][b] or " " in final2[a][b] or final2[a][b].isdigit() or b > 2):
			pass
		else:
			#print("Valor: ", final2[a][1])
			campoFinal += [ final2[a][1] ]

#print(categoria)
#print(campo[0])
#print(campoFinal)

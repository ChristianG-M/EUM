#!/usr/bin/python3
import re

#phone = "{'id': 1, 'last_update': '2020-01-29', 'status': True, 'user': 'Christian'}"

final = re.split(r'\,+', "{'id': 1, 'last_update': '2020-01-29', 'status': True, 'user': 'Christian'}")
print(final)
print(final[0])
print(final[1])
print(final[2])
print(final[3])

final2 = re.split(r'\'+', "{'id': 1")
final3 = re.split(r'\'+', "'last_update': '2020-01-29'")
final4 = re.split(r'\'+', "'user': 'Christian'}")


print(final2[1])
print(final3[1])
print(final4[1])
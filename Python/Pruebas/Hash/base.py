import base64
encoded = base64.b64encode(b'M,1050,1,22-01-2020,01:22:53.')
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)
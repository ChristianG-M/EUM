from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
print(key)
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"M,1105,1,01-02-2020,05:06:56.")
print(encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print(decoded_text)

#M,1105,1,01-02-2020,05:06:56.
#texto_cifrado = SJCL().encrypt("M,1105,1,01-02-2020,05:06:56.".encode("utf-8"), "1234".encode("utf-8"))
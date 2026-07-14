from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
print(password_hash.hash("RM654321"))

#poner en el terminal: python archivos_fastapi/hasher.py
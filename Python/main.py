import math

print("Benvenuto nel mio programma!!!")

nome = input("Inserisci il tuo nome: ")
print(f"Benvenuto {nome}!!")

cognome = input("Inserire cognome: ")
print("cognome inserito")

num = input("Inserire numero di telefono: ")
if num.isdigit() == True: 
    print("Numero di telefono registrato")
else:
    print()

mail = input("Inserire mail: ")
print("mail registrata")

print("___I tuoi dati___")
print(f"Nome: {nome}\nCognome: {cognome}\nNumero di telefono: {num}\nEmail: {mail}")
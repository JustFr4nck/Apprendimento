import math

print("Benvenuto nel mio programma!!!")

nome = input("Inserisci il tuo nome: ")
print(f"Benvenuto {nome}!!")

cognome = input("Inserire cognome: ")
print("cognome inserito")

num = "w"
while num.isdigit() == False or len(num) != 10:
    num = input("Inserire numero di telefono: ")
    if num.isdigit() == True and len(num) == 10: 
        print("Numero di telefono registrato")
    else:
        print("ERRORE: digitare solo numeri nel limite della lunghezza di 10")

mail = input("Inserire mail: ")
print("mail registrata")

print("___I tuoi dati___")
print(f"Nome: {nome}\nCognome: {cognome}\nNumero di telefono: {num}\nEmail: {mail}")
print("___BENVENUTO NEL MIO PROGRAMMA___")

user = input("Inserisci nome utente: ")

if len(user) > 12:
    print("Errore nel programma: Inserire meno di 12 caratteri")
elif user.find(" ") != -1:
    print("Errore nel programma: non puoi inserire gli spazi nel nome utente")
elif user.isalpha() == False:
    print("Errore nel programma: non puoi inserire valori nu  merici")
else:
    print(f"Benvenuto {user}")
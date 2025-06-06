
#___BASI___
#[help(strumento)] serve per vedere tutte le funzioni e i metodi di ciò che viene messo fra parentesi
# [print] per stampare
# [print(f"hello {x}")] la f permette di mettre fra 2 {} una variabile da stampare
# per dichiarare una variabile non serve mettere il tipo di variabile che vai a realizzare basta fare variabile = contenuto(String, Float, Integer, Boolean)
# per le condizioni basta mettere i [:] per iniziare ad inserire le condizioni
# con [print(type(variabile))] si stampa il tipo della variabile
# (TypeCasting) per convertire una variabile ad un altro tipo si usano le funzioni [str(), int(), float(), bool()]
# con [input(string)] puoi richieder l'imput dall'utente su terminale e tra le parentesi puoi mettere una stringa che verrà stampata a schermo
#[pass] place holder

#___Funzioni Matematiche___
# [round(variabile)] si usa per arrotondare un valore
# [abs(variabile)] si usa per modificare una variabile al suo valore assoluto
# [pow(variabile, valore elevato)] si usa per calcolare la potenza di una variabile
# [max(variabile1, variabile2, variabile3)] ricerca della variabile più grande (Se ne possono mettere all'infinito)
# [min(variabile1, variabile2, variabile3)] ricerca della variabile più piccola (Se ne possono mettere all'infinito)

#___ class math___
# [import math] si importa la classe math per delle funzioni specifiche
# [math.pi] pi greco
# [math.e] esponenziale
# [math.sqrt(valori sotto radice)] radice quadrata
# [math.ceil(variabile)] approssima per eccesso
# [math.floor(variabile)] approssima per difetto

#___ Operatori Logici___
# [or] [and] [not]

#___String functions___
# [len(variabile)] si usa per calcolare la lunghezza di una stringa (compresi gli spazi)(restituisce integer)
# [variabile.find(carattere)] si usa per cercare un carattere in una stringa (Restituisce la posizione del primo carattere corrispondente) (puoi cercare anche gli spazi), in caso non trova il carattere restituisce -1 (restituisce integer)
# [variabile.rfind(carattere)] si usa per cercare un carattere in una stringa (Restituisce la posizione dell'ultimo carattere corrispondente) (puoi cercare anche gli spazi), in caso non trova il carattere restituisce -1 (restituisce integer)
# [variabile.capitalize()] rende la prima lettera di una stringa maiuscola
# [variabile.upper()] rende una stringa tutta maiuscola
# [variabile.lower()] rende una stringa tutta minuscola
# [variabile.isdigit()] restituisce [True] se la stringa è composta SOLO da numeri, altrimenti restituisce [False]
# [variabile.isalpha()] restituisce [True] se la stringa è composta SOLO da lettere, altrimenti restituisce [False] (se ci sono spazi restituisce [False])
# [variabile.count("carattere")] conta quanti caratteri del tipo specificato sono presenti nella stringa della variabile (Restituisce Integer)
# [variabile.replace("carattere da sostituire", "carattere che prenderà il suo posto")] con questa funzione vengono sostituiti tutti i caratteri specificati con un altro carattere specificato

#___Indexing___
#[Stringa[posizione]] resituisce il carattere nella posizione fra parentesi
#[Stringa[start : end]] restituisce i caratteri fra la posizione [start] e la posizione [end]
#[Stringa[start : end : step]] restituisce i caratteri ogni valore dello [step]

#___Format Specifiers___
#[print(f"text {variabile :.nf}")] n equivale alla quantità di numeri dopo la virgola da stampare
#[print(f"text {variabile :n}")] n equivale alla quantità di spazi occupati dal  valore stampato (In caso di un numero superiore al numero di cifre del valore vengono aggiunti degli spazi vuoti)
#[print(f"text {variabile :0n}")] n equivale alla quantità di spazi occupati dal  valore stampato (In caso di un numero superiore al numero di cifre del valore vengono aggiunti degli zeri)
#[print(f"text {variabile :>n}")] n equivale alla quantità di spazi occupati dal  valore stampato ed il simbolo giustifica il testo verso destra
#[print(f"text {variabile :<n}")] n equivale alla quantità di spazi occupati dal  valore stampato ed il simbolo giustifica il testo verso sinistra
#[print(f"text {variabile :^n}")] n equivale alla quantità di spazi occupati dal  valore stampato ed il simbolo giustifica il testo al centro


#___loop___
#while loop
#for in loop

#___import time___
# Serve per i metodi per creare timer  
 
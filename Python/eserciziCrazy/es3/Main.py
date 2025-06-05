from Calcoli import Calcoli

class Main:

    num1 = input("Inserisci primo valore: ")

    num2 = input("Inserire secondo valore: ")

    costruct = Calcoli(num1, num2)

    print(f"Addizione: {costruct.add()}")
    print(f"\nSottrazione: {costruct.sub()}")
    print(f"\nMoltiplicazione {costruct.molt()}")
    print(f"\nDivisione {costruct.div()}")
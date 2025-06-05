class gay:

    

    def __init__(self, nome, cognome, eta):

        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def toString(self):

        print(f"Nome: {self.nome} \nCognome: {self.cognome} \nEtà: {self.eta} ")
        











######################################

stampa = gay("Francesco", "Perrotta", 18)

stampa.toString()
class Utilizatori:
    def __init__(self):
        self.listaUtilizatori = []

    def addUtilizator(self,utilizator):
        self.listaUtilizatori.append(utilizator)

    def __str__(self):
        string = ""
        for i in self.listaUtilizatori:
            string = string + i.__str__() + "\n"
        return string

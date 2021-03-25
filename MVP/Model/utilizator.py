from Model.persoana import Persoana

class Utilizator(Persoana):
    def __init__(self, nume, parola, rol, cont):
        super().__init__(nume)
        self.parola = parola
        self.rol = rol
        self.cont = cont

    def __eq__(self, other):
        if(self.nume == other.nume and self.parola == other.parola and self.rol == other.rol and self.cont == other.cont):
            return True
        return False

    def __str__(self):
        return super().__str__() + " " + self.parola + " " + self.rol + " " + self.cont
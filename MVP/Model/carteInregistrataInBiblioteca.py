from Model.cartePublicata import CartePublicata
from json import JSONEncoder

class CarteInregistrataInBiblioteca(CartePublicata, JSONEncoder):
    def __init__(self,titlu, autor, domeniu, editura, anAparitie, disponibilitate, nrInregistrare):
        super().__init__(titlu, autor, domeniu, editura, anAparitie)
        self.disponibilitate = disponibilitate
        self.nrInregistrare = nrInregistrare

    def __eq__(self, other):
        if super().__eq__(other) and self.disponibilitate == other.disponibilitate and self.nrInregistrare == other.nrInregistrare:
            return True
        return False

    def __str__(self):
        return super().__str__() + " " + self.disponibilitate + " " + self.nrInregistrare

    def default(self):
        return self.__dict__
from Model.carte import Carte

class CartePublicata(Carte):
    def __init__(self,titlu, autor, domeniu, editura, anAparitie):
        super().__init__(titlu, autor, domeniu)
        self.editura = editura
        self.anAparitie = anAparitie

    def __eq__(self, other):
        if super().__eq__(other) and self.editura == other.editura and self.anAparitie == other.anAparitie:
            return True
        return False

    def __str__(self):
        return super().__str__() + " " + self.editura + " " + self.anAparitie
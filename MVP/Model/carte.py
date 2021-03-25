class Carte:
    def __init__(self, titlu, autor, domeniu):
        self.titlu = titlu
        self.autor = autor
        self.domeniu = domeniu

    def __eq__(self, other):
        if self.titlu == other.titlu and self.autor == other.autor and self.domeniu == other.domeniu:
            return True
        return False

    def __str__(self):
        return self.titlu + " " + self.autor + " " + self.domeniu
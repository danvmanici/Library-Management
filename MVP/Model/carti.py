from json import JSONEncoder

class Carti(JSONEncoder):
    def __init__(self):
        self.listaCartiInregistrate = []

    def addCarte(self, carte):
        self.listaCartiInregistrate.append(carte)

    def __str__(self):
        string = ""
        for i in self.listaCartiInregistrate:
            string = string + i.__str__() + "\n"
        return string

    def json_encode(self):
        d={}
        for i in self.listaCartiInregistrate:
            d[i.titlu]=i.__dict__
        return d

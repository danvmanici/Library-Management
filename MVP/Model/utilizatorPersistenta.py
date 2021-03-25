from xml.etree import ElementTree as ET
from Model.utilizatori import Utilizatori
from Model.utilizator import Utilizator

class UtilizatorPersistenta:
    def __init__(self, filename):
        self.filename = filename

    def createUtilizator(self, utilizator):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        el = root.makeelement("Utilizator", {})
        root.append(el)
        for key, value in utilizator.__dict__.items():
            sub = root[root.__len__() - 1].makeelement(key, {})
            sub.text = str(value)
            root[root.__len__() - 1].append(sub)
        tree.write(self.filename)

    def readUtilizator(self, rol):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        utilizatori = Utilizatori()
        for child in root:
            utilizator = Utilizator(child[0].text, child[1].text, child[2].text, child[3].text)
            if rol == "bibliotecar" and child[2].text == "bibliotecar":
                utilizatori.addUtilizator(utilizator)
            if rol == "abonat" and child[2].text == "abonat":
                utilizatori.addUtilizator(utilizator)
            if rol == "all":
                utilizatori.addUtilizator(utilizator)
        return utilizatori

    def updateUtilizator(self,utilizatorOld,utilizatorNew):
        if self.deleteUtilizator(utilizatorOld) == True :
            self.createUtilizator(utilizatorNew)
            return True
        return False

    def deleteUtilizator(self, utilizatorRemove):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for child in root:
            utilizator = Utilizator(child[0].text, child[1].text, child[2].text, child[3].text)
            if utilizator == utilizatorRemove:
                root.remove(child)
                tree.write(self.filename)
                return True
        return False

    def checkUtilizator(self, nume, parola):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for child in root:
            if nume == child[0].text and parola == child[1].text:
                return True
        return False

    def findUtilizator(self, nume):
        utilizatori = self.readUtilizator("all")
        for utilizator in utilizatori.listaUtilizatori:
            if utilizator.nume == nume:
                return utilizator

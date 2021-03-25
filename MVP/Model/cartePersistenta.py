import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import csv
import json

from Model.carteInregistrataInBiblioteca import CarteInregistrataInBiblioteca
from Model.carti import Carti
from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt

class CartePersistenta:
    def __init__(self, filename):
        self.filename = filename

    def createCarte(self, carte):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        el = root.makeelement("Carte", {})
        root.append(el)
        for key, value in carte.__dict__.items():
            sub = root[root.__len__() - 1].makeelement(key, {})
            sub.text = str(value)
            root[root.__len__() - 1].append(sub)
        tree.write(self.filename)

    def readCarti(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        carti = Carti()
        for child in root:
            carte = CarteInregistrataInBiblioteca(child[0].text,child[1].text,child[2].text,child[3].text,child[4].text,child[5].text,child[6].text)
            carti.addCarte(carte)
        return carti

    def updateCarte(self, carteOld, carteNew):
        if self.deleteCarte(carteOld) == True :
            self.createCarte(carteNew)
            return True
        return False

    def deleteCarte(self, carteRemove):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for child in root:
            carte = CarteInregistrataInBiblioteca(child[0].text, child[1].text, child[2].text, child[3].text,
                                            child[4].text, child[5].text, child[6].text)
            if carte == carteRemove:
                root.remove(child)
                tree.write(self.filename)
                return True
        return False

    def filterCarti(self, key, value):
        carti = self.readCarti()
        listaCartiFiltrate = Carti()
        for carte in carti.listaCartiInregistrate:
            for i in carte.__dict__.keys():
                if i == key:
                    if value == carte.__dict__[i]:
                        listaCartiFiltrate.addCarte(carte)
        return listaCartiFiltrate

    def borrowCarte(self, carteImprumutata):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for child in root:
            carte = CarteInregistrataInBiblioteca(child[0].text, child[1].text, child[2].text, child[3].text,
                                                  child[4].text, child[5].text, child[6].text)
            if carte == carteImprumutata:
                if child[5].text == "True":
                    child[5].text="False"
                    tree.write(self.filename)
                    return True
        return False

    def returnCarte(self, carteImprumutata):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for child in root:
            carte = CarteInregistrataInBiblioteca(child[0].text, child[1].text, child[2].text, child[3].text,
                                                  child[4].text, child[5].text, child[6].text)
            if carte == carteImprumutata:
                if child[5].text == "False":
                    child[5].text="True"
                    tree.write(self.filename)
                    return True
        return False


    def findCarte(self, titluCarte):
        carti = self.readCarti()
        listaCarti=Carti()
        for carte in carti.listaCartiInregistrate:
            if carte.titlu == titluCarte:
                listaCarti.addCarte(carte)
        return listaCarti

    def viewStatistici(self, stats):
        carti = self.readCarti()
        d = {}
        for carte in carti.listaCartiInregistrate:
            for key, value in carte.__dict__.items():
                if key == stats:
                    if value not in d.keys():
                        d[value] = 1
                    else:
                        d[value] = d[value] + 1
        left=[]
        for i in range(len(d)):
            left.append(i+1)
        tick_label=[]
        for key in d.keys():
            tick_label.append(key)
        plt.bar(left, d.values(), tick_label=tick_label, width=0.8)
        plt.show()

    def csvRaport(self, csvfile):
        with open(csvfile, "w") as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            carte = self.readCarti()
            writer.writerow(carte.listaCartiInregistrate[0].__dict__.keys())
            for carte in carte.listaCartiInregistrate:
                writer.writerow(carte.__dict__.values())

    def jsonRaport(self, jsonfile):
        carti = self.readCarti()

        with open(jsonfile, 'w') as f:
            json.dump(carti.json_encode(), f, indent=2)


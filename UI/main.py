import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton
from PyQt5 import uic
import csv

from Element import Element

def load_elements(file_path): 
    with open(file_path) as file: 
        file_reader = csv.reader(file, delimiter=',') 
        elements = list(file_reader)  
    return elements 

class App(QMainWindow):
    
    def __init__(self):

        super(App, self).__init__()
        uic.loadUi("./test.ui", self)

        self.setFixedSize(1200, 800)

        #frames
        self.frame1 = self.findChild(QFrame, 'konfiguracja_powlokowa') 
        self.frame2 = self.findChild(QFrame, 'mendelew_frame')

        #configuration elements
        self.text_input = self.findChild(QLineEdit, "text_input")
        self.send = self.findChild(QPushButton, "send")
        # self.result = self.findChild(QLabel, "result")
        self.send.clicked.connect(self.generate_configuration)

        #menu elements
        self.mendelewButton = self.findChild(QPushButton, "mendelewButton")
    
        #mendelew elements
        self.CloseMendelew = self.findChild(QPushButton, "CloseMendelew")
        self.CloseMendelew.clicked.connect(self.toggle_frames)

        self.WodorButton = self.findChild(QPushButton, "Wodor")
        self.HelButton = self.findChild(QPushButton, "Hel")
        self.LitButton = self.findChild(QPushButton, "Lit")
        self.BerylButton = self.findChild(QPushButton, "Beryl")
        self.BorButton = self.findChild(QPushButton, "Bor")
        self.WegielButton = self.findChild(QPushButton, "Wegiel")
        self.AzotButton = self.findChild(QPushButton, "Azot")
        self.TlenButton = self.findChild(QPushButton, "Tlen")
        self.FluorButton = self.findChild(QPushButton, "Fluor")
        self.NeonButton = self.findChild(QPushButton, "Neon")
        self.SodButton = self.findChild(QPushButton, "Sod")
        self.MagnezButton = self.findChild(QPushButton, "Magnez")
        self.GlinButton = self.findChild(QPushButton, "Glin")
        self.KrzemButton = self.findChild(QPushButton, "Krzem")
        self.FosforButton = self.findChild(QPushButton, "Fosfor")
        self.SiarkaButton = self.findChild(QPushButton, "Siarka")
        self.ChlorButton = self.findChild(QPushButton, "Chlor")
        self.ArgonButton = self.findChild(QPushButton, "Argon")
        self.PotasButton = self.findChild(QPushButton, "Potas")
        self.WapnButton = self.findChild(QPushButton, "Wapn")
        self.SkandButton = self.findChild(QPushButton, "Skand")
        self.TytanButton = self.findChild(QPushButton, "Tytan")
        self.WanadButton = self.findChild(QPushButton, "Wanad")
        self.ChromButton = self.findChild(QPushButton, "Chrom")
        self.ManganButton = self.findChild(QPushButton, "Mangan")
        self.ZelazoButton = self.findChild(QPushButton, "Zelazo")
        self.KobaltButton = self.findChild(QPushButton, "Cobalt")
        self.NikielButton = self.findChild(QPushButton, "Nikiel")
        self.MiedzButton = self.findChild(QPushButton, "Miedz")
        self.CynkButton = self.findChild(QPushButton, "Cynk")
        self.GalButton = self.findChild(QPushButton, "Gal")
        self.GermanButton = self.findChild(QPushButton, "German")
        self.ArsenButton = self.findChild(QPushButton, "Arsen")
        self.SelenButton = self.findChild(QPushButton, "Selen")
        self.BromButton = self.findChild(QPushButton, "Brom")
        self.KryptonButton = self.findChild(QPushButton, "Krypton")
        self.RubidButton = self.findChild(QPushButton, "Rubid")
        self.StrontButton = self.findChild(QPushButton, "Stront")
        self.CyrkonButton = self.findChild(QPushButton, "Cyrkon")
        self.NiobButton = self.findChild(QPushButton, "Niob")
        self.MolibdenButton = self.findChild(QPushButton, "Molibden")
        self.TechnetButton = self.findChild(QPushButton, "Technet")
        self.RutenButton = self.findChild(QPushButton, "Ruten")
        self.RodButton = self.findChild(QPushButton, "Rod")
        self.PalladButton = self.findChild(QPushButton, "Pallad")
        self.SrebroButton = self.findChild(QPushButton, "Srebro")
        self.KadmButton = self.findChild(QPushButton, "Kadm")
        self.IndButton = self.findChild(QPushButton, "Ind")
        self.CynaButton = self.findChild(QPushButton, "Cyna")
        self.AntymonButton = self.findChild(QPushButton, "Antymon")
        self.TelurButton = self.findChild(QPushButton, "Tellur")
        self.JodButton = self.findChild(QPushButton, "Jod")
        self.KsenonButton = self.findChild(QPushButton, "Xenon")
        self.CezButton = self.findChild(QPushButton, "Cez")
        self.BarButton = self.findChild(QPushButton, "Bar")
        self.HafnButton = self.findChild(QPushButton, "Hafn")
        self.TantalButton = self.findChild(QPushButton, "Tantal")
        self.WolframButton = self.findChild(QPushButton, "Wolfram")
        self.RenButton = self.findChild(QPushButton, "Ren")
        self.OsmButton = self.findChild(QPushButton, "Osm")
        self.IrydButton = self.findChild(QPushButton, "Iryd")
        self.PlatynaButton = self.findChild(QPushButton, "Platyna")
        self.ZlotoButton = self.findChild(QPushButton, "Zloto")
        self.RtecButton = self.findChild(QPushButton, "Rtec")
        self.TalButton = self.findChild(QPushButton, "Tal")
        self.OlowButton = self.findChild(QPushButton, "Olow")
        self.BizmutButton = self.findChild(QPushButton, "Bizmut")
        self.PolonButton = self.findChild(QPushButton, "Polon")
        self.AstatButton = self.findChild(QPushButton, "Astat")
        self.RadonButton = self.findChild(QPushButton, "Radon")
        self.FransButton = self.findChild(QPushButton, "Frans")
        self.RadButton = self.findChild(QPushButton, "Rad")
        self.RutherfordButton = self.findChild(QPushButton, "Rutherford")
        self.DubnButton = self.findChild(QPushButton, "Dubn")
        self.SeaborgButton = self.findChild(QPushButton, "Seaborg")
        self.BohryButton = self.findChild(QPushButton, "Bohr")
        self.HasButton = self.findChild(QPushButton, "Has")
        self.MeitnerButton = self.findChild(QPushButton, "Meitner")
        self.DarmsztadButton = self.findChild(QPushButton, "Darmsztad")
        self.RoentgenButton = self.findChild(QPushButton, "Roentgen")
        self.KopernikButton = self.findChild(QPushButton, "Kopernik")
        self.NihonButton = self.findChild(QPushButton, "Nihon")
        self.FlerowButton = self.findChild(QPushButton, "Flerow")
        self.MoskowButton = self.findChild(QPushButton, "Moskow")
        self.LivermorButton = self.findChild(QPushButton, "Livermor")
        self.TenesButton = self.findChild(QPushButton, "Tenes")
        self.OganessonButton = self.findChild(QPushButton, "Oganeson")

        self.WodorButton.clicked.connect(lambda: self.generatePopUp("Wodor"))
        self.HelButton.clicked.connect(lambda: self.generatePopUp("Hel"))
        self.LitButton.clicked.connect(lambda: self.generatePopUp("Lit"))
        self.BerylButton.clicked.connect(lambda: self.generatePopUp("Beryl"))
        self.BorButton.clicked.connect(lambda: self.generatePopUp("Bor"))
        self.WegielButton.clicked.connect(lambda: self.generatePopUp("Wegiel"))
        self.AzotButton.clicked.connect(lambda: self.generatePopUp("Azot"))
        self.TlenButton.clicked.connect(lambda: self.generatePopUp("Tlen"))
        self.FluorButton.clicked.connect(lambda: self.generatePopUp("Fluor"))
        self.NeonButton.clicked.connect(lambda: self.generatePopUp("Neon"))
        self.SodButton.clicked.connect(lambda: self.generatePopUp("Sod"))
        self.MagnezButton.clicked.connect(lambda: self.generatePopUp("Magnez"))
        self.GlinButton.clicked.connect(lambda: self.generatePopUp("Glin"))
        self.KrzemButton.clicked.connect(lambda: self.generatePopUp("Krzem"))
        self.FosforButton.clicked.connect(lambda: self.generatePopUp("Fosfor"))
        self.SiarkaButton.clicked.connect(lambda: self.generatePopUp("Siarka"))
        self.ChlorButton.clicked.connect(lambda: self.generatePopUp("Chlor"))
        self.ArgonButton.clicked.connect(lambda: self.generatePopUp("Argon"))
        self.PotasButton.clicked.connect(lambda: self.generatePopUp("Potas"))
        self.WapnButton.clicked.connect(lambda: self.generatePopUp("Wapn"))
        self.SkandButton.clicked.connect(lambda: self.generatePopUp("Skand"))
        self.TytanButton.clicked.connect(lambda: self.generatePopUp("Tytan"))
        self.WanadButton.clicked.connect(lambda: self.generatePopUp("Wanad"))
        self.ChromButton.clicked.connect(lambda: self.generatePopUp("Chrom"))
        self.ManganButton.clicked.connect(lambda: self.generatePopUp("Mangan"))
        self.ZelazoButton.clicked.connect(lambda: self.generatePopUp("Zelazo"))
        self.KobaltButton.clicked.connect(lambda: self.generatePopUp("Cobalt"))
        self.NikielButton.clicked.connect(lambda: self.generatePopUp("Nikiel"))
        self.MiedzButton.clicked.connect(lambda: self.generatePopUp("Miedz"))
        self.CynkButton.clicked.connect(lambda: self.generatePopUp("Cynk"))
        self.GalButton.clicked.connect(lambda: self.generatePopUp("Gal"))
        self.GermanButton.clicked.connect(lambda: self.generatePopUp("German"))
        self.ArsenButton.clicked.connect(lambda: self.generatePopUp("Arsen"))
        self.SelenButton.clicked.connect(lambda: self.generatePopUp("Selen"))
        self.BromButton.clicked.connect(lambda: self.generatePopUp("Brom"))
        self.KryptonButton.clicked.connect(lambda: self.generatePopUp("Krypton"))
        self.RubidButton.clicked.connect(lambda: self.generatePopUp("Rubid"))
        self.StrontButton.clicked.connect(lambda: self.generatePopUp("Stront"))
        self.CyrkonButton.clicked.connect(lambda: self.generatePopUp("Cyrkon"))
        self.NiobButton.clicked.connect(lambda: self.generatePopUp("Niob"))
        self.MolibdenButton.clicked.connect(lambda: self.generatePopUp("Molibden"))
        self.TechnetButton.clicked.connect(lambda: self.generatePopUp("Technet"))
        self.RutenButton.clicked.connect(lambda: self.generatePopUp("Ruten"))
        self.RodButton.clicked.connect(lambda: self.generatePopUp("Rod"))
        self.PalladButton.clicked.connect(lambda: self.generatePopUp("Pallad"))
        self.SrebroButton.clicked.connect(lambda: self.generatePopUp("Srebro"))
        self.KadmButton.clicked.connect(lambda: self.generatePopUp("Kadm"))
        self.IndButton.clicked.connect(lambda: self.generatePopUp("Ind"))
        self.CynaButton.clicked.connect(lambda: self.generatePopUp("Cyna"))
        self.AntymonButton.clicked.connect(lambda: self.generatePopUp("Antymon"))
        self.TelurButton.clicked.connect(lambda: self.generatePopUp("Telur"))
        self.JodButton.clicked.connect(lambda: self.generatePopUp("Jod"))
        self.KsenonButton.clicked.connect(lambda: self.generatePopUp("Ksenon"))
        self.CezButton.clicked.connect(lambda: self.generatePopUp("Cez"))
        self.BarButton.clicked.connect(lambda: self.generatePopUp("Bar"))
        self.HafnButton.clicked.connect(lambda: self.generatePopUp("Hafn"))
        self.TantalButton.clicked.connect(lambda: self.generatePopUp("Tantal"))
        self.WolframButton.clicked.connect(lambda: self.generatePopUp("Wolfram"))
        self.RenButton.clicked.connect(lambda: self.generatePopUp("Ren"))
        self.OsmButton.clicked.connect(lambda: self.generatePopUp("Osm"))
        self.IrydButton.clicked.connect(lambda: self.generatePopUp("Iryd"))
        self.PlatynaButton.clicked.connect(lambda: self.generatePopUp("Platyna"))
        self.ZlotoButton.clicked.connect(lambda: self.generatePopUp("Zloto"))
        self.RtecButton.clicked.connect(lambda: self.generatePopUp("Rtec"))
        self.TalButton.clicked.connect(lambda: self.generatePopUp("Tal"))
        self.OlowButton.clicked.connect(lambda: self.generatePopUp("Olow"))
        self.BizmutButton.clicked.connect(lambda: self.generatePopUp("Bizmut"))
        self.PolonButton.clicked.connect(lambda: self.generatePopUp("Polon"))
        self.AstatButton.clicked.connect(lambda: self.generatePopUp("Astat"))
        self.RadonButton.clicked.connect(lambda: self.generatePopUp("Radon"))
        self.FransButton.clicked.connect(lambda: self.generatePopUp("Frans"))
        self.RadButton.clicked.connect(lambda: self.generatePopUp("Rad"))
        self.RutherfordButton.clicked.connect(lambda: self.generatePopUp("Rutherford"))
        self.DubnButton.clicked.connect(lambda: self.generatePopUp("Dubn"))
        self.SeaborgButton.clicked.connect(lambda: self.generatePopUp("Seaborg"))
        self.BohryButton.clicked.connect(lambda: self.generatePopUp("Bohry"))
        self.HasButton.clicked.connect(lambda: self.generatePopUp("Hassium"))
        self.MeitnerButton.clicked.connect(lambda: self.generatePopUp("Meitner"))
        self.DarmsztadButton.clicked.connect(lambda: self.generatePopUp("Darmsztad"))
        self.RoentgenButton.clicked.connect(lambda: self.generatePopUp("Roentgen"))
        self.KopernikButton.clicked.connect(lambda: self.generatePopUp("Kopernik"))
        self.NihonButton.clicked.connect(lambda: self.generatePopUp("Nihon"))
        self.FlerowButton.clicked.connect(lambda: self.generatePopUp("Flerow"))
        self.MoskowButton.clicked.connect(lambda: self.generatePopUp("Moskow"))
        self.LivermorButton.clicked.connect(lambda: self.generatePopUp("Livermor"))
        self.TenesButton.clicked.connect(lambda: self.generatePopUp("Tenes"))
        self.OganessonButton.clicked.connect(lambda: self.generatePopUp("Oganesson"))


        #init frame
        self.frame1.setVisible(True)
        self.frame2.setVisible(False)

        self.mendelewButton.clicked.connect(self.toggle_frames)

    def generatePopUp(self, element):
        QMessageBox.information(self, "Nazwa pierwiastka", element)

    def toggle_frames(self):
        if self.frame1.isVisible(): 
            self.frame1.setVisible(False) 
            self.frame2.setVisible(True) 
            # self.mendelewButton.text="Obliczanie Konfiguracji"
        else: 
            self.frame1.setVisible(True) 
            self.frame2.setVisible(False)
            # self.mendelewButton.text="Układ Okresowy Pierwiastków Chemicznych"


    def generate_configuration(self):
        
        elements = load_elements("./data.csv")

        value = self.text_input.text()
        try:
            number = int(value)
            if number < 0 or number > 118:
                QMessageBox.critical(self, "Nie znaleziono", "Nie zidentyfikowano pierwiastka o podanej ilości elektronów")
            else:
                element = Element("None", value, elements)
                # print("Konfiguracja powłokowa")
                # print(element.podaj_konfiguracje_elektronowa())
                QMessageBox.information(self, "Konfiguracja powłokowa", element.podaj_konfiguracje_elektronowa())
        except ValueError:
            correct_name = False
            for row in elements:
                if row[0].lower() == value.lower():
                    correct_name = True
                    element = Element(value, "0", elements)
                    QMessageBox.information(self, "Konfiguracja powłokowa", element.podaj_konfiguracje_elektronowa())
            if correct_name == False:
                QMessageBox.critical(self, "Nie znaleziono", "Nie odkryto jeszcze pierwiastka o podanej nazwie, sprawdź czy nie ma literówki ;)")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
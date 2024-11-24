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
        # self.frame2 = self.findChild(QFrame, 'mendelew_frame')

        #configuration elements
        self.text_input = self.findChild(QLineEdit, "text_input")
        self.send = self.findChild(QPushButton, "send")
        # self.result = self.findChild(QLabel, "result")
        self.send.clicked.connect(self.generate_configuration)

        #menu elements
        self.mendelewButton = self.findChild(QPushButton, "mendelewButton")
    
        #mendelew elements


        #init frame
        self.frame1.setVisible(True)
        # self.frame2.setVisible(False)


        def toggle_frames(self):
            if self.frame1.isVisible(): 
                self.frame1.setVisible(False) 
                # self.frame2.setVisible(True) 
            else: 
                self.frame1.setVisible(True) 
                # self.frame2.setVisible(False)


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
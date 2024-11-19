import csv
from Element import Element

def load_elements(file_path): 
    with open(file_path) as file: 
        file_reader = csv.reader(file, delimiter=',') 
        elements = list(file_reader)  
    return elements 

elements = load_elements("./data.csv")

print("WITAJ W LABOLATORIUM CHEMICZNYM")

while 1:
    value = input("Podaj nazwę pierwiastka lub wpisz liczbę elektronów: ")
    if(value == "Q"):
        break;
    try:
        number = int(value)
        if number < 0 or number > 118:
            print("Nie zidentyfikowano pierwiastka o podanej ilości elektronów\n")
        else:
            element = Element("None", value, elements)
            print("Konfiguracja powłokowa")
            print(element.podaj_konfiguracje_elektronowa())
    except ValueError:
        correct_name = False
        for row in elements:
            if row[0].lower() == value.lower():
                correct_name = True
                element = Element(value, "0", elements)
                print("Konfiguracja powłokowa")
                print(element.podaj_konfiguracje_elektronowa())
        if correct_name == False:
            print("Nie odkryto jeszcze pierwiastka o podanej nazwie, sprawdź czy nie ma literówki ;)\n")
    print("\nAby wyjść wpisz Q")
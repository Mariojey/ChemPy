class InvalidName(Exception):
    pass

class NegativeCountElectrons(Exception):
    pass

class RealName():

    def __set_name__(self,owner,name):
        self._name = name
    
    def __get__(self,instance,owner):
        return instance.__dict__[self._size]
    
    def __set__(self, instance, value):
        if value == "" or value == " ":
            raise InvalidName("Invaild Name")
        instance.__dict__[self._name] = value

class Element:

    name = RealName()
    
    def __init__(self, name, count_of_electrons, elements):

        self.elements = elements

        if name == "None":
            if int(count_of_electrons) > 0 and int(count_of_electrons) < 119:
                self.electrons = count_of_electrons
                found = False
                for roww in elements:
                    if roww[1] == count_of_electrons:
                        self.name = roww[0]
                        self.valence = roww[2]
                        self.row = roww[3]
                        self.col = roww[4]
                        self.short = roww[5]
                        found = True
                        break;
                if not found: 
                    raise NegativeCountElectrons("Nie zidentyfikowano pierwiastka o podanej ilości elektronów")
            else: 
                raise NegativeCountElectrons("Nie zidentyfikowano pierwiasta o podanej ilości elektronów")
        
        else:
            correct_name = False
            for roww in elements:
                if roww[0].lower() == name.lower():
                    self.name = name
                    self.electrons = roww[1]
                    self.valence = roww[2]
                    self.row = roww[3]
                    self.col = roww[4]
                    self.short = roww[5]
                    correct_name = True
                    break;
            if correct_name == False:
                raise InvalidName("Nie odkryto jeszcze pierwiastka o podanej nazwie, uruchom program jeszcze raz i  sprawdź czy nie ma literówki ;)")

    def podaj_konfiguracje_elektronowa(self):

        shell_names = ['K','L','M','N','O','P','Q']
        result = ""

        if self.row == '1':

            result = "K - " + self.valence

        elif self.row == '2':

            result = "K - " + str(int(self.electrons) - int(self.valence))
            result = result + ", L -" + self.valence

        else:

            used_electrons = 0

            for i in range(0, int(self.row) -1):

                max_electrons = 2*((i+1)**2)
                electrons_for_use = int(self.electrons) - int(self.valence) - used_electrons

                if electrons_for_use >= max_electrons:
                    electrons_for_use = max_electrons

                result = result + shell_names[i]
                result = result + " - "
                result = result + str(electrons_for_use)
                result = result + ", "
                used_electrons = electrons_for_use

            result = result + shell_names[i+1] + " - " + self.valence + ","

        return result

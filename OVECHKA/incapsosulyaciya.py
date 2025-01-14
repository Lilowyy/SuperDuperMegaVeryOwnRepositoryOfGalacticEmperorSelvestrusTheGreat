class PrimerC():
    def __init__(self, a):
        self.__a = a

        #Геттер
    def get_a(self):
        return self.__a
        #Сеттер
    def set_b(self, b):
        self.__b = b

        Name = PrimerC("Monika")
        print(Name.get_a())

        Name.set_b("Sayori")
        print(Name.get_a())
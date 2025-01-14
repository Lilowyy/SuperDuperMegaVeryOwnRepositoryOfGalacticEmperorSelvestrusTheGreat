class Soda:
    def __init__(self, supplement=None):
     self.supplement=supplement

    def show_my_drink(self):
        if self.supplement:
            print("газировка и", self.supplement)
        else:
            print("обычная газировка")
ssoda=Soda()
ssoda.show_my_drink()

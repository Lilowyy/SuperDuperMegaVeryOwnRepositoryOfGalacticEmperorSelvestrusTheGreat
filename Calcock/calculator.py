class Calculator:
    def __init__(self):
        self.result = 0

    def calc_sum(self, x, y):
        self.result = x + y
        return self.result
    
    def calc_subtract(self, x, y):
        self.result = x - y
        return self.result
    
    def calc_multiply(self, x, y):
        self.result = x * y
        return self.result

    def calc_divide(self, x, y):
        if y == 0:
            raise ValueError
        self.result = x / y
        return self.result
    

calc = Calculator()
print(calc.calc_sum(1, 2))
print(calc.calc_subtract( 3, 5))
print(calc.calc_multiply( 2, 2))
print(calc.calc_divide( 6, 2))
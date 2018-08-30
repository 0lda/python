
class Calculator:
    name = 'LDA'
    age = 22

    def __init__(self, name, price, height, width, weight):   # 注意，这里的下划线是双下划线
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight

    def add(self, x, y):
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x/y)

calcul = Calculator()

calcul.add(5, 8)
calcul.minus(88, 8)
calcul.divide(33, 8)
calcul.times(8, 8)

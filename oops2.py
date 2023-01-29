class Calc:
    result = 0

    def show(self):
        return self.result
    
    def add(self, n1, n2):
        self.result = n1 + n2

    def sub(self, n1, n2):
        self.result = n1 - n2

    def mul(self, n1, n2):
        self.result = n1 * n2

    def square(self, n):
        self.result = n ** 2

c = Calc()
c.add(10, 20)
print(c.show())
c.sub(12, 3)
print(c.show())
c.mul(10, 20)
print(c.show())
c.square(10)
print(c.show())
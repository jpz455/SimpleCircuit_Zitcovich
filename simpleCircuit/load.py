class load:
    def __init__(self, name: str, bus1: str, p:float,q:float):
       self.name = name
       self.bus1 = bus1
       self.p = p
       self.q = q
       self.g = self.calc_g()

    def calc_g(self):
        return self.p / (self.p ** 2 + self.q ** 2) if (self.p != 0 or self.q != 0) else 0.0







class Load:
    def __init__(self, name: str, bus1: str, p:float,v:float):
       self.name = name
       self.bus1 = bus1
       self.p = p
       self.v = v
       #P = I*V  --> I = P/V
       #V = IR   --> R = V/I
       self.i = p/v
       self.r = v/self.i
       self.g = self.calc_g(self.r)

    def calc_g(self,r:float):
        return 1/r










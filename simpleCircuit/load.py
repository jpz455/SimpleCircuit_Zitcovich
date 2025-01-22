import numpy as np
class Load:
    def __init__(self, name: str, bus1: str, p:float,v:float):
       self.name = name
       self.bus1 = bus1
       self.p = p
       self.v = v
       #P = I*V  --> I = P/V
       #V = IR   --> R = V/I
       #G = I/V --> G = P/V^2
       self.g=self.calc_g()

    def calc_g(self):
        return self.p/self.v**2










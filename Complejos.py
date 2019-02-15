import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
        
    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                          self.imag + otro.imag)
        return result
        
    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                          self.imag - otro.imag)
        return result
        
    def multiplicar(self, otro):
        result = Complejo((self.real*otro.real - self.imag*otro.imag),
                          (self.real*otro.imag + self.imag*otro.real))
        return result
        
    def dividir(self, otro):
        a = (self.real*otro.real + self.imag*otro.imag)
        b = (self.imag*otro.real - self.real*otro.imag)
        denom = ((otro.real**2)+(otro.imag**2))
        result = Complejo((a/denom), 
 			  (b/denom))
        return result
    
    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag
        
class TestComplejo(unittest.TestCase):
    
    def test_sumar(self):
        
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)
        
        suma = c1.sumar(c2)
        
        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)
    
    def test_restar(self):
        
        c1 = Complejo(6,1)
        c2 = Complejo(8,4)
        
        restar = c1.restar(c2)
        
        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)
        
    def test_multiplicar(self):
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)
        
        multiplica = c1.multiplicar(c2)
        
        self.assertEqual(multiplica.real, -5)
        self.assertEqual(multiplica.imag, 10)
    
    def test_dividir(self):
        c1 = Complejo(3)
        c2 = Complejo(1,-2)
        
        divide = c1.dividir(c2)
        
        self.assertEqual(divide.real, float(3/5))
        self.assertEqual(divide.imag, float(6/5))
    
if __name__ == "__main__":
    unittest.main()

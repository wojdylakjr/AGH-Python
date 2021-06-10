from abc import abstractmethod
from abc import ABC

class Integral(ABC):
  '''Klasa bazowa reprezntujaca ogolny typ calki'''
  def __init__(self, min, max, steps, fun):
    '''Metoda inicjalizujaca określająca granice całkowania, liczbę kroków oraz funkcję podcałkową'''
    self.start = min
    self.end = max
    self.steps = steps
    self.fun = fun
  
  @abstractmethod
  def integration(self):
    '''Metoda wirtulna, definiiowana w zaleznosci od typu'''
    pass

class Trapez(Integral):
  '''Klasa pochodna reprezentujaca calke obliczana metoda trapezow'''
  def integration(self):
    h = (self.end - self.start) / self.steps
    s = 0
    for i in range(self.steps+1):
      s += self.fun(self.start + i*h) + self.fun(self.start + (i+1)*h)
    s *= (h / 2)
    return s

class Simpson(Integral):
  '''Klasa pochodna reprezentujaca calke obliczana metoda Simpsona'''
  def integration(self):
    h = (self.end - self.start) / (2*self.steps)
    s = self.fun(self.start)
    
    for i in range(1,2*self.steps):
      if(i%2 == 1):
        s += 4*self.fun(i*h)
  
    for i in range(2, 2*self.steps):
      if(i%2 == 0):
        s += 2*self.fun(i*h)
    
    s += self.fun(self.end)
    s = (h / 3)*s
    return s

def func(x):
  return 2 - x

test1 = Trapez(0, 2, 1000, func)
print("Metoda trapezow:")
print(test1.integration())

test2  = Simpson(0, 2, 1000, func)
print("Metoda Simpsona:")
print(test2.integration())
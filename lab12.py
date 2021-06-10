# Proszę napisać iterator zwracający kolejny wyraz ciągu arytmetycznego dwoma sposobami i porównać ich wykorzystanie (2p)
print("zad1")
class Arythmetic1:

  def __init__(self, number, a0,  r):
    self._number = number;
    self._a0 = a0
    self._r = r;
  
    
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._a0 >= self._number:
      raise StopIteration
    self._a0 = self._a0 + self._r
    return self._a0

class Arythmetic2:
  def __init__(self, number, a0,  r):
    self._number = number;
    self._a0 = a0
    self._r = r;

  def __iter__(self):
    return Arythmetic2(self._number, self._a0, self._r)

  def __next__(self):
    if self._a0 >= self._number:
      raise StopIteration
    self._a0 = self._a0 + self._r
    return self._a0
  
# test = Arythmetic1(100,0,2)
for i in Arythmetic1(100,0,2):
  # for j in Arythmetic1(100,0,2):
  print(i, end = ' ')
print()

  # test = Arythmetic1(100,0,2)
for i in Arythmetic2(100,0,5):
  # for j in Arythmetic1(100,0,2):
  print(i, end = ' ')
print()







# Proszę utworzyć iterator zwracający liczbę pseudolosową generowaną wg wzoru Xn+1 = (aXn + c)%m, dla m = 248, a = 44485709377909, c = 0, x0 = 1. Korzystając z zaimplementowanego iteratora proszę sprawdzić ile punktów trzeba wylosować, aby obliczyć wartość całki z zadaną dokładnością, np. 10−7 (stosujemy metodę Monte Carlo) (5p).

# Losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania. Wprowadzamy zmienną pomocniczą t, którą modyfikować będziemy następująco:
# jeżeli wylosowany punkt (xi, yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej, czyli spełnia nierówność: 0 < yi ≤ f(xi), wówczas zwiększamy zmienną t o jeden,
# jeżeli wylosowany punkt (xi, yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej, czyli spełnia nierówność: 0 > yi ≥ f(xi), wówczas zmniejszamy zmienną t o jeden,
# jeżeli wylosowany punkt (xi, yi) nie spełnia żadnego z powyższych warunków, wówczas pozostawiamy zmienną t bez zmian.
# Całkę obliczamy jako Pprostokątat/n
print("\nzad2")

class random:
  def __init__(self):
    self._m = 2**48
    self._a = 44485709377909
    self._c = 0
    self._x0 = 1
  
  def __iter__(self):
    return self
  
  def __next__(self):
    self._x0 = (self._a * self._x0 + self._c)%self._m
    return self._x0

def function(x):
  return 2 - x


# for i in random():
#   print(i)









# Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10-5 (pochodna - scipy.misc) (3p).
import scipy.misc as misc
import math

print("\nzad3")
class Newton_Raphson:
  def __init__(self, function, x, eps):
    self._function = function
    self._x = x
    self._eps = eps

  def __iter__(self):
    return self
  
  def __next__ (self):
    temp = self._x
    self._x = self._x - self._function(self._x)/misc.derivative(self._function, self._x)
    if abs(self._x - temp) < self._eps:
      raise StopIteration
    return self._x
  
def fun(x):
  return math.sin(x) - (0.5 * x)**2

test = Newton_Raphson(fun, 1.5 , 10 **-5)
for i in test:
  print(i)

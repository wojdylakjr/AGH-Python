

#1. Proszę wygenerować losowy ciąg zer i jedynek o długości N. Proszę napisać generator zwracający liczbę zer oddzielających kolejne jedynki w sekwencji przekazanej jako parametr. Korzystając z utworzonego generatora proszę obliczyć średnią odległość między kolejnymi jedynkami w wygenerowanym wcześniej ciągu (2p)
print("\nZad 1")
def gen_zeros(l):
  amount = 0
  first_zeros = 0 #tutaj sprawdzam ile jest 0 na poczatku, ktore nie stoja pomiedzy 1
  if(l[0] == 0):
    for i in l:
      if i == 0:
        first_zeros += 1
      else:
        break

        
  for i in l[first_zeros:]:
    if i == 0:
      amount += 1
    elif amount != 0:
      yield amount
      amount = 0

import random
N = 10
l = [random.randint(0,1) for _ in range(N)]
print(l)
zeros_amount = list(gen_zeros(l))
print("Ilosc odzielajacych zer: ", zeros_amount)
print("Srednia dlugosc ciagu zer:", sum(zeros_amount) / len(zeros_amount))





#2. Proszę napisać trzy funkcje generatorowe:
# -zwracającą kolejne elementy ciągu Fibonacciego (nieskończony),
# -zwracającą te wartości z przekazanej jako parametr sekwencji, które są parzyste/nieparzyste
# -zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji
# Korzystając ze zdefiniowanych funkcji proszę obliczyć sumę parzystych/nieparzystych elementów ciągu Fibonacciego mniejszych od 100 (2p)
print("\nZad 2")
def gen_fib(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x,y= y, x+y

def gen_parzyste(l):
  for i in l:
    if i%2 == 0:
      yield i

def gen_mniejsze(l, x):
  for i in l:
    if i < x:
      yield i
    else:
      break

fib = list(gen_fib(10))
print("Fibonaci dla 10 liczb:", fib)
print("Parzyste:",list(gen_parzyste(fib)))
fib = list(gen_fib(10000))
fib = list(gen_parzyste(fib))
# print(list(gen_mniejsze(fib,5)))
print("Suma parzystych elementow mniejszych od 100 ciagu Fibonacciego: ",sum(list(gen_mniejsze((fib),100))))

#3. Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych (2p)
# Do testów: range(7), range(-7), range(2,7), range(7,2), range(2,7,2), range(2,7,-2), range(7,2,2), range(7,2,-2)
print("\nZad 3")
def myRange(start, stop = None, step = 1.):
  start = float(start)
  if stop == None:
    stop = start
    start = 0.

  if(start > stop and step <0):
    while start > stop:
      yield start
      start = start + step

  while start < stop:
    if step >= 0 and start >= stop:
      return
    if step < 0 and start <= stop:
      return
    yield start
    start = start + step
  
for i in range(2,7):
  print(i)
for i in myRange(2,7):
  print(i)



#4. Proszę napisać generator obliczający ui wg zależności:
# ui=ui-1+a/xi-1, z wartością początkową u0=0 dla x0=1 oraz z xi=x0+ia
# Obliczenia proszę wykonać dla a=0.05 i przerwać je dla x=1.5. Zależność pozwala na wyznaczenie przybliżonej wartości logarytmu naturalnego z danej liczby. Generator ma zwracać x oraz przybliżoną i dokładną wartość logarytmu naturalnego dla danego x (2p)
print("\nZad 4")

from math import log
def gen_ui():
   u = 0
   x_0 = 1
   a = 0.05
   i = 1
   x = 1
   while x <= 1.5:
     yield x, u, log(x)
     u = u + a/x
     x = x_0 + i*a
     i+= 1

for i in gen_ui():
  print(i)
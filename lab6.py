#Zad 1. Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję tak, aby uzupełnić poniższy kod:

# import time
# import sys

# powt=1000
# N=10000
# (...)
# print(sys.version)
# test=(forStatement, listComprehension, mapFunction, generatorExpression)
# for testFunction in test:
#     print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych jest N wartości.

# Proszę wykonać testy (wszystko w ramach tych samych funkcji):
#1.         dodawanie elementu
#2.         dodawanie elementu podniesionego do kwadratu
#3.       sumowanie elementów z wykorzystaniem pętli for
#4.       sumowanie z wykorzystaniem funkcji sum
#5.         konwersja obiektu map i generatora do listy

# Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

print("Zad 1")
import time
import sys

powt=1000
N=10000
def forStatement():
  l = []
  for i in range(N):
    l.append(i)
    # l.append(i**2) #2.
  return l

def listComprehension():
  return [i for i in range(N)] 
  # return [i**2 for i in range(N)] #2.

def mapFunction():
  return map (lambda x: x, range(N))
  # return list(map(lambda x: x,range(N))) #5.

def generatorExpression():
  return (i for i in range(N))
  # return (i**2 for i in range(N)) #2.
  # return list(map(lambda x: x,range(N))) #5.

def tester(testFunction):
  t1 = time.time_ns()
  for _ in range(powt):
    testFunction()

    # s = 0
    # for i in testFunction(): #3.
    #   s=s+i

    # sum(testFunction()) #4.
  t2 = time.time_ns()
  return t2 - t1 



print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
# for testFunction in test:
    # print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

#wyniki
#1. dodawanie elementu
# [GCC 7.5.0]
# forStatement         => 6788854476
# listComprehension    => 3452993093
# mapFunction          => 3527067
# generatorExpression  => 1258057

#2. dodawanie elementu podniesionego do kwadratu
# [GCC 7.5.0]
# forStatement         => 14136122113
# listComprehension    => 11405745882
# mapFunction          => 8076633
# generatorExpression  => 1061101

#3. sumowanie elementów z wykorzystaniem pętli for
# [GCC 7.5.0]
# forStatement         => 3325796140
# listComprehension    => 3106960686
# mapFunction          => 3871586578
# generatorExpression  => 2085792098

#4. sumowanie elementów z wykorzystaniem funkcji sum()
# [GCC 7.5.0]
# forStatement         => 2435426210
# listComprehension    => 1600985559
# mapFunction          => 2000100403
# generatorExpression  => 1269544344

#5.
# [GCC 7.5.0]
# forStatement         => 3037883582
# listComprehension    => 1683762823
# mapFunction          => 5526952904
# generatorExpression  => 3879701222

#Zad 2.Proszę utworzyć dwie listy po sto wartości losowych z przedziału [0,20) każda. Następnie na ich podstawie proszę utworzyć listę dwuelementowych krotek, elementów o jednakowych indeksach w listach wyjściowych spełniających warunek, że suma ich wartości jest większa od 3 i mniejsza od 15. Należy wykorzystać listę składaną oraz funkcje filter i zip (2p)
print("Zad 2")
import random
N = 100
l1 = [random.randint(0,20) for i in range(N)]
l2 = [random.randint(0,20) for i in range(N)]
l3 = list(filter(lambda x: x[0] + x[1] > 3 and x[0] + x[1] < 15, zip(l1, l2)))
print(l3)




#Zad 3. Proszę napisać funkcję myreduce przyjmującą dwa parametry (funkcję i sekwencję) oraz zwracającą liczbę. Funkcja przekazywana jako parametr będzie funkcją przyjmującą dwa parametry. Działanie funkcji proszę przetestować korzystając z wyrażenia lambda dla dodawania i mnożenia (2p)
print("Zad 3")
def myreduce(func, l):
  temp = l[0]
  for i in l[1:]:
    temp = func(temp,i)
  return  temp

lista = [3,2,1,2,5]
print(myreduce(lambda x,y: x * y, lista))
print(myreduce(lambda x,y: x + y, lista))

#Zad 5. Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako współrzędne punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym elementem jest lista x-ów, a drugim lista y-ów. Proszę to zrobić w jednej linijce korzystając z funkcji myreduce, wyrażenia lambda oraz wbudowanej funkcji map (obie listy tworzymy jednocześnie!) (2p)
print("Zad 5")
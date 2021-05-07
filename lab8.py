#1. Proszę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku, co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)
print("Zad 1")
def fun(file, n):
  with open(file) as f:
    lines = f.readlines()
    print(lines[:n])
    print(lines[-n:])
    print(lines[::n])
    # print([line.split(" ")[n-1] for line in lines])
    print([line[n-1] for line in lines])

fun("plik1.txt", 3)


#2. Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
# -pierwsza kolumna - numer wiersza,
# -druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
# t-rzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)
# (2.5p)
# PLIKI TESTOWE: data.zip
# data0.in data1.in ... data.out
print("\nZad 2")
import glob 
import numpy
matrix = {}

for file  in glob.glob("data*.in"):
  with open(file) as f:
    for counter, line in enumerate(f):
      matrix.setdefault(counter,[]).append(float(line))

with open('zad2','w') as pl:
  for i in matrix:
    # pl.write(f'i = {i}, srednia = {numpy.average(matrix[i])}, odchylenie = {numpy.std(matrix[i])}\n')
    pl.write(f'{i} {numpy.average(matrix[i])} {numpy.std(matrix[i])}\n')



#3. Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowa (1p)

print("\nZad 3")
import matplotlib.pyplot as plt

def drawPlot(name):
  x,y,z=numpy.loadtxt(name, unpack=True)
  plt.plot(x, y,z, 'o')
  plt.show()

drawPlot("zad2")


#4. Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób, w kolejnych latach. Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się "nazwisko", kolejne kolumny będą odpowiadały pozycja danej osoby na liście rankingowej w kolejnych latach, od 2000 do 2020 (2.5p)
print("\nZad 4")
dane = []
s = {}

for file  in glob.glob("20*.txt"):
  with open(file) as f:
    for counter, line in enumerate(f):
      dane.append(line.split(" "))
      s[dane[counter][0]] = float(dane[counter][1])
      sort = sorted(s.items(), key = lambda x: x[1])
      with open('zad4','w') as pl:
        for i in sort:
          pl.write(f'{i[0]} {i[1]} \n')




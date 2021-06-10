

# Proszę utworzyć klasę Tablica, a w niej metody:
# inicjalizującą przyjmującą jako parametr wymiar tablicy oraz jej elementy (jeżeli liczba elementów nie pozwala na inicjalizację tablicy proszę zgłosić wyjątek),
# przeciążającą operator dodawania,
# przeciążającą operator dodawania przyrostowego,
# przeciążającą operator nawiasowy (pobranie i przypisanie wartości, proszę zapewnić brak możliwości przypisania niepoprawnej wartości np. jeśli tablica jest dwuwymiarowa nie można zastąpić wiersza pojedynczą wartością),
# pozwalającą na sprawdzenie wymiaru tablicy,
# wypisanie tablicy na ekran.
# (5p)
print("\nzad1")
class wrongSize(Exception):
  pass

class Tablica:
  def __init__(self, size, array1):
    if size < len(array1):
      print("Zly rozmiar tablicy")
      raise wrongSize
    self._size = size;
    self._array1 = array1;
    # print(self._array1)

  def __len__(self):
    return len(self._array1)
  
  def print(self):
    print(self._array1)
  
  def __getitem__(self, key):
    return self._array1[key]

  def __setitem__(self, key, value):
    if type(self._array1[key]) != list and value is not list:
      self._array1[key] = value

  def __add__(self, array1):
    tempArray = [array1[i] + self._array1[i] for i in range(len(array1))]
    return Tablica(len(tempArray), tempArray)
  
  def __iadd__(self, other):
    for i in range(len(self._array1)):
      self._array1[i] += other._array1[i]
    return(self)

    

tab0 = Tablica(5,[[1,2], [3,4],[5,6]])
tab0[0]= 0
tab0.print()
tab1 = Tablica(5,[3,4,5,6,8])
tab2 = Tablica(5,[5,2,3,1,3])
tab3 = tab1 + tab2
tab1[0]=0
tab1.print()
tab2.print()
tab3.print()
print(len(tab3))
tab4 = Tablica(5,[0,0,0,0,0])
tab4 += tab1
tab4 += tab2
tab4 += tab3
tab4.print()
# 1. Proszę napisać funkcję, do której można przekazać zmienną liczbę parametrów, zwracającą listę. Do wynikowej listy trafiają elementy, które powtarzają się we wszystkich parametrach przekazanych do funkcji, np. ([1,2,3], (1,3,5), [3,2]) -> [3], ([1,2,3], (1,3,5), [3,2,1]) -> [1,3].
# Proszę użyć konstrukcji for-else (2p)

print("\nZad1")

def fun2(*args):
  lista = []
  for j in args[0]:
    for l in args[1:]:
        if j not in l:
          break
    else:
        lista.append(j)
  return lista

a,b,c =  [1,2,3], (1,3,5), [3,2]
d,e,f = [1,2,3], (1,3,5), [3,2,1]
print("Test1: ", fun2(a,b,c))
print("Test2: ", fun2(d,e,f))

# 2. Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z wartością domyślną True. Funkcja zwraca listę dwuelementowych krotek zawierających elementy o tych samych indeksach z obu sekwencji. Jeżeli wartość trzeciego parametru wynosi True, długość zwracanej listy równa jest długości krótszej z przekazanych sekwencji, w przeciwnym wypadku brakujące elementy w krotkach uzupełniamy wartością None. Budowanie każdej z wynikowych list jedna linijka, proszę nie używać funkcji wbudowanych! (2p) 
print("\nZad2")
def fun3(s1, s2, p = True):
  if p:
    lista1 = [(s1[i], s2[i]) for i in range(min(len(s1), len(s2)))]
    return lista1
  else:
    lista2 = [(s1[i], s2[i]) if i < min(len(s1), len(s2)) else (None, s2[i]) if len(s2) > len(s1) else(s1[i],None) for i in range(max(len(s1), len(s2)))]
    return lista2

l1 = [1,2,3,4,5]
l2 =['x', 'z']
print("Test1: ", fun3(l1,l2))
print("Test2: ", fun3(l1,l2,False))

# 3. Proszę napisać funkcję umożliwiającą rozmienienie kwoty pieniędzy przekazanej jako jej pierwszy parametr nominałami określonymi poprzez drugi parametr - wartość domyślna krotka (10,5,2) (algorytm zachłanny). Proszę sprawdzić działanie funkcji przekazując inny zestaw monet (2p)
print("\nZad3")

def fun4(price, coins = (10,5,2)):
  change = []
  counter = 0
  while(price >= 0):
    if price >= coins[counter]:
      price -= coins[counter]
      change.append(coins[counter])
    elif counter + 1 < len(coins):
        counter += 1
    else:
      break
  return change

print("Test1: ", fun4(18))
print("Test2: ", fun4(25,(10,3,1)))



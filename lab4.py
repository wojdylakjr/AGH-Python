# 1. Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
# Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy, mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku (2p)
# 2.Proszę utworzyć losowy string o długości k zawierający tylko małe litery, pomiędzy poszczególne litery proszę wstawić kropkę (1p)
# 3.Proszę utworzyć listę stu wartości losowych z przedziału [0,20). Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są liczbami z listy, a wartościami lista ich indeksów.
# w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate (1.5p)
# w rozwiązaniu proszę wykorzystać metody setdefault i index (1.5p)
# 4.Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych składających się z n cyfr, gdzie n jest z przedziału [3,6], jest liczbami palindromowymi. Wynik proszę zapisać w słowniku (2p)
# 5.Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne liczby naturalne, a wartościami liczby losowe z przedziału [1,100). Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami.
# Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze są kluczami występującymi jednocześnie w obu wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości związanych z danym kluczem w słownikach oryginalnych  (2p)


import random
import string
#-------------ZAD1------------------
k = 10
arr = []
dic ={}
for i in range(k):
  arr.append(random.randint(0, 5*k))
print(arr)
for i in range(100):
  counter = 0
  arr_copy = arr[:]
  random.shuffle(arr)
  for j in range(k):
    if arr[j] == arr_copy[j]:
      counter+=1

dic[counter] = 1 if counter not in dic else dic[counter]+1
print(dic)


#-------------ZAD2------------------
st = '.'.join(random.choice(string.ascii_lowercase) for i in range(k))
print(st)


#-------------ZAD3------------------
arr1 = []
for i in range(100):
  arr1.append(random.randint(0, 20))
dic1 = {}
for index, value in enumerate(arr1):
  dic1.setdefault(value,[]).append(index)
# print(dic1)
dic2 = {}
index = 0
for i in arr1:
  dic2.setdefault(i,[]).append(arr1.index(i, index))
  index = arr1.index(i, index) + 1
# print(dic2)


#-------------ZAD4------------------
arr2 = []

for n in range(3,7):
  counter = 0
  for _ in range(10000):
    i=random.randint(10**n, 100**n)
    if str(i) == str(i)[::-1]:
      counter += 1
  print('Dla liczb ', n,' elemntowych bylo ', counter,' palindromow')


#-----------ZAD5-----------------
dic3 = {}
dic4 = {}
for i in range (10):
  dic3[i] = random.randint(1,100)
  dic4[i] = random.randint(1,100)
print(dic3)
print(dic4)
dic3 = dict((v,k) for k,v in dic3.items())
dic4 = dict((v,k) for k,v in dic4.items())
print(dic3)
print(dic4)

new_dic = {}
for i in dic3.keys():
  if i in dic4.keys():
    new_dic[i] = (dic3[i], dic4[i])
print(new_dic)
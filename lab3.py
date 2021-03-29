# 1.Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy programu. Jeżeli program został uruchomiony bez podania parametrów proszę wypisać na ekran komunikat informujący o właściwym sposobie uruchomienia programu (1p)
# 2.Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy: zawierającą małe litery, zawierającą duże litery, zawierającą cyfry oraz zawierającą wszystko co nie jest literą (2p)
# 3.Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć listę małych liter bez powtórzeń. Następnie proszę utworzyć nową listę, w której każdy element jest dwuelementową krotką (litera, krotność jej wystąpienia w liście oryginalnej) (2p)
# 4.Otrzymaną w powyższym punkcie listę proszę wyświetlić w kolejności od najwyższej krotności (1p)
# 5.Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element jest liczbą pobraną z listy cyfr, drugi natomiast wartością funkcji liniowej ax+b dla danej liczby; wartości współczynników proszę ustalić w następujący sposób: a równa się liczbie samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże (2p)


# python3 main.py test 3*5/2@ee1 4 PYTHON leSs0n
#zad1
import sys
if len(sys.argv) <= 1:
  print('Podaj argumenty wywolania programu')
else:
  s = ''.join(sys.argv[1:])
print(s)

#zad2
s_lower =[i for i in s if i.islower()]
s_upper =[i for i in s if i.isupper()]
s_digit =[i for i in s if i.isdigit()]
s_numeric =[i for i in s if not i.isalpha()]

print('Małe litery: ', s_lower)
print('Duże litery: ', s_upper)
print('Cyfry: ', s_digit)
print('Nie liczby: ', s_numeric)

#zad3
s_single_alpha = []
for i in s_lower:
  if  i not in s_single_alpha:
    s_single_alpha.append(i)
print('Male litery bez powtorzen: ', s_single_alpha)


s_tuple = [(i,s_lower.count(i)) for i in s_single_alpha]
print('Krotka: ', s_tuple)

#zad4
s_tuple.sort(key = lambda x: x[1], reverse=True)
print('Posortowane: ', s_tuple)

#zad5
samogloski = ['a','e', 'i', 'o', 'u', 'y',]
s_alpha =[i for i in s if i.isalpha()]
ilosc_sam = 0
ilosc_spol = len(s_alpha)
for i in s_alpha:
  if i in samogloski:
    ilosc_sam +=1
    ilosc_spol -=1
    
print(ilosc_sam, ilosc_spol)

x=[1,2,3,4,5,]
x_tuple = [(i,ilosc_sam * i + ilosc_spol) for i in x]
print(x_tuple)





#  #laczenie
# #  print('*'.join(('a','b','c')))
# print('asfdfsd'.replace('a', 'A'))
# tr = str.maketrans('abc', 'ABC')
# print(tr)
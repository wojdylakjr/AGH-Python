# Proszę utworzyć funkcję sprawdzającą poprawność numeru PESEL (3.5p)
# Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
print("zad1")
from datetime import date

class ZlyPesel(Exception):
  pass

def check_pesel(pesel, data, plec):
  print(pesel, data, plec)
  kod_miesiac = 0
  if data.year < 1900:
    kod_miesiac = 80
  elif data.year < 2000:
    kod_miesiac = 0
  elif data.year < 2100:
    kod_miesiac = 20
  elif data.year < 2200:
    kod_miesiac = 40
  elif data.year < 2300:
    kod_miesiac = 60
  
  sprawdz_plec = 0 if plec=="kobieta" else 1
  pesel_array = [int(i) for i in pesel]
  print(pesel_array)

  wagi = [1,3,7,9,1,3,7,9,1,3]
  suma = 0
  for i in range(len(wagi)):
    suma += int(pesel[i]) * wagi[i]
  suma = suma % 10
  suma = (10 - suma) % 10

  miesiac = pesel[2:4]
  temp = int(miesiac)%20
  miesiac_liczba = int(miesiac) - temp
  dzien = pesel[4:6]

    



  # suma_miesiac = int(pesel[2]) + int(pesel[3])
  # print(suma_miesiac)
  # print(len(data.month))
  # miesiac = 
  if str(data.year)[2] != pesel[0] and str(data.year)[3] != pesel[1]:
    raise ZlyPesel
  if temp != data.month:
    raise ZlyPesel
  if int(dzien) != data.day:
    raise ZlyPesel
  if miesiac_liczba!=kod_miesiac:
    raise ZlyPesel
  if pesel_array[9]%2 != sprawdz_plec:
    raise ZlyPesel
  if suma != int(pesel[10]):
    raise ZlyPesel



# and str(pesel_array[2] - kod_miesiac) == pesel[2]

# check_pesel("02070803628", date(1902,7,8), "kobieta")
check_pesel("00300509454",date(2000,10,5), "mezczyzna")




# Proszę napisać funkcję sprawdzającą czy elementy listy tworzą trójkę (a2+b2=c2)/czwórkę(a2+b2+c2=d2) pitagorejską (funkcja ma działać dla dowolnej długości "podciągu"!). Proszę zgłosić wyjątek w przypadku niepoprawnej długości listy oraz w przypadku, gdy lista nie zawiera żadnych trójek/czwórek pitagorejskich. Dla każdej trójki/czwórki proszę sprawdzić ile jest w niej wartości parzystych i nieparzystych (3p).
print("\nzad2")
class zla_dlugosc(Exception):
    pass
class nie_pitagorejski(Exception):
    pass
class inne(Exception):
    pass

def czy_pitagorejski(lista, n):
    try:
        if n > len(lista):
            raise zla_dlugosc
        num = 0
        i = 0
        p = 0
        for i in range(n):
                a = lista[i]
                b = lista[i+1]
                c = lista[i+2]
                d = lista[i+3]
                if(a**2 + b**2 + c**2 == d**2):                           
                    num += 1
        
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    if(d%2==0):
                        p+=1
                    print("Dla czworokatu ", a, b, c, d, "ilosc parzystych:", p)
                    p = 0
                    
                elif(a**2 + b**2 == c**2):
                    num += 1
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    print("Dla trojkatu", a, b, c, "ilosc parzystych:", p)
                    p = 0                    
                  
        if(num == 0):
            raise nie_pitagorejski
        else:
            print("znalezionych", num, "pitagorejskich trojkatow lub czworokatow")

            
    except inne:
        print("Cos poszlo nie tak")
    except zla_dlugosc:
        print("Zly rozmiar")
    except nie_pitagorejski:
        print("Nie ma zadnych pitagorejskich trojaktow ani czworokatow")

# l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
# l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
# l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l=(1,2,3,4,5,6,7,8,9)
czy_pitagorejski(l,5)
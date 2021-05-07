units = [(1,"I"), (4,"IV"), (5, "V"), (9, "IX"),(10,"X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400,"CD"), (500,"D"), (900,"CM"), (1000, "M")]

def arabicToRoman(n):
  '''
  Funkcja zamieniajaca liczbe arabska na rzymska
  '''
  print(n)
  # print(units)
  counter = len(units) - 1
  Roman = ""
  while n > 0:
    while units[counter][0] > n:
      counter -= 1
    Roman += units[counter][1]
    n -= units[counter][0]
  return Roman


def romanToArabic(roman):
  '''
  Funkcja zamieniajaca liczbe rzymska na arabska
  '''
  n = 0
  l = []
  for i in roman:
    for j in units:
      if i==j[1]:
        l.append(j[0])
  # print(l)
  
  copy = l
  for i in range(len(l) - 1):
    if l[i] >= l[i + 1]:
      copy[i] = l[i]
    else:
      copy[i+1] = l[i + 1] - l[i]
      copy[i] = 0
      
  # print(copy)
  return(sum(copy))

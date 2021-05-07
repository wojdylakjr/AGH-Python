
# funkcję konwertującą liczbę zapisaną w systemie arabskim na rzymski (3p)
print("\nzad1")

from module import arabicToRoman
help(arabicToRoman)
liczba = 2444
roman = arabicToRoman(liczba)
print(roman)

# funkcję konwertującą liczbę zapisaną w systemie rzymskim na arabski (3p)
print("\nzad2")
from module import romanToArabic
print(romanToArabic(roman))
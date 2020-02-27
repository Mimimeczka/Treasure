'''posortowana lista'''
# x = [1, 2, 3, 4, 5, 6, 7]
# # x = [2, 5, 8, 4, 3, 5, 6, 3, 3]
# def sprawdzanie_listy(lista):
#     for y in range(len(lista) - 1):
#         if lista[y] > lista[y + 1]:
#             return False
#     return True
#
# print(sprawdzanie_listy(x))

'''liczba doskonala'''
# def liczba_doskonala(liczba):
#     suma = 0
#     for x in range(1, int(liczba / 2) + 1):
#         if liczba % x == 0:
#             suma += x
#
#     if suma == liczba:
#         return True
#     else:
#         return False
#
# print(liczba_doskonala(60))

'''liczby doskonałe'''
# def liczby_doskonale(liczba):
#     suma = 0
#     znaleziono = 0
#     for x in range(1, liczba + 1):
#         for y in range(1, int(x / 2) +1):
#             if x % y == 0:
#                 suma += y
#
#         if suma == x:
#             print(f"Liczba {x} jest doskonałą")
#             znaleziono += 1
#         suma = 0
#
#     return znaleziono
#
# print("Znaleziono: " + str(liczby_doskonale(9999)))

'''inwersja'''
# def inwersja(lista):
#     para = 0
#     for x in range(len(lista)):
#         for y in range(x + 1, len(lista)):
#             if lista[x] > lista[y]:
#                 print(lista[x], "-", lista[y])
#                 para += 1
#     return para
#
# x = [1, 2, 5, 7, 4, 6]
# print("Znaleziono", inwersja(x))

'''skarb'''
# plansza = [["*" for x in range(10)]for y in range(10)]
#
# import random
# a = random.randint(0, 9)
# b = random.randint(0, 9)
# # plansza[a][b] = "s"
#
# def wyswietl_plansze():
#     liczba = 1
#     print("      1    2    3    4    5    6    7    8    9    10")
#     for linia in plansza:
#         print("%3s" % liczba, linia)
#         liczba += 1
#
# wyswietl_plansze()
# while True:
#     x, y = [int(x) for x in input("podaj wspolzedne oddzielone spacja: ").split(" ")]
#     plansza[x - 1][y - 1] = "O"
#     wyswietl_plansze()
#     plansza[x - 1][y - 1] = "*"
#     if a == x - 1 and b == y - 1:
#         print("WYGRANA")
#         break
#     if a > x - 1:
#         print("w dol")
#     if a < x - 1:
#         print("w gore")
#     if b < y - 1:
#         print("w lewo")
#     if b > y - 1:
#         print("w prawo")

'''sklep'''
# produkty = {1: ["banan", 5.5, 50], 2: ["jabłko", 2.3, 50], 3: ["pomarancze", 7.45, 50], 4: ["brzoskwinie", 9.75, 50]}
# dostep = "2020"
#
#
# def wyswietlanie_produktwo():
#     tekst = "produkt {0:4d} nazwa {1:20s} cena {2:.2f} zapasy {3:.2f}"
#     for i in produkty:
#         print(tekst.format(i, produkty[i][0], produkty[i][1], produkty[i][2]))
#
# def nowy_produkt():
#     nazwa = input("Nazwa nowego produktu: ")
#     cena = pobierz_liczbe("Cena nowego produktu: ")
#     waga = pobierz_liczbe("Waga nowego produktu: ")
#     return [nazwa, cena, waga]
#
#
# def pobierz_liczbe(wiadomosc):
#     while True:
#         try:
#             return float(input(wiadomosc))
#         except ValueError:
#             print("nieprawidlowa wartosc")
#
# while True:
#     osoba = int(pobierz_liczbe("1 - kupujacy\n2 - sprzedający \n0 - zakoncz "))
#     if osoba == 1:
#         kwota_do_zaplaty = 0
#         while True:
#             wyswietlanie_produktwo()
#             x = int(pobierz_liczbe("Podaj numerek wybranego produktu:"))
#             y = pobierz_liczbe("Ilość wybranego produktu w kg. ")
#             kwota_do_zaplaty += y *  produkty[x][1]
#             produkty[x][2] -= y
#             z = int(pobierz_liczbe('''1 - kontynuowac zakupy \n0 - zakonczyc zakupy'''))
#             if z == 0:
#                 print("Do zapłaty {0:.2f}".format(kwota_do_zaplaty))
#                 break
#
#     elif osoba == 2:
#         haslo = input("Podaj hasło:")
#         if haslo == dostep:
#             while True:
#                 funkcja = int(pobierz_liczbe("1 - dodaj nowy produkt \n2 - usun produkt \n3 - edycja produktu \n0 - wyjscie"))
#                 if funkcja == 1:
#                     parametry_produktu = nowy_produkt()
#                     produkty[len(produkty) + 1] = [parametry_produktu[0], parametry_produktu[1], parametry_produktu[2]]
#                 elif funkcja == 2:
#                     wyswietlanie_produktwo()
#                     produkt_usuwany = int(pobierz_liczbe("Podaj numer usuwanego produktu"))
#                     produkty.pop(produkt_usuwany)
#                 elif funkcja == 3:
#                     wyswietlanie_produktwo()
#                     edytowanie = int(pobierz_liczbe("Wybierz numerek produktu, który chcesz zmodyfikowac"))
#                     parametry_produktu = nowy_produkt()
#                     produkty[edytowanie] = [parametry_produktu[0], parametry_produktu[1], parametry_produktu[2]]
#                 else:
#                     break
#         else:
#             print("Hasło nieprawidłowe")
#     else:
#         break

'''wyrażenie nawiasowe'''
# def wyrazenie_nawiasowe(napis, znakA, znakB):
#     licznik = 0
#     for x in napis:
#         if licznik == -1:
#             return False
#         if x == znakA:
#             licznik += 1
#         if x == znakB:
#             licznik -= 1
#     return licznik == 0
#
# print(wyrazenie_nawiasowe(")(", "(", ")"))

'''wyrażenie nawiasowe'''
# zbior = []
# def wyrezenie_nawiasowe(napis):
#     for x in napis:
#         if x in "({<[":
#             zbior.append(x)
#         if x in ")}>]":
#             if x == ")" and zbior.pop() != "(":
#                 return False
#             if x == "]" and zbior.pop() != "[":
#                 return False
#             if x == "}" and zbior.pop() != "{":
#                 return False
#             if x == ">" and zbior.pop() != "<":
#                 return False
#     return len(zbior) == 0
#
# print(wyrezenie_nawiasowe("()("))

'''quicksort'''
# def quick_sort(array, left, right):
#     i = left
#     j = right
#     pivot = array[int((i + j) / 2)]
#
#     while i < j:
#         while array[i] < pivot:
#             i += 1
#         while pivot < array[j]:
#             j -= 1
#
#         if i <= j:
#             temp = array[i]
#             array[i] = array[j]
#             array[j] = temp
#             i += 1
#             j -= 1
#
#         if left < j:
#             quick_sort(array, left, j)
#         if i < right:
#             quick_sort(array, i, right)
#
#
# arr = [1, 3, 2, 6, 5, 4, 2, 0, 1, 4, 5]
# quick_sort(arr, 0, 10)
# print(arr)

'''ułamek'''
'''zadanie z ułamkami'''

#
# class Ulamek:
#     def __init__(self, licznik, mianownik):
#         self.licznik = licznik
#         if mianownik != 0:
#             self.mianownik = mianownik
#         else:
#             raise ValueError("Mianownik nie może być zerem")
#
#     def __str__(self):
#         return f"{self.licznik}/{self.mianownik}"
#
#     def __nwd__(self, a, b):
#         # najwiekszy wspólny dzielnik dwuch liczb
#         while b != 0:
#             temp = b
#             b = a % b
#             a = temp
#         return a
#
#     def __nww__(self, c, d):
#         # najmniejsza wspólna wielokrotność dwuch liczb
#         return c / self.__nwd__(c, d) * d
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik + other.licznik
#
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#             return Ulamek(int(y), 1)
#
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             suma_licznikow = licznik_a + licznik_b
#
#             if suma_licznikow % mianownik == 0:
#                 suma_licznikow /= mianownik
#                 return Ulamek(int(suma_licznikow), 1)
#
#             nwd = self.__nwd__(suma_licznikow, mianownik)
#             return Ulamek(int(suma_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __iadd__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik + other.licznik
#
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#             return Ulamek(int(y), 1)
#
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             suma_licznikow = licznik_a + licznik_b
#
#             if suma_licznikow % mianownik == 0:
#                 suma_licznikow /= mianownik
#                 return Ulamek(int(suma_licznikow), 1)
#
#             nwd = self.__nwd__(suma_licznikow, mianownik)
#             return Ulamek(int(suma_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __radd__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik + other.licznik
#
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#
#             return Ulamek(int(y), 1)
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             suma_licznikow = licznik_b + licznik_a
#
#             if suma_licznikow % mianownik == 0:
#                 suma_licznikow /= mianownik
#                 return Ulamek(int(suma_licznikow), 1)
#
#             nwd = self.__nwd__(suma_licznikow, mianownik)
#             return Ulamek(int(suma_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __sub__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik - other.licznik
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#
#             return Ulamek(int(y), 1)
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             roznica_licznikow = licznik_a - licznik_b
#
#             if roznica_licznikow % mianownik == 0:
#                 roznica_licznikow /= mianownik
#                 return Ulamek(int(roznica_licznikow), 1)
#
#             nwd = self.__nwd__(roznica_licznikow, mianownik)
#             return Ulamek(int(roznica_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __isub__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik - other.licznik
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#
#             return Ulamek(int(y), 1)
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             roznica_licznikow = licznik_a - licznik_b
#
#             if roznica_licznikow % mianownik == 0:
#                 roznica_licznikow /= mianownik
#                 return Ulamek(int(roznica_licznikow), 1)
#
#             nwd = self.__nwd__(roznica_licznikow, mianownik)
#             return Ulamek(int(roznica_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __rsub__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         if self.mianownik == other.mianownik:
#             y = self.licznik - other.licznik
#
#             if y % self.mianownik == 0:
#                 y /= self.mianownik
#
#             return Ulamek(int(y), 1)
#         else:
#             mianownik = self.__nww__(self.mianownik, other.mianownik)
#             licznik_a = mianownik / self.mianownik * self.licznik
#             licznik_b = mianownik / other.mianownik * other.licznik
#             roznica_licznikow = licznik_b - licznik_a
#
#             if roznica_licznikow % mianownik == 0:
#                 roznica_licznikow /= mianownik
#                 return Ulamek(int(roznica_licznikow), 1)
#
#             nwd = self.__nwd__(roznica_licznikow, mianownik)
#             return Ulamek(int(roznica_licznikow / nwd), int(mianownik / nwd))
#
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         licznik = self.licznik * other.licznik
#         mianownik = self.mianownik * other.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __imul__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         licznik = self.licznik * other.licznik
#         mianownik = self.mianownik * other.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __rmul__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         licznik = self.licznik * other.licznik
#         mianownik = self.mianownik * other.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         licznik = self.licznik * other.mianownik
#         mianownik = other.licznik * self.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __itruediv__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         licznik = self.licznik * other.mianownik
#         mianownik = other.licznik * self.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __rtruediv__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.licznik * other.mianownik
#         licznik = other.licznik * self.mianownik
#
#         if licznik % mianownik == 0:
#             licznik /= mianownik
#             return Ulamek(int(licznik), 1)
#
#         nwd = self.__nwd__(licznik, mianownik)
#         return Ulamek(int(licznik / nwd), int(mianownik / nwd))
#
#
#     def __neg__(self):
#         return Ulamek(self.licznik * (-1), self.mianownik)
#
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) == int(licznik_b)
#
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) > int(licznik_b)
#
#
#     def __ge__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) >= int(licznik_b)
#
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) < int(licznik_b)
#
#
#     def __le__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) <= int(licznik_b)
#
#
#     def __ne__(self, other):
#         if isinstance(other, int):
#             other = Ulamek(other, 1)
#
#         mianownik = self.__nww__(self.mianownik, other.mianownik)
#         licznik_a = mianownik / self.mianownik * self.licznik
#         licznik_b = mianownik / other.mianownik * other.licznik
#         return int(licznik_a) != int(licznik_b)

'''zadanie 4'''
# import os
# # os.listdir("/Users") # zwraca tablice z nazwami wszystkich plików i katalogów w danym katalogu
# def print_directory_content(path, level):
#     current_dir = os.listdir(path)
#     for file in current_dir:
#         if os.path.isdir(path + "/" + file):
#             print("|" + " " * (level * 4) + "-- " + path + "/" + file)
#             print_directory_content(path + "/" + file, level + 1)
#         else:
#             if current_dir.index(file) == (len(current_dir) - 1):
#                 print("|" + " " * (level * 4) + "\\-- " + file)
#             else:
#                 print("|" + " " * (level * 4) + "|-- " + file)
#
# print("test")
# print_directory_content(".", 0)

'''zadanie 11'''
# class Element:
#     def __init__(self, value):
#         self.value = value
#
#     def render(self):
#         return self.value
#
#
# class HeaderElement(Element):
#     def __init__(self, value):
#         Element.__init__(self, value)
#
#     def render(self):
#         return Element.render(self) + "\n====="
#
#
# class LinkElement(Element):
#     def __init__(self, value, value_y):
#         Element.__init__(self, value)
#         self.value_y = value_y
#
#     def render(self):
#         return f"({Element.render(self)}) [http://{self.value_y}]"
#
#
# class Document:
#     def __init__(self):
#         self.elements = []
#
#     def add_element(self, element):
#         self.elements.append(element)
#
#     def render_document(self):
#         string = ""
#         for x in self.elements:
#             string += x.render()
#             string += "\n"
#         return string
#
#
# document = Document()
# document.add_element(HeaderElement("Header"))
# document.add_element(LinkElement("ABC", "abc.com"))
# document.add_element(Element("simple"))
# print(document.render_document())


'''zadanie 12'''
# class Product:
#     def __init__(self, prod_id: int, name: str, price: float):
#         self.prod_id = prod_id
#         self.name = name
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
# class Basket:
#     def __init__(self):
#         self.products = {}
#         self.value_discounts = []
#         self.percent_discounts = []
#
#     def add_discount(self, discount): # dodaj znizke kwotowa
#         self.value_discounts.append(discount)
#
#     def add_percent_discount(self, percent_discount): #dodaj znizke procentowa
#         self.percent_discounts.append((100 - percent_discount.get_discount()) / 100)
#
#     def add_product(self, product, quantity):
#         self.products[product] = quantity
#
#     def count_total_price(self):
#         suma = 0
#         for x in self.products:
#             y = self.products[x]
#             suma += x.get_price() * y
#
#         sum_discounts = 0
#         for z in self.value_discounts:
#             sum_discounts += z.get_discount()
#
#         percent_discount_value = 1.0
#         for percent in self.percent_discounts:
#             percent_discount_value *= percent
#
#         to_pay = (suma - sum_discounts) * percent_discount_value
#
#         if to_pay > 0:
#             return to_pay
#         return 0
#
#     def generate_report(self):
#         print("Produkty w koszyku")
#         for a in self.products:
#             print(f"{a.name} ({a.prod_id}), cena: {a.price}, ilosc: {self.products[a]}")
#         print("Suma:")
#         return self.count_total_price()
#
#
# class ValueDiscount:
#     def __init__(self, discount: float):
#         self.discount = discount
#
#     def get_discount(self):
#         return self.discount
#
#
# class PercentDiscount:
#     def __init__(self, discount: float):
#         self.discount = discount
#
#     def get_discount(self):
#         return self.discount
#
#
# produktA = Product(1, "Woda", 10.0)
# produktB = Product(2, "Chleb", 5.0)
# basked = Basket()
# basked.add_product(produktA, 6)
# basked.add_product(produktB, 10)
# # discount = ValueDiscount(3.0)
# # discountx = ValueDiscount(7.0)
# # basked.add_discount(discount)
# # basked.add_discount(discountx)
# # basked.add_percent_discount(PercentDiscount(20))
# # basked.add_percent_discount(PercentDiscount(30))
# print(basked.generate_report())


'''robot'''
class Robot:
    def __init__(self):
        self.kierunek = "N"
        self.y = 0
        self.x = 0

    def wykonaj(self, instrukcja):
        for x in instrukcja:
            if x == "N":
                self.__na_przod__()
            elif x == "P":
                self.__obrot_w_prawo__()
            else:
                self.__obrot_w_lewo__()

    def __obrot_w_lewo__(self):
        if self.kierunek == "N":
            self.kierunek = "W"
        elif self.kierunek == "W":
            self.kierunek = "S"
        elif self.kierunek == "S":
            self.kierunek = "E"
        elif self.kierunek == "E":
            self.kierunek = "N"

    def __obrot_w_prawo__(self):
        if self.kierunek == "N":
            self.kierunek = "E"
        elif self.kierunek == "E":
            self.kierunek = "S"
        elif self.kierunek == "S":
            self.kierunek = "W"
        elif self.kierunek == "W":
            self.kierunek = "N"

    def __na_przod__(self):
        if self.kierunek == "N":
            self.y += 1
        elif self.kierunek == "E":
            self.x += 1
        elif self.kierunek == "S":
            self.y -= 1
        elif self.kierunek == "W":
            self.x -= 1

    def __str__(self):
        return f"kierunek: {self.kierunek} x:{self.x} y:{self.y}"

robot = Robot()
print(robot)
robot.wykonaj("NNPNLNPP")
print(robot)

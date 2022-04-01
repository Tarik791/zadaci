#!/usr/bin/env python3
try:
  # Definišemo listu cijelih brojeva
  numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

  # ako želimo prikaz liste
  # print(numberList)

  # Uzimamo broj koji želite da pretražite
  numberList = input("Unesite cijeli broj(od 1 do 10): ")

  # Pretražite element koristeći indeksnu metodu
  search_pos = int(numberList.index(numberList))

  # Printanje pronađenog broja
  print("%s broj je pronađen u listi" %(numberList))
except(ValueError):
  # Printanje ako broj ne postoji u nizu
  print("%s broj nije pronađen u listi" %(numberList))
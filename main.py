import datetime

from Device import *
from Receipt import *

receipts = []

while True:

    full_name = input("Введите ФИО: ")
    device = input("Выберете тип техники: телефон, ноутбук, телевизор ")
    crash = input("Опишите поломку: ")
    model = input('Укажите модель: ')

    if device == 'телефон':
        os = input('Операционная система: ')
        device = Phone(model, crash, os)

    if device == 'ноутбук':
        os = input('Операционная система: ')
        year = input('Год выпуска ноутбука: ')
        device = Laptop(model, os, year, crash)

    if device == 'телевизор':
        diagonal = input('Укажите диагональ телевизора: ')
        device = TV(model, crash, diagonal)

    receipt = Receipt(full_name, device)
    receipts.append(receipt)
    for r in receipts:
        r.print_info()

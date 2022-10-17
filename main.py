import datetime

from Device import *
from Receipt import *

receipts = []
receipt_number = 0
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
    receipt_number += 1
    receipt = Receipt(full_name, device, receipt_number)
    receipts.append(receipt)
    for r in receipts:
        r.print_info()

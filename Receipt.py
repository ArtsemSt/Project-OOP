import datetime
import random


class Receipt(object):

    def __init__(self, customer, device, receipt_number):
        self.receipt_number = receipt_number
        self.customer = customer
        self.device = device

    def print_info(self):
        print("-----------------")
        print("Номер Квитанции: ", self.receipt_number)
        print("ФИО: " + self.customer)
        print(datetime.date.today())
        print("Время ремонта: ", random.randint(1, 5), "дн")
        self.device.print_info()
        print("-----------------")

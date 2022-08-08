import datetime
import random


class Receipt(object):

    def __init__(self, customer, device):
        self.id = "123"
        self.customer = customer
        self.device = device

    def print_info(self):
        print("-----------------")
        print("Номер Чека: " + self.id)
        print("ФИО: " + self.customer)
        print(datetime.date.today())
        print("Время ремонта: ", random.randint(1, 5), "дн")
        self.device.print_info()
        print("-----------------")

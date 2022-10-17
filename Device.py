class Device():

    def __init__(self, model, crash):
        self.model = model
        self.crash = crash

    def print_info(self):
        print("Модель: " + self.model)
        print("Поломка: " + self.crash)


class Phone(Device):
    def __init__(self, model, crash, os):
        super().__init__(model, crash)
        self.os = os

    def print_info(self):
        super().print_info()
        print("Операционная система: " + self.os)


class Laptop(Device):
    def __init__(self, model, os, year, crash):
        super().__init__(model, crash)
        self.os = os
        self.year = year

    def print_info(self):
        super().print_info()
        print("Операционная система: " + self.os)
        print("Год выпуска ноутбука: " + self.year)


class TV(Device):
    def __init__(self, model, crash, diagonal):
        super().__init__(model, crash)
        self.diagonal = diagonal

    def print_info(self):
        super().print_info()
        print("Диагональ экрана: " + self.diagonal)

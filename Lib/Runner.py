from Lib import functions
from Lab_1.Lab1 import Lab1
from Lab_2.Lab2 import Lab2
from Lab_3.Lab3 import Lab3
from Lab_4.Lab4 import Lab4
from Lab_5.Lab5 import Lab5
from Lab_6.Lab6 import Lab6
from Lab_7.Lab7 import Lab7
from Lab_8.Lab8 import Lab8

class Runner:
    def __init__(self):
        self.labs = {
            "1": Lab1(),
            "2": Lab2(),
            "3": Lab3(),
            "4": Lab4(),
            "5": Lab5(),
            "6": Lab6(),
            "7": Lab7(),
            "8": Lab8(),
            # Додайте всі лабораторні роботи.
        }

    def run_lab(self, lab_number: str):
        if lab_number in self.labs:
            self.labs[lab_number].execute()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def show_menu(self):
        print("Оберіть лабораторну роботу для запуску:")
        for number in self.labs:
            print(f" {number} - Лабораторна робота {number}")
        print(" 0 - Вийти")
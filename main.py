class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"Человек {self.name} сейчас спит")
        self.endurance += 2

    def eat(self):
        print(f"Человек {self.name} кушает")
        self.power += 1

    def hit(self):
        print(f"Человек {self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"Человек {self.name} гулет")

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Сила воина - {self.power}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"ВЫносливость воина - {self.endurance}")



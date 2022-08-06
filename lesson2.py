class Car:
    def __init__(self, color, price, age, max_speed):
        self.color = color
        self.price = price
        self.age = age
        self.max_speed = max_speed

    def __str__(self):
        return 'Цвет машины - ' + self.color + '\nЦена машины - ' + str(self.price) + '\nВозраст машины - ' + str(self.age) + '\nМаксимальная скорость - ' + str(self.max_speed)
    
    def __eq__(self, other):
        if self.color == other.color and self.price == other.price:
            return True
        else:
            return False

    def __add__(self, other):
        color = 'black'
        price = self.price + other.price
        age = self.age + other.age
        max_speed = self.max_speed + other.max_speed
        return Car(color, price, age, max_speed)
    
    def __neg__(self):
        color = self.color
        price = - self.price
        age = self.age
        max_speed = self.max_speed
        return Car(color, price, age, max_speed)

car1 = Car('red', 2000000, 2, 185)
car2 = Car('red', 2000000, 1, 200)
print(- car1)

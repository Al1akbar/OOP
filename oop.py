class Car:
    def __init__(self, color, price, owner):
        self.color = color
        self.price = price
        self.owner = owner
    @property
    def color(self):
        return self.__dict__['color']
    @property
    def price(self):
        return self.__dict__['price']
    @property
    def owner(self):
        return self.__dict__['owner']
    @color.setter
    def color(self, newcolor):
        self.__dict__['color'] = newcolor
        print(f"\nRang {newcolor}ga o'zgartirildi!")
    @price.setter
    def price(self, newprice):
        self.__dict__['price'] = newprice
        print(f"Narxi {newprice}ga o'zgartirildi!")
    @owner.setter
    def owner(self, newowner):
        self.__dict__['owner'] = newowner
        print(f"Ega {newowner}ga o'zgartirildi!")

car = Car(color="Qora", price="500.000UZS", owner="Ali")
# print(car.__dict__)
print(f"\nMashina rangi: {car.color}\nMashina narxi: {car.price}\nMashina egasi: {car.owner}")

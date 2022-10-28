
# class Stuent:
#     name = 'John'

#     def __init__(self, name):
#         self.name = name

#     def __str__(self) -> str:
#         return self.name

#     def course(self):
#         return 'DME'


# Kuy = Stuent('Bond')
# print(Student.course())
# Cap = Stuent('Game')
# print(Cap.name)

'''
1. Create a class called Car
2. Create 2 attributes: brand, model
3. Create 1 private attribute: __price
4. Create 2 methods: get_brand(), get_model()
5. Create 1 private method: __get_price()
6. Create 1 object: car1
7. Print the brand and model of car1
8. Print the price of car1
'''


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def __get_price(self):
        return self.__price

    def get_price(self):
        return self.__get_price()


if __name__ == '__main__':
    car1 = Car('Toyota', 'Camry', 1000000)
    print(f'Car1: {car1.get_brand()} {car1.get_model()}')
    print(f'Price: {car1.get_price()}')

# Write a program to create a class called Car which is abstract class
'''Follow this requirements:
1. Create a class called Car which is abstract class
2. Create 2 attributes: brand, model
3. Create 2 methods: get_brand(), get_model()
4. Create subclass called Toyota
5. Create 2 attributes: brand, model
6. Create 2 methods: get_brand(), get_model()
7. Create subclass called Honda
8. Create 2 attributes: brand, model
9. Create 2 methods: get_brand(), get_model()
10. Create 2 objects: car1, car2
11. Print the brand and model of car1 and car2
'''

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def get_brand(self):
        pass

    @abstractmethod
    def get_model(self):
        pass


class Toyota(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model


class Honda(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model


if __name__ == '__main__':
    car1 = Toyota('Toyota', 'Camry')
    car2 = Honda('Honda', 'Civic')
    print(f'Car1: {car1.get_brand()} {car1.get_model()}')
    print(f'Car2: {car2.get_brand()} {car2.get_model()}')

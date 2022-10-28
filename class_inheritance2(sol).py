# Write a program to create a class called People with the following attributes:
'''Follow this requirements:
1. Create a class called People
2. Create 2 attributes: name, age
3. Create 2 methods: get_name(), get_age()
4. Create subclass called Knight
5. Create 4 attributes: name, age, weapon, armor
6. Get the name, age, weapon, armor of Knight from user
7. Create 4 methods: get_name(), get_age(), get_weapon(), get_armor()
8. Create subclass called Wizard
9. Create 4 attributes: name, age, spell, wand
10. Get the name, age, spell, wand of Wizard from user
11. Create 4 methods: get_name(), get_age(), get_spell(), get_wand()
12. Make choice to create Knight or Wizard
13. If choice is Knight, create Knight object and print the name, age, weapon, armor of Knight
14. If choice is Wizard, create Wizard object and print the name, age, spell, wand of Wizard'''


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Knight(People):
    def __init__(self, name, age, weapon, armor):
        super().__init__(name, age)
        self.weapon = weapon
        self.armor = armor

    def get_weapon(self):
        return self.weapon

    def get_armor(self):
        return self.armor


class Wizard(People):
    def __init__(self, name, age, spell, wand):
        super().__init__(name, age)
        self.spell = spell
        self.wand = wand

    def get_spell(self):
        return self.spell

    def get_wand(self):
        return self.wand


if __name__ == '__main__':
    print('Choose your character:')
    choice = input('Knight or Wizard? (spell it correctly): ')
    if choice == 'Knight':
        name = input('Enter name: ')
        age = input('Enter age: ')
        weapon = input('Enter weapon: ')
        armor = input('Enter armor: ')
        knight1 = Knight(name, age, weapon, armor)
        print(knight1.get_name())
        print(knight1.get_age())
        print(knight1.get_weapon())
        print(knight1.get_armor())
    elif choice == 'Wizard':
        name = input('Enter name: ')
        age = input('Enter age: ')
        spell = input('Enter spell: ')
        wand = input('Enter wand: ')
        wizard1 = Wizard(name, age, spell, wand)
        print(wizard1.get_name())
        print(wizard1.get_age())
        print(wizard1.get_spell())
        print(wizard1.get_wand())
    else:
        print('Invalid choice!')

# Write an object oriented program that performs the following tasks:
# 1. Create a class called Chair from the base class Furniture
# 2. Teakwood should be the tpe of furniture that is used by all furnitures by default
# 3. The user can be given an option to change the type of wood used for the chair if they wish to
# 4. The number of legs a chair should be a property that should not be altered outside the class


class Furniture:
    def __init__(self):
        self.furniture_material = "Teakwood"


class Chair(Furniture):
    def __init__(self):
        self.__number_of_legs = 4

    def chair_material(self, material):
        self.material = material

    def chair_statement(self):
        print(
            f"This chair will be made of {self.material} and will have {self.__number_of_legs} legs.")


furniture = Furniture()
chair = Chair()
change_material = input(
    f"Would you like to change the chair material from {furniture.furniture_material}? (y/n): ")
if change_material == "y":
    new_material = input("Please specify which material you would like: ")
    chair.chair_material(new_material)

chair.chair_statement()

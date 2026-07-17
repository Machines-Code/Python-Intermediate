# Project to practice Python OOP further. Now introducing the following concepts:
# 1. Mixins
# 2. @property objects

# Task - Simulate a small zoo. A zookeeper can add animals to the zoo, list all animals currently in the zoo, feed a specific animal, feed every animal at once, and view an animal's details (name, species, hunger level, sound it makes)
# For the purposes of this task and focusing on the understanding of concepts, I will not be including input validation, duplicate name handling/bad menu choices/non-numeric input

# Came across the concept of "introspection at runtime". Hasn't been used here, but definitely something to look into in future

from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, hunger_level):
        self.hunger_level = hunger_level

    # Learn more about property getters and property setters
    @property
    def _hunger(self):
        return self.hunger_level

    @_hunger.setter
    def _hunger(self, new_hunger_level):
        self.hunger_level = new_hunger_level

    @abstractmethod
    def dietary_classication(self):
        return ""

    @abstractmethod
    def make_sound(self):
        return ""

    @abstractmethod
    def species(self):
        return ""


class SwimmableMixin:

    def swim(self):
        pass


class FlyableMixin:

    def fly(self):
        pass


class Mammal(Animal):

    required_fields = ["name", "weight", "fur_colour"]

    def __init__(self, name, weight, fur_colour):
        self.name = name
        self.weight = weight
        self.fur_colour = fur_colour


class Bird(Animal):

    required_fields = ["name", "weight", "wingspan"]

    def __init__(self, name, weight, wingspan):
        self.name = name
        self.weight = weight
        self.wingspan = wingspan


class Reptile(Animal):

    required_fields = ["name", "weight", "scale_texture"]

    def __init__(self, name, weight, scale_texture):
        self.name = name
        self.weight = weight
        self.scale_texture = scale_texture


class Lion(Mammal):

    required_fields = Mammal.required_fields.copy() + ["canine_length"]

    def __init__(self, name, weight, fur_colour, canine_length):
        super().__init__(name, weight, fur_colour)
        self.canine_length = canine_length

    def eat(self, new_hunger_level):
        Animal._hunger.fset(self, new_hunger_level)

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Roar"

    def species(self):
        return "Lion"


class Otter(Mammal, SwimmableMixin):

    required_fields = Mammal.required_fields.copy() + ["tail_length"]

    def __init__(self, name, weight, fur_colour, tail_length):
        super().__init__(name, weight, fur_colour)
        self.tail_length - tail_length

    def eat(self):
        pass

    def dietary_classication(self):
        "Carnivore"

    def make_sound(self):
        return "Squeek"

    def species(self):
        return "Otter"

    def swim(self):
        pass


class Penguin(Bird, SwimmableMixin):

    required_fields = Bird.required_fields.copy() + ["waddle_speed"]

    def __init__(self, name, weight, wingspan, waddle_speed):
        super().__init__(name, weight, wingspan)
        self.waddle_speed = waddle_speed

    def eat(self):
        pass

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Honk"

    def species(self):
        return "Penguin"

    def swim(self):
        pass


class Owl(Bird, FlyableMixin):

    required_fields = Bird.required_fields.copy() + ["flight_sound_level_db"]

    def __init__(self, name, weight, wingspan, flight_sound_level_db):
        super().__init__(name, weight, wingspan)
        self.flight_sound_level_db = flight_sound_level_db

    def eat(self):
        pass

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Screech"

    def species(self):
        return "Owl"

    def fly(self):
        pass


class Ostrich(Bird):

    required_fields = Bird.required_fields.copy() + ["run_speed"]

    def __init__(self, name, weight, wingspan, run_speed):
        super().__init__(name, weight, wingspan)
        self.run_speed = run_speed

    def eat(self):
        pass

    def dietary_classication(self):
        return "Omnivore"

    def make_sound(self):
        return "Boom"

    def species(self):
        return "Ostrich"


class Snake(Reptile):

    required_fields = Reptile.required_fields.copy() + ["poison_level"]

    def __init__(self, name, weight, scale_texture, poison_level):
        super().__init__(name, weight, scale_texture)
        self.poison_level = poison_level

    def eat(self):
        pass

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Snake"


class Crocodile(Reptile, SwimmableMixin):

    required_fields = Reptile.required_fields.copy() + ["bite_force_N"]

    def __init__(self, name, weight, scale_texture, bite_force_N):
        super().__init__(name, weight, scale_texture)
        self.bite_force_N = bite_force_N

    def eat(self):
        pass

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Crocodile"

    def swim(self):
        pass


class Komodo(Reptile):

    required_fields = Reptile.required_fields.copy() + ["venom_strength"]

    def __init__(self, name, weight, scale_texture, venom_strength):
        super().__init__(name, weight, scale_texture)
        self.venom_strength = venom_strength

    def eat(self):
        pass

    def dietary_classication(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Komodo Dragon"


class Zoo:

    _animal_list = {}

    def __init__(self):
        self.menu_options = {
            "1": ("Add an animal", self.add_animal),
            "2": ("List all animals", self.list_animals),
            "3": ("Feed a specific animal", self.feed_animal),
            "4": ("Feed all animals", self.feed_all),
            "5": ("View an animal's details", self.view_animal_details),
            "6": ("Exit", self.handle_exit)
        }

        self.animal_options = {
            "1": ("Lion", Lion),
            "2": ("Otter", Otter),
            "3": ("Penguin", Penguin),
            "4": ("Owl", Owl),
            "5": ("Ostrich", Ostrich),
            "6": ("Snake", Snake),
            "7": ("Crocodile", Crocodile),
            "8": ("Komodo Dragon", Komodo)
        }

    def show_menu(self):

        for number, (label, _) in self.menu_options.items():
            print(f"{number}. {label}")

    def add_animal(self):

        for key, (label, _) in self.animal_options.items():
            print(f"{key}. {label}")

        animal_choice = int(input("Pick an animal from the list: "))
        animal_description, animal_class = self.animal_options[animal_choice]

        animal_name = str(
            input(f"What is the name of the {animal_description}?: "))

        animal_class_details = {"name": animal_name}

        for field in animal_class.required_fields:
            print(field.replace("_", " ").capitalize())
            animal_class_details[field] = str(input())

        animal_class_details["Hunger Level"] = 1

        # New technique learned with ** - unpacks a dictionary, allow you to use key-value pairs as arguments/parameters for functions and classes. Cool!
        new_animal = animal_class(**animal_class_details)
        Zoo._animal_list[new_animal.name] = new_animal
        return new_animal

    def list_animals(self):

        for field, entry in Zoo._animal_list.items():
            print(f"{field}. {entry}")

# Continue getting the feeding system right. Set hunger_level = 1 at animal creation, and set it to 0 after feeding
    def feed_animal(self):

        for name, _ in self._animal_list.items():
            print(f"{name}\n")

        animal_name = str(
            input("Enter the name of the animal you would like to feed: "))

        Zoo._animal_list[animal_name].eat(0)

        print(f"{animal_name} has been fed.")

    def feed_all(self):
        pass

    def view_animal_details(self):

        animal_name = str(
            input("Please enter the name of the animal you would like to inspect: "))

        animal_details = Zoo._animal_list[animal_name]

        for field, entry in animal_details.items():
            print(f"{field}: {entry}")

    def handle_exit(self):
        return True

    def run(self):

        while True:
            self.show_menu()

            zookeeper_selection = int(
                input("Select an option from the menu: "))
            _, action = self.menu_options[zookeeper_selection]
            result = action()
            if result:
                break


if __name__ == "__main__":
    zookeper_interaction = Zoo()
    zookeper_interaction.run()

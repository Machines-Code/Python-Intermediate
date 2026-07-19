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

    def eat(self):
        self._hunger = 0

    @abstractmethod
    def dietary_classification(self):
        return ""

    @abstractmethod
    def make_sound(self):
        return ""

    @abstractmethod
    def species(self):
        return ""


class SwimmableMixin:

    def swim(self):
        print(
            f"{self.name} has now gone for a swim around! But now they are hungry...")
        self.hunger_level = 1


class FlyableMixin:

    def fly(self):
        print(
            f"{self.name} has now gone for a flight around the enclosere! But now they are hungry...")
        self.hunger_level = 1


class Mammal(Animal):

    required_fields = ["weight", "fur_colour"]

    def __init__(self, name, weight, fur_colour, hunger_level):
        super().__init__(hunger_level)
        self.name = name
        self.weight = weight
        self.fur_colour = fur_colour


class Bird(Animal):

    required_fields = ["weight", "wingspan"]

    def __init__(self, name, weight, wingspan, hunger_level):
        super().__init__(hunger_level)
        self.name = name
        self.weight = weight
        self.wingspan = wingspan


class Reptile(Animal):

    required_fields = ["weight", "scale_texture"]

    def __init__(self, name, weight, scale_texture, hunger_level):
        super().__init__(hunger_level)
        self.name = name
        self.weight = weight
        self.scale_texture = scale_texture


class Lion(Mammal):

    required_fields = Mammal.required_fields.copy() + ["canine_length"]

    def __init__(self, name, weight, fur_colour, canine_length, hunger_level):
        super().__init__(name, weight, fur_colour, hunger_level)
        self.canine_length = canine_length

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Roar"

    def species(self):
        return "Lion"


class Otter(Mammal, SwimmableMixin):

    required_fields = Mammal.required_fields.copy() + ["tail_length"]

    def __init__(self, name, weight, fur_colour, tail_length, hunger_level):
        super().__init__(name, weight, fur_colour, hunger_level)
        self.tail_length = tail_length

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Squeek"

    def species(self):
        return "Otter"


class Penguin(Bird, SwimmableMixin):

    required_fields = Bird.required_fields.copy() + ["waddle_speed"]

    def __init__(self, name, weight, wingspan, waddle_speed, hunger_level):
        super().__init__(name, weight, wingspan, hunger_level)
        self.waddle_speed = waddle_speed

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Honk"

    def species(self):
        return "Penguin"


class Owl(Bird, FlyableMixin):

    required_fields = Bird.required_fields.copy() + ["flight_sound_level_db"]

    def __init__(self, name, weight, wingspan, flight_sound_level_db, hunger_level):
        super().__init__(name, weight, wingspan, hunger_level)
        self.flight_sound_level_db = flight_sound_level_db

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Screech"

    def species(self):
        return "Owl"


class Ostrich(Bird):

    required_fields = Bird.required_fields.copy() + ["run_speed"]

    def __init__(self, name, weight, wingspan, run_speed, hunger_level):
        super().__init__(name, weight, wingspan, hunger_level)
        self.run_speed = run_speed

    def dietary_classification(self):
        return "Omnivore"

    def make_sound(self):
        return "Boom"

    def species(self):
        return "Ostrich"


class Snake(Reptile):

    required_fields = Reptile.required_fields.copy() + ["poison_level"]

    def __init__(self, name, weight, scale_texture, poison_level, hunger_level):
        super().__init__(name, weight, scale_texture, hunger_level)
        self.poison_level = poison_level

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Snake"


class Crocodile(Reptile, SwimmableMixin):

    required_fields = Reptile.required_fields.copy() + ["bite_force_N"]

    def __init__(self, name, weight, scale_texture, bite_force_N, hunger_level):
        super().__init__(name, weight, scale_texture, hunger_level)
        self.bite_force_N = bite_force_N

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Crocodile"


class Komodo(Reptile):

    required_fields = Reptile.required_fields.copy() + ["venom_strength"]

    def __init__(self, name, weight, scale_texture, venom_strength, hunger_level):
        super().__init__(name, weight, scale_texture, hunger_level)
        self.venom_strength = venom_strength

    def dietary_classification(self):
        return "Carnivore"

    def make_sound(self):
        return "Hiss"

    def species(self):
        return "Komodo Dragon"


class Zoo:

    def __init__(self):
        self.menu_options = {
            "1": ("Add an animal", self.add_animal),
            "2": ("List all animals", self.list_animals),
            "3": ("Feed a specific animal", self.feed_animal),
            "4": ("Feed all animals", self.feed_all),
            "5": ("Take animals for a swim", self.take_swim),
            "6": ("Take animals for a fly around", self.take_flight),
            "7": ("View an animal's details", self.view_animal_details),
            "8": ("Exit", self.handle_exit)
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

        self._animal_list = {}

    def show_menu(self):

        for number, (label, _) in self.menu_options.items():
            print(f"{number}. {label}")

    def _select_animal(self, prompt):
        self.prompt = prompt

        for name in self._animal_list.keys():
            print(f"{name}\n")

        print(f"{self.prompt}")

    def add_animal(self):

        for key, (label, _) in self.animal_options.items():
            print(f"{key}. {label}")

        animal_choice = str(input("Pick an animal from the list: "))
        animal_description, animal_class = self.animal_options[animal_choice]

        animal_name = str(
            input(f"What is the name of the {animal_description}?: "))

        animal_class_details = {"name": animal_name}

        for field in animal_class.required_fields:
            print(field.replace("_", " ").capitalize())
            animal_class_details[field] = str(input())

        # New technique learned with ** - unpacks a dictionary, allow you to use key-value pairs as arguments/parameters for functions and classes. Cool!
        new_animal = animal_class(hunger_level=1, **animal_class_details)
        self._animal_list[new_animal.name] = new_animal
        return new_animal

    def list_animals(self):

        for field, entry in self._animal_list.items():
            print(f"{field}. {entry}")

    def feed_animal(self):

        self._select_animal(
            "Enter the name of the animal you would like to feed")

        animal_name = str(input())

        self._animal_list[animal_name].eat()

        print(f"{animal_name} has been fed.")

    def feed_all(self):
        for name, _ in self._animal_list.items():
            self._animal_list[name].eat()

        print("All the animals at the zoo have been fed")

    def take_swim(self):

        swim_choice = int(input(
            "Would you like to take all the animals for a swim (1) or one animal for a swim (2)?: "))

        if swim_choice == 1:
            for animal in self._animal_list.values():
                if hasattr(animal, "swim"):
                    animal.swim()
        elif swim_choice == 2:
            self._select_animal("Enter the name of the animal from the list")

            animal_name = str(input())
            self._animal_list[animal_name].swim()

    def take_flight(self):

        flight_choice = int(input(
            "Would you like to take all the animals for a fly around (1) or one animal for a fly around (2)?: "))

        if flight_choice == 1:
            for animal in self._animal_list.values():
                if hasattr(animal, "fly"):
                    animal.fly()
        elif flight_choice == 2:
            self._select_animal("Enter the name of the animal from the list")

            animal_name = str(input())
            self._animal_list[animal_name].fly()

    def view_animal_details(self):

        print("Current list of animals in the zoo:")
        self._select_animal("Enter the name of the animal from the list")

        animal_name = str(input())

        animal_details = vars(self._animal_list[animal_name])

        for field, entry in animal_details.items():
            print(f"{field.replace('_', ' ').capitalize()}: {entry}")

        print(
            f"Dietary classification: {self._animal_list[animal_name].dietary_classification()}")
        print(f"Sound: {self._animal_list[animal_name].make_sound()}")
        print(f"Species: {self._animal_list[animal_name].species()}")

    def handle_exit(self):
        return True

    def run(self):

        while True:
            self.show_menu()

            zookeeper_selection = str(
                input("Select an option from the menu: "))
            _, action = self.menu_options[zookeeper_selection]
            result = action()
            if result is True:
                break


if __name__ == "__main__":
    zookeper_interaction = Zoo()
    zookeper_interaction.run()

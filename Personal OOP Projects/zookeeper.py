# Project to practice Python OOP further. Now introducing the following concepts:
# 1. Mixins
# 2. @property objects

# Task - Simulate a small zoo. A zookeeper can add animals to the zoo, list all animals currently in the zoo, feed a specific animal, feed every animal at once, and view an animal's details (name, species, hunger level, sound it makes)
# For the purposes of this task and focusing on the understanding of concepts, I will not be including input validation, duplicate name handling/bad menu choices/non-numeric input


from abc import ABC, abstractmethod


class Animal(ABC):

    # Learn more about property getters and property setters
    @property
    def _hunger(self):
        self._hunger = 1
        return self._hunger

    @abstractmethod
    def eat(self):
        return 0

    @abstractmethod
    def dietary_classication(self):
        return ""

    @abstractmethod
    def make_sound(self):
        return ""

    @abstractmethod
    def weight(self):
        return 0

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

    @abstractmethod
    def fur_colour(self):
        return ""


class Bird(Animal):

    @abstractmethod
    def wingspan(self):
        return ""


class Reptile(Animal):

    @abstractmethod
    def scale_toughness(self):
        return ""


class Lion(Mammal):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def fur_colour(self):
        pass


class Otter(Mammal, SwimmableMixin):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def fur_colour(self):
        pass

    def swim(self):
        pass


class Penguin(Bird, SwimmableMixin):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def wingspan(self):
        pass

    def swim(self):
        pass


class Owl(Bird, FlyableMixin):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def wingspan(self):
        pass

    def fly(self):
        pass


class Ostrich(Bird):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def wingspan(self):
        pass


class Snake(Reptile):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def scale_toughness(self):
        pass


class Crocodile(Reptile, SwimmableMixin):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def scale_toughness(self):
        pass

    def swim(self):
        pass


class Komodo(Reptile):

    def eat(self):
        pass

    def dietary_classication(self):
        pass

    def make_sound(self):
        pass

    def weight(self):
        pass

    def species(self):
        pass

    def scale_toughness(self):
        pass


class Zoo:

    # Rethink how this dictionary works and how we set animal characteristics to it
    animal_list = {
        "1": "Lion",
        "2": "Otter",
        "3": "Penguin",
        "4": "Owl",
        "5": "Ostrich",
        "6": "Snake",
        "7": "Crocodile",
        "8": "Komodo Dragon"
    }

    def __init__(self):
        self.menu_options = {
            "1": ("Add an animal", self.add_animal),
            "2": ("List all animals", self.list_animals),
            "3": ("Feed a specific animal", self.feed_animal),
            "4": ("Feed all animals", self.feed_all),
            "5": ("View an animal's details", self.view_animal_details),
            "6": ("Exit", self.handle_exit)
        }

    def add_animal(self):
        pass

    def list_animals(self):
        pass

    def feed_animal(self, animal_name):
        pass

    def feed_all(self):
        pass

    def view_animal_details(self, animal_name):
        pass

    def handle_exit(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    zookeper_interaction = Zoo()
    zookeper_interaction.run()

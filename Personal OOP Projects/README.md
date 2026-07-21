# Personal OOP Projects

This folder contains projects I completed that have helped me practice Python OOP concepts and experiment with various techniques

The lessons and concepts learned in these projects are the following:

1. Abstraction - including ABCs, abstract methods, and property decorators
2. Multilevel inheritance
3. Multiple inheritance and Mixins
4. Polymorphism - method overriding and duck typing
5. Access specifiers
6. Encapsulation
7. Dict-based dispatch
8. Dynamic construction via **kwargs

The projects completed in this section are the following:

1. A zoo (zookeeper.py) program - A more complex program allowing a zookeeper to run and maintain a zoo of animals
    - Includes the following
        * An ABC (Animal) c/w with abstract methods (dietary_classification, make_sound, and species), a _hunger property, a _hunger property setter, and an eat method
        * Two mixins (SwimmableMixin and FlyableMixin) which would be used later to take certain animals out for some exercise. This exercise in turn would make those animals hungry
        * Mammal, Bird, and Reptile subclasses that inherit Animal as a parent class. These subclasses intitiate a "required_fields" list of animal prompts for later in the program when the zookeeper adds a new animal
        * Eight leaf classes (Lion, Otter, Penguin, Owl, ostrich, Snake, Crocodile, and Komodo), each inheriting their relevant animal type subclass (Mammal, Bird, or Reptile) as well as their mixins (Swimmable or Flyable) accordingly. These leaf classes copy "required_fields" from their parent classes and append new fields to the list.
        * Finally, a Zoo class, which handles the zookeeper interaction. This class contains "_animal_list" (a registry of all animals currently in the zoo, along with their details), a dict containing "animal_options" (each animal species) in the form of a dispatch table, and a menu for the zookeeper to interact with (menu_options) in the form of a dispatch table
        * Functionalities available to the zookeeper are the following:
            1. Add an animal (here is where "required_fields" is used to prompt the zookeeper for the relevant information about the animal being added)
            2. List all animals (prints a list of the animals currently in the zoo)
            3. Feed a specific animal (makes use of the eat() method in "Animal")
            4. Feed all animals
            5. Take animals for a swim (can either take 1 or all animals for a swim who have inherited the SwimmableMixin)
            6. Take animals for a fly around(can either take 1 or all animals for a fly around who have inherited the FlyableMixin)
            7. View an animal's details (shows a combination of inherent traits and inputted traits at time of adding an animal)
            8. Exit
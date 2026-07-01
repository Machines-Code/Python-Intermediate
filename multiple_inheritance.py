# Multiple inheritance

# Base class
class OperatingSystem:
    multitasking = True
    name = "Mac OS"

# Base class


class Apple:
    website = "www.apple.com"
    name = "Apple"

# Derived class


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print(
                f"This is a multitasking system. Visit {self.website} for more details.")
            print(f"Name: {self.name}")

# In the event that both base classes have an attribute with the same name, and that attribute is called in the derived class, the base class listed first in the derived class parentheses will be prioritised. In this case - OperatingSystem


macbook = MacBook()

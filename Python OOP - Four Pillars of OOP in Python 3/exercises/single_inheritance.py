# Single inheritance

class Apple:  # This is the base class
    manufacturer = "Apple Inc."
    contact_website = "www.apple.com/contact"

    def contact_details(self):
        print(f"To contact us, log on to {self.contact_website}")


class MacBook(Apple):  # This is the derived class
    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_details(self):
        print(
            f"This MacBook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}")

# Program will look to find self.manufacturer as an instance attribute within class Macbook, then as a class attribute within class MacBook, then look for it in its parent class - class Apple


macbook = MacBook()
macbook.manufacture_details()
macbook.contact_details()

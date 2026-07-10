class CarRental:

    def __init__(self):
        self.vehicleCatalogue = {
            "Hatchback": 30,
            "Sedan": 50,
            "SUV": 100
        }

    def fareDetails(self):
        print("Cost per day:")
        for car, price in self.vehicleCatalogue.items():
            print(f"{car}: ${price}")

    def calculateCost(self, car, days):
        self.car = car
        self.days = days
        self.rentalCost = self.vehicleCatalogue[self.car] * self.days

    def printCost(self):
        print(f"This car will cost you ${self.rentalCost}.00.")


class userInteraction:
    def __init__(self):
        self.menu_options = {
            1: ("Show fare details", self.handle_fareDetails),
            2: ("Rent a car", self.handle_carRental),
            3: ("Exit", self.handle_exit)
        }

    def show_menu(self):
        for options, (label, _) in self.menu_options.items():
            print(f"{options}: {label}")

    def handle_fareDetails(self):
        rental = CarRental()
        rental.fareDetails()

    def handle_carRental(self):
        carChoice = input(
            "What type of car would you like? (Hatchback, Sedan, or SUV): ")
        numberOfDays = int(
            input("How many days would you like to rent the car for?: "))

        rentalChoice = CarRental()
        rentalChoice.calculateCost(carChoice, numberOfDays)
        rentalChoice.printCost()

    @staticmethod
    def handle_exit():
        print("Thank you for using this service!")
        return True

    def run(self):
        while True:
            self.show_menu()
            try:
                selection = int(
                    input("Please select an option from the menu: "))
                if selection not in self.menu_options:
                    print("Invalid option.")
                else:
                    _, action = self.menu_options[selection]
                    result = action()
                    if result:
                        break
            except ValueError:
                print("Please enter a number.")


user_interaction = userInteraction()
user_interaction.run()

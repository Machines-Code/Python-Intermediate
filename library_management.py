class Library:
    def __init__(self):
        self.book_library = ["Harry Potter", "Lord of the Rings", "Wheel of Time"]

    def borrow_book(self, book_taken):
        self.book_library.remove(book_taken)

    def return_book(self, book_returned):
        self.book_library.append(book_returned)


class UserInteraction:

    def __init__(self):
        self.library = Library()
        self.menu_options = {
            1: ("See full library", self.handle_library),
            2: ("Borrow a book", self.handle_borrow),
            3: ("Return a book", self.handle_return),
            4: ("Exit", self.handle_exit)
        }

    def show_menu(self):
        for option, (label, _) in self.menu_options.items():
            print(f"{option}: {label}")

    def handle_library(self):
        current_library = ", ".join(self.library.book_library)
        print(current_library)

    def handle_borrow(self):
        while True:
            book_borrowed = input("Which book would you like to borrow?: ")
            if book_borrowed not in self.library.book_library:
                print("Please select a book that is available in the library.")
            else:
                self.library.borrow_book(book_borrowed)
                break

    def handle_return(self):
        while True:
            book_returned = input("Which book have you returned?: ")
            if book_returned in self.library.book_library:
                print("This book is already in the library.")
            else:
                self.library.return_book(book_returned)
                break

    @staticmethod
    def handle_exit():
        print("Thank you for using the library!")
        return True

    def run(self):
        while True:
            self.show_menu()
            try:
                selection = int(
                    input("Please select an option from the menu: "))
                if selection not in self.menu_options:
                    print("Please select an option from the menu.")
                else:
                    _, action = self.menu_options[selection]
                    result = action()
                    if result:
                        break
            except ValueError:
                print("Please select a number from the menu.")


library_experience = UserInteraction()
library_experience.run()

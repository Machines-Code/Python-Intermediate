# Python OOP - Four Pillars of OOP in Python 3

This folder contains the exercises and lessons from the short course "Python OOP - Four Pillars of OOP in Python"

The lessons and concepts learned in this course are the following:

1. Classes, attributes, methods, encapsulation & abstraction, and access specifiers
2. Inheritance: single, multilevel, and multiple (and the Diamond Problem)
3. Polymorphism, including method overriding and operator overloading
4. Dunder methods
5. Abstract Base Classes

3 projects were completed in this short course:

1. A car rental (car_rental.py) program - a simple OOP program allowing a user to rent a car
    - Includes 2 simple classes - one to handle car rental functionality, and one to handle user interaction
    - Class CarRental contains a car registry, and calculates rental price based on type of car and daily rate
    - Class userInteraction contains a dispatch table, providing the user with a menu, and executing a command based on user input

2. A library management system (library_management.py) program - a simple OOP program allowing a user to borrow and return books from a library
    - Includes 2 simple classes - one to handle the library of books, and the borrow and return functionalities, and one to handle user interaction
    - Class Library contains the list of books currently available, and allows for the borrowing and returning of books
    - Class UserInteraction contains a dispatch table providing the user with a menu, and executing a command based on user input

3. A banking system (banking_system.py) program - a more complex OOP program which functions like a bank
    - The original project given by the short course asked for a program to either login to a Savings account or create one. Upon creation of a new account, a random 5-digit account number should be given, and the user should be asked for an initial deposit. Additionally, the program should handle typical bank functions, such as withdraw, deposit, and view balance
    - This version of the project was very similar to a previous project I had done (atm_simulation.py), stored in my "python-fundamentals" repo. I also felt that the brief did not include some of the concepts we had been taught throughout this course.
    - Therefore, I made the following adjustments to the project brief:
        * When creating an account, the user would have a choice of 3 account types to create (Savings, Cheque, or Investment)
        * Each account type would function with slightly different rules, making the user's choice of account meaningful
        * Although small, these changes made the use of an abstract base class, abstract methods, and inheritance relevant and meaningful.
    - Includes the following:
        * class Account (ABC) c/w get_balance and deposit methods, withdraw and account_type abstract methods, and a generate_account_number class method
        * separate classes for Savings_Account, Cheque_Account, and Investment_Account, each with similar functionalities, but differing slightly in interest rates, withdraw periods, and overdraft limits
        * access_account function - handles the process of logging in, and check balance, deposit, and withdraw
        * create_account function - handles the process of account creation
        * user_interaction function - handles initial menu to login, create account, or exit


Overall, this course was very functional and I feel that I learned valuable skills and came to grips with some core concepts of OOP in Python. These are skills I will definitely take forward with me as I progress in my learning.
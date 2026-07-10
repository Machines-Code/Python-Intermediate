# Public vs Protected vs Private

# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car:
    number_of_wheels = 4
    _colour = "Black"
    __year_of_manufacture = 2017  # Internally, this attribute is being stored as _Car__year_of_manufacture, that's why it can't be used later. You need to preface it with "_Car" to use it


class BMW(Car):
    def __init__(self):
        print(f"Protected attribute colour: {self._colour}.")


car = Car()
print(f"Public attribute number_of_wheels: {car.number_of_wheels}.")
bmw = BMW()
print(
    f"Private attribute year_of_manufacture: {car._Car__year_of_manufacture}.")

# Name mangling on private members:
# __variableName => _ClassName__variableName

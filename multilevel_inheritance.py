class musical_instruments:
    number_of_major_keys = 12


class string_instruments(musical_instruments):
    type_of_wood = "Tonewood"


class Guitar(string_instruments):
    def __init__(self):
        self.number_of_strings = 6
        print(
            f"This guitar consists of {self.number_of_strings} strings, is made of {self.type_of_wood}, and it can play {self.number_of_major_keys} major keys.")


guitar = Guitar()

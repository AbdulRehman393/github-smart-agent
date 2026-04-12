
class Car:
    def __init__(self, model, year, color, for_sale):        # to create car object, we need special type of method called constructor.
        self.model = model                                   # self is already provided to us, self means this object we are creating right now
        self.year = year                                     # means Store the given model and year inside this object.
        self.color = color
        self.for_sale = for_sale

    def drive(self):                                     # self is going to be provided to us
            print(f"You drive the {self.color} {self.model}")

    def stop(self):
            print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")





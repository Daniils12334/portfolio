class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self. colour = colour
        self. for_sale = for_sale

    def drive(self):
        print(f"You drive a {self.colour} {self.model}")

    def stop(self):
        print(f"Youve stopped the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.model} {self.year}, {self.colour},{self.for_sale}")
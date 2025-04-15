#QUESTION 1

class SetBook:
    def __init__(self, title, author, year, themes):
        self.title = title
        self.author = author
        self.year = year
        self.themes = themes

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.year}). Themes: {', '.join(self.themes)}"

class SwahiliSetBook(SetBook):
    def __init__(self, title, author, year, themes, summary):
        super().__init__(title, author, year, themes)
        self.__summary = summary  # Private attribute for encapsulation

    def get_summary(self):
        return f"Summary: {self.__summary}"

    def describe(self):  # Method override for polymorphism
        return f"Swahili Set Book: '{self.title}' by {self.author}. Themes: {', '.join(self.themes)}"

# Example instance with the book *Kidagaa Kimemwozea*
book1 = SwahiliSetBook("Kidagaa Kimemwozea", "Ken Walibora", 2005, ["Uongozi mbaya", "Ufisadi", "Utu"], 
                       "A story of betrayal, corruption, and the struggle for justice.")

# Testing methods
print(book1.describe())
print(book1.get_summary())


#QUESTION 2
class Vehicle:
    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for vehicle in vehicles:
    print(vehicle.move())

# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.__city = city  # Encapsulated (private attribute)

    def show_details(self):
        print(f"Hero: {self.name} | Power: {self.power} | City: {self.__city}")

    def protect_city(self):
        print(f"{self.name} is protecting {self.__city} using {self.power}!")

# Derived class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, wingspan):
        super().__init__(name, power, city)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} meters!")


# Example usage
if __name__ == "__main__":
    hero1 = FlyingHero("SkyWing", "Wind Control", "AeroCity", 15)
    hero1.show_details()
    hero1.fly()
    hero1.protect_city()

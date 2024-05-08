# Create add method to add two countries together.
# This method should create another country object with the name of the two countries
# combined and the population of the two countries added together.

# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia.add(herzegovina)
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    
    def add(self, county):
        new_name = f"{self.name} {county.name}"
        new_population = self.population + county.population
        return Country(new_name, new_population)
    
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(f"New country name: {bosnia_herzegovina.name}")
print(f"Population in the {bosnia_herzegovina.name}: {bosnia_herzegovina.population}")

        

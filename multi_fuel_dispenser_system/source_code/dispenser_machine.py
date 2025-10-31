from fuel import Fuel
class DispenserMachine:
    def __init__(self):
        self.fuels = {}

    def get_available_fuel(self):
        for name, fuel in self.fuels.items():
            return {
                name: {
                    "quantity": fuel.available_quantity,
                    "price": fuel.price_per_unit
                 }
            }

        return None

    def dispense_fuel(self, fuel_name, quantity):
        if fuel_name not in self.fuels:
            raise ValueError(f"{fuel_name} not available.")

        fuel = self.fuels[fuel_name]

        if fuel.available_quantity < quantity:
            raise ValueError(f"Not enough {fuel_name} in stock.")

        fuel.dispense(quantity)
        cost = fuel.price_per_unit * quantity
        return cost

    def add_fuel(self, fuel: Fuel):
        if not isinstance(fuel, Fuel):
            raise TypeError("Only Fuel objects can be added")
        if fuel in self.fuels:
            raise ValueError(f"{fuel} already added.")

        self.fuels[fuel.name] = fuel

    def update_fuel_price(self, fuel_name, new_price):
        if not isinstance(new_price, float):
            raise ValueError("New price must be a float")
        if not isinstance(fuel_name, str):
            raise ValueError("Fuel name must be a string")

        if fuel_name not in self.fuels:
            raise ValueError(f"{fuel_name} not found in dispenser.")

        fuel = self.fuels[fuel_name]

        fuel.price_per_unit = new_price

        return f"{fuel_name} price updated to ₦{fuel.price_per_unit}"




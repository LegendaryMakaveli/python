from fuel import Fuel

class FuelAttendant:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Attendant's name must be a string")
        self._name = value

    def update_fuel_price(self, machine, fuel_name, new_price):
        if not isinstance(fuel_name, str):
            raise ValueError("fuel_name must be a string")
        if not isinstance(new_price, float):
            raise ValueError("new_price must be a float")
        return machine.update_fuel_price(fuel_name, new_price)

    def add_new_fuel(self, machine, fuel_name, price_per_unit, initial_quantity):
        if not isinstance(fuel_name, str):
            raise TypeError("fuel_name must be a string")
        if not isinstance(price_per_unit, float):
            raise ValueError("price_per_unit must be a float")
        if not isinstance(initial_quantity, float):
            raise ValueError("initial_quantity must be a float")

        if fuel_name in machine.fuels:
            raise ValueError("fuel_name already exists")

        new_fuel = Fuel(fuel_name, price_per_unit, initial_quantity)
        return machine.add_fuel(new_fuel)

class Fuel:
    def __init__(self, name, price_per_unit, available_quantity):
        self.name = name
        self.price_per_unit = price_per_unit
        self.available_quantity = available_quantity


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not(isinstance(value, str)):
            raise TypeError("The name must be a string")
        self._name = value

    @property
    def price_per_unit(self):
        return self._price_per_unit

    @price_per_unit.setter
    def price_per_unit(self, value):
        if not isinstance(value, float):
            raise TypeError("The price_per_unit must be a float")
        self._price_per_unit = value

    @property
    def available_quantity(self):
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, value):
        if not isinstance(value, float):
            raise ValueError("The available_quantity must be a float")
        self._available_quantity = value

    def dispense(self, quantity):
        if not isinstance(quantity, float):
            raise ValueError("The quantity must be a float")
        if self.available_quantity > quantity:
            self.available_quantity -= quantity
            return True
        else:
            return False

    def get_cost(self, quantity):
        if not isinstance(quantity, float):
            raise ValueError("The quantity must be a float")
            return self._price_per_unit * quantity

    def update_price(self, new_price):
        if not isinstance(new_price, int):
            raise ValueError("The new price must be a int")
        if new_price > 10:
            self._price_per_unit = new_price

    def restock(self, amount):
        if not isinstance(amount, float):
            raise ValueError("The amount must be a float")
        if amount >= 100:
            self._available_quantity += amount


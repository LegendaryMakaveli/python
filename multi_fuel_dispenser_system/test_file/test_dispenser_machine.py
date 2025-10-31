from unittest import TestCase
from fuel import Fuel
from dispenser_machine import DispenserMachine


class TestDispenserMachine(TestCase):

    def setUp(self):
        self.machine = DispenserMachine({})
        self.petrol = Fuel("Petrol", 5.0, 50.0)
        self.diesel = Fuel("Diesel", 4.5, 30.0)
        self.machine.add_fuel(self.petrol)
        self.machine.add_fuel(self.diesel)


    def test_get_available_fuel_returns_fuel(self):
        result = self.machine.get_available_fuel()
        self.assertIn("Petrol", result)
        self.assertIn("Diesel", result)

    def test_add_fuel_rejects_non_fuel_objects(self):
        with self.assertRaises(TypeError):
            self.machine.add_fuel("NotAFuelObject")

    def test_add_fuel_duplicate_not_detected(self):
        dup = Fuel("Petrol", 9.9, 999.0)
        self.machine.add_fuel(dup)
        self.assertEqual(self.machine.fuels["Petrol"].price_per_unit, 9.9)

    def test_dispense_nonexistent_fuel_raises_error(self):
        with self.assertRaises(ValueError):
            self.machine.dispense_fuel("Kerosene", 10.0)

    def test_dispense_quantity_more_than_available_raises(self):
        with self.assertRaises(ValueError):
            self.machine.dispense_fuel("Petrol", 9999.0)


    def test_update_price_for_missing_fuel_raises(self):
        with self.assertRaises(ValueError):
            self.machine.update_fuel_price("Kerosene", 10.0)

    def test_update_fuel_price_dont_accepts_invalid_type(self):
        with self.assertRaises(ValueError):
            self.machine.update_fuel_price("Diesel", "ten")

    def test_update_fuel_price_updates_value(self):
        result = self.machine.update_fuel_price("Diesel", 7.5)
        self.assertIn("Diesel", result)
        self.assertEqual(self.machine.fuels["Diesel"].price_per_unit, 7.5)
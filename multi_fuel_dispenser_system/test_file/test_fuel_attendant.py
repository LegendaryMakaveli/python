from unittest import TestCase
from fuel import Fuel
from dispenser_machine import DispenserMachine
from fuel_attendant import FuelAttendant


class TestFuelAttendant(TestCase):
    def setUp(self):
        self.machine = DispenserMachine({})
        self.attendant = FuelAttendant("Mary")

    def test_name_accepts_string(self):
        self.attendant.name = "John"
        self.assertEqual(self.attendant.name, "John")

    def test_name_setter_non_string(self):
        with self.assertRaises(ValueError):
            self.attendant.name = 12345

    def test_add_new_fuel_adds_to_machine(self):
        self.attendant.add_new_fuel(self.machine, "Diesel", 5.0, 100.0)
        self.assertIn("Diesel", self.machine.fuels)
        self.assertIsInstance(self.machine.fuels["Diesel"], Fuel)

    def test_add_new_fuel_rejects_non_string_name(self):
        with self.assertRaises(TypeError):
            self.attendant.add_new_fuel(self.machine, 123, 5.0, 100.0)

    def test_add_new_fuel_rejects_non_float_price(self):
        with self.assertRaises(ValueError):
            self.attendant.add_new_fuel(self.machine, "Diesel", 5, 100.0)

    def test_add_new_fuel_rejects_non_float_quantity(self):
        with self.assertRaises(ValueError):
            self.attendant.add_new_fuel(self.machine, "Diesel", 5.0, 100)

    def test_add_new_fuel_with_existing_fuel_raises(self):
        self.attendant.add_new_fuel(self.machine, "Petrol", 4.5, 200.0)
        with self.assertRaises(ValueError):
            self.attendant.add_new_fuel(self.machine, "Petrol", 4.5, 200.0)

    def test_update_fuel_price(self):
        self.attendant.add_new_fuel(self.machine, "Diesel", 5.0, 100.0)
        result = self.attendant.update_fuel_price(self.machine, "Diesel", 6.5)
        self.assertIn("updated", result)
        self.assertEqual(self.machine.fuels["Diesel"].price_per_unit, 6.5)

    def test_update_fuel_price_rejects_non_string_name(self):
        with self.assertRaises(ValueError):
            self.attendant.update_fuel_price(self.machine, 100, 6.0)

    def test_update_fuel_price_rejects_non_float_price(self):
        with self.assertRaises(ValueError):
            self.attendant.update_fuel_price(self.machine, "Diesel", 6)

    def test_update_price_for_missing_fuel_raises(self):
        with self.assertRaises(ValueError):
            self.attendant.update_fuel_price(self.machine, "Kerosene", 7.0)

    def test_numeric_string_inputs_rejected(self):
        with self.assertRaises(ValueError):
            self.attendant.add_new_fuel(self.machine, "Diesel", "5.0", 100.0)
        with self.assertRaises(ValueError):
            self.attendant.update_fuel_price(self.machine, "Diesel", "7.5")

from unittest import TestCase
from fuel import Fuel


class TestFuelEdgeCases(TestCase):
    def setUp(self):
        self.fuel = Fuel("Diesel", 5.0, 50.0)

    def test_name_rejects_non_string(self):
        with self.assertRaises(TypeError):
            self.fuel.name = 123

    def test_price_per_unit_rejects_int(self):
        with self.assertRaises(TypeError):
            self.fuel.price_per_unit = 10

    def test_available_quantity_rejects_int(self):
        with self.assertRaises(ValueError):
            self.fuel.available_quantity = 20

    def test_dispense_rejects_non_float(self):
        with self.assertRaises(ValueError):
            self.fuel.dispense(5)

    def test_dispense_more_than_available_returns_false_and_no_change(self):
        before = self.fuel.available_quantity
        result = self.fuel.dispense(100.0)
        after = self.fuel.available_quantity
        self.assertFalse(result)
        self.assertEqual(before, after)

    def test_get_cost_with_float_returns_none(self):
        result = self.fuel.get_cost(10.0)
        self.assertIsNone(result)

    def test_get_cost_rejects_non_float(self):
        with self.assertRaises(ValueError):
            self.fuel.get_cost(10)

    def test_update_price_rejects_non_int(self):
        with self.assertRaises(ValueError):
            self.fuel.update_price(12.0)

    def test_update_price_no_change_if_less_or_equal_10(self):
        before = self.fuel._price_per_unit
        self.fuel.update_price(8)
        after = self.fuel._price_per_unit
        self.assertEqual(before, after)

    def test_update_price_changes_and_type_becomes_int_when_above_10(self):
        self.fuel.update_price(12)
        self.assertEqual(self.fuel._price_per_unit, 12)
        self.assertIsInstance(self.fuel._price_per_unit, int)

    def test_restock_rejects_non_float(self):
        with self.assertRaises(ValueError):
            self.fuel.restock(150)

    def test_restock_does_nothing_when_amount_less_than_100(self):
        before = self.fuel._available_quantity
        self.fuel.restock(50.0)
        after = self.fuel._available_quantity
        self.assertEqual(before, after)

    def test_restock_adds_when_amount_ge_100(self):
        before = self.fuel._available_quantity
        self.fuel.restock(150.0)
        after = self.fuel._available_quantity
        self.assertEqual(after, before + 150.0)

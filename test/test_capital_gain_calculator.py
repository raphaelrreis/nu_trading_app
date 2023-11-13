import unittest
from decimal import Decimal
from calculator.capital_gain_calculator import CapitalGainCalculator

class TestCapitalGainCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CapitalGainCalculator()
        self.calculator.update_average_price(Decimal('10.00'), Decimal('10000'))

    def test_validate_sell_quantity_with_valid_quantity(self):
        self.calculator.total_quantity = Decimal('1000')
        self.calculator.validate_sell_quantity(Decimal('500'))

    def test_validate_sell_quantity_with_invalid_quantity(self):
        self.calculator.total_quantity = Decimal('1000')
        with self.assertRaises(ValueError):
            self.calculator.validate_sell_quantity(Decimal('1500'))

    def test_calculate_operation_value(self):
        operation_value = self.calculator.calculate_operation_value(Decimal('10.00'), Decimal('100'))
        self.assertEqual(operation_value, Decimal('1000'))

    def test_is_sale_exempt_below_limit(self):
        self.assertTrue(self.calculator.is_sale_exempt(Decimal('19000')))

    def test_is_sale_exempt_above_limit(self):
        self.assertFalse(self.calculator.is_sale_exempt(Decimal('21000')))

    def test_update_state_after_sale(self):
        self.calculator.total_quantity = Decimal('1000')
        self.calculator.total_cost_accumulated = Decimal('10000')
        self.calculator.update_state_after_sale(Decimal('500'))
        self.assertEqual(self.calculator.total_quantity, Decimal('500'))
        self.assertEqual(self.calculator.total_cost_accumulated, Decimal('5000'))

    def test_get_average_price(self):
        self.calculator.total_quantity = Decimal('1000')
        self.calculator.total_cost_accumulated = Decimal('10000')
        average_price = self.calculator.get_average_price()
        self.assertEqual(average_price, Decimal('10'))

    def test_reset(self):
        self.calculator.total_cost_accumulated = Decimal('10000')
        self.calculator.total_quantity = Decimal('1000')
        self.calculator.accumulated_loss = Decimal('500')
        self.calculator.reset()
        self.assertEqual(self.calculator.total_cost_accumulated, Decimal('0'))
        self.assertEqual(self.calculator.total_quantity, Decimal('0'))
        self.assertEqual(self.calculator.accumulated_loss, Decimal('0'))

    def test_buy_operation(self):
        self.calculator.update_average_price(Decimal('20.00'), Decimal('5000'))
        expected_average_price = self.calculator.total_cost_accumulated / self.calculator.total_quantity
        self.assertEqual(self.calculator.average_price, expected_average_price)

    def test_sell_operation_below_exemption_limit(self):
        tax_due = self.calculator.execute_sell_operation(Decimal('15.00'), Decimal('100'))
        self.assertEqual(tax_due, Decimal('0'))

    def test_sell_operation_above_exemption_limit(self):
        tax_due = self.calculator.execute_sell_operation(Decimal('15.00'), Decimal('2000'))
        expected_tax_due = self.calculator.calculate_tax_due(self.calculator.adjust_for_accumulated_loss(
            self.calculator.calculate_profit_or_loss(Decimal('15.00'), Decimal('2000'))
        ))
        self.assertEqual(tax_due, expected_tax_due)

    def test_reset_after_selling_all(self):
        self.calculator.execute_sell_operation(Decimal('20.00'), Decimal('10000'))
        self.assertEqual(self.calculator.total_quantity, Decimal('0'))
        self.assertEqual(self.calculator.total_cost_accumulated, Decimal('0'))
        self.assertEqual(self.calculator.accumulated_loss, Decimal('0'))

    def test_sell_more_than_available_raises_error(self):
        with self.assertRaises(ValueError):
            self.calculator.execute_sell_operation(Decimal('20.00'), Decimal('15000'))

if __name__ == '__main__':
    unittest.main()

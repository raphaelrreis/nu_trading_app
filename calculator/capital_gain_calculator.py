from decimal import Decimal, ROUND_DOWN


class CapitalGainCalculator:
    TAX_RATE = Decimal('0.20')
    EXEMPTION_LIMIT = Decimal('20000')

    def __init__(self):
        self.total_cost_accumulated = Decimal('0')
        self.total_quantity = Decimal('0')
        self.accumulated_loss = Decimal('0')

    def update_average_price(self, unit_cost, quantity):
        total_cost_of_new_shares = unit_cost * quantity
        self.total_cost_accumulated += total_cost_of_new_shares
        self.total_quantity += quantity
        self.average_price = self.total_cost_accumulated / self.total_quantity if self.total_quantity else Decimal('0')

    def calculate_tax_due(self, profit_after_loss):
        return (profit_after_loss * self.TAX_RATE).quantize(Decimal('1'), rounding=ROUND_DOWN)

    def calculate_profit_or_loss(self, unit_cost, quantity):
        average_price = self.total_cost_accumulated / self.total_quantity
        return (unit_cost - average_price) * quantity

    def apply_exemption_limit(self, operation_value):
        return operation_value <= self.EXEMPTION_LIMIT

    def adjust_for_accumulated_loss(self, profit_or_loss):
        if profit_or_loss > 0:
            profit_after_loss = max(profit_or_loss - self.accumulated_loss, Decimal('0'))
            self.accumulated_loss = Decimal('0') if profit_after_loss > 0 else self.accumulated_loss - profit_or_loss
            return profit_after_loss
        else:
            self.accumulated_loss += abs(profit_or_loss)
            return Decimal('0')

    def execute_sell_operation(self, unit_cost, quantity):
        self.validate_sell_quantity(quantity)
        operation_value = self.calculate_operation_value(unit_cost, quantity)

        if self.is_sale_exempt(operation_value):
            return Decimal('0')

        profit_or_loss = self.calculate_profit_or_loss(unit_cost, quantity)
        profit_after_loss = self.adjust_for_accumulated_loss(profit_or_loss)
        tax_due = self.calculate_tax_due(profit_after_loss)

        self.update_state_after_sale(quantity)

        return tax_due

    def validate_sell_quantity(self, quantity):
        if quantity > self.total_quantity:
            raise ValueError("Não é possível vender mais ações do que o disponível em carteira.")

    def calculate_operation_value(self, unit_cost, quantity):
        return unit_cost * quantity

    def is_sale_exempt(self, operation_value):
        return operation_value <= self.EXEMPTION_LIMIT

    def update_state_after_sale(self, quantity):
        average_price = self.get_average_price()
        self.total_quantity -= quantity
        self.total_cost_accumulated -= (average_price * quantity)
        if self.total_quantity == Decimal('0'):
            self.reset()

    def get_average_price(self):
        if self.total_quantity == 0:
            return Decimal('0')
        return self.total_cost_accumulated / self.total_quantity

    def reset(self):
        self.total_cost_accumulated = Decimal('0')
        self.total_quantity = Decimal('0')
        self.accumulated_loss = Decimal('0')

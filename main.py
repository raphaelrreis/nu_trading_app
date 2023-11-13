from calculator.capital_gain_calculator import CapitalGainCalculator
from utils.io_helpers import read_operations_from_file, write_output_to_file, print_json_to_stdout
from decimal import Decimal
import os

def main(input_file_path, output_file_path=None):
    data = read_operations_from_file(input_file_path)
    casos = data["casos"]

    for caso in casos:
        operations = caso["operacoes"]
        calculator = CapitalGainCalculator()
        tax_results = []

        for operation in operations:
            if operation['operation'] == 'buy':
                calculator.update_average_price(Decimal(operation['unit-cost']), Decimal(operation['quantity']))
                tax_results.append({"tax": 0})
            elif operation['operation'] == 'sell':
                tax = calculator.execute_sell_operation(Decimal(operation['unit-cost']), Decimal(operation['quantity']))
                tax_results.append({"tax": int(tax)})
            else:
                raise ValueError(f"Operação desconhecida: {operation['operation']}")

        if output_file_path:
            write_output_to_file(tax_results, output_file_path)
        else:
            print_json_to_stdout(tax_results)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'data', 'input', 'test_cases.json')
    output_path = os.path.join(current_dir, 'data', 'output', 'tax_results.json')

    main(input_path, output_path)

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\s\d+\.\d+\s'
    match = re.findall(pattern, text)
    for number in match:
        yield float(number)
    
def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")









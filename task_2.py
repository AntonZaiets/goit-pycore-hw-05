import re

# generator numbers
def generator_numbers(text):
    pattern = r"(?<=\s)\d+\.\d+(?=\s)"
    for match in re.finditer(pattern, text):
        yield float(match.group())

# sum all numbers
def sum_profit(text, func):
    total = 0
    for number in func(text):
        total += number
    return total


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)

print("Загальний дохід:",total_income)
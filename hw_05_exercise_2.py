import re


def generator_numbers(text: str):
    # Regex to find decimal numbers surrounded by spaces
    pattern = r"\b\d+\.\d+\b"

    # Iterate over all matches in the text
    for match in re.finditer(pattern, text):
        # Extract the numeric part (without surrounding spaces)
        number_str = match.group(1)

        # Convert to float and yield one number at a time
        yield float(number_str)


def sum_profit(text: str, func):
    # Create a generator of numbers from the text using the provided function
    numbers = func(text)

    # Sum all yielded numbers and return the total profit
    return sum(numbers)


# Example usage
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

# Calculate total income using the generator-based parser
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")  # 1351.46

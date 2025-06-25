import re
from functools import total_ordering
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """ Аналізує текст і повертає генератор дійсних чисел. """

    pattern = r"\b\d+\.\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group(0))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """ Підсумує числа, отримані від функції-генератора. """
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатками надходження 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

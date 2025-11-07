# test_calculator.py
from calculator import add_numbers

def test_add_positive_numbers():
    """Перевіряємо додавання позитивних чисел."""
    assert add_numbers(5, 3) == 8

def test_add_negative_numbers():
    """Перевіряємо додавання від'ємних чисел."""
    assert add_numbers(-1, -4) == -5

def test_add_zero():
    """Перевіряємо додавання з нулем."""
    assert add_numbers(100, 0) == 100

# Цей тест навмисно невірний, щоб перевірити, чи спрацьовує помилка
# def test_failing_example():
#     assert add_numbers(2, 2) == 5 # Це спричинить помилку

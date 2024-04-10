# calculator.py

def add(x, y):
    """Функция для сложения двух чисел."""
    return x + y

def subtract(x, y):
    """Функция для вычитания одного числа из другого."""
    return x - y

def multiply(x, y):
    """Функция для умножения двух чисел."""
    return x * y

def divide(x, y):
    """Функция для деления одного числа на другое."""
    if y == 0:
        raise ValueError("Деление на ноль невозможно.")
    return x / y

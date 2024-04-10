async def async_add(x, y):
    """Асинхронная функция для сложения двух чисел."""
    return x + y

async def async_subtract(x, y):
    """Асинхронная функция для вычитания одного числа из другого."""
    return x - y

async def async_multiply(x, y):
    """Асинхронная функция для умножения двух чисел."""
    return x * y

async def async_divide(x, y):
    """Асинхронная функция для деления одного числа на другое."""
    if y == 0:
        raise ValueError("Деление на ноль невозможно.")
    return x / y

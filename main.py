import asyncio
import calculator

async def main():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    while True:
        choice = input("Выберите операцию (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print("Результат сложения:", await calculator.async_add(num1, num2))
            elif choice == '2':
                print("Результат вычитания:", await calculator.async_subtract(num1, num2))
            elif choice == '3':
                print("Результат умножения:", await calculator.async_multiply(num1, num2))
            elif choice == '4':
                try:
                    print("Результат деления:", await calculator.async_divide(num1, num2))
                except ValueError as e:
                    print("Ошибка:", e)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    asyncio.run(main())

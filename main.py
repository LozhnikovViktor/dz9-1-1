def number_sequence(start, end, even=True):
    """
    Генератор чисел в заданном диапазоне [start, end].
    :param start: Начало диапазона (включительно)
    :param end: Конец диапазона (включительно)
    :param even: Если True - чётные, если False - нечётные
    """
    step = 2 if even else 1
    # Настраиваем стартовое значение в зависимости от четности/нечетности
    if even:
        first = start if start % 2 == 0 else start + 1
    else:
        first = start if start % 2 != 0 else start + 1

    current = first
    while current <= end:
        yield current
        current += step

def get_user_input():
    """Запрашивает у пользователя параметры для генерации последовательности"""
    print("Генератор последовательностей чисел")

    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))

            if start > end:
                print("Начало диапазона должно быть меньше или равно концу!")
                continue

            choice = input("Выберите тип чисел: 1 - Чётные, 2 - Нечётные, 3 - Все: ")
            if choice in ['1', '2', '3']:
                return start, end, choice == '1'
            else:
                print("Некорректный выбор. Попробуйте снова.")

        except ValueError:
            print("Пожалуйста, введите корректные числовые значения!")

def main():
    start, end, is_even = get_user_input()

    print(f"\nПоследовательность {'чётных' if is_even else 'нечётных' if not is_even else 'всех'} чисел от {start} до {end}:")
    sequence = number_sequence(start, end, is_even)

    for number in sequence:
        print(number, end=' ')
    print()  # Перевод строки в конце вывода

if __name__ == "__main__":
    main()

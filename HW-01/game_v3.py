"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Для поиска загаданного числа предлагается среднее значение
    диапазона, границы которого сужаются в зависимости от сравнения
    заданного числа с предлагаемым
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Число попыток:
    count = 1
    # Первичные границы диапазона:
    predict_min, predict_max = 0, 100
    # Первичное предлагаемое значение:
    predict = round((predict_min+predict_max)/2)

    # Цикл угадывания числа
    while number != predict:
        count += 1
        if number > predict:
            predict_min = predict
            predict = round((predict_min+predict_max)/2)
        elif number < predict:
            predict_max = predict
            predict = round((predict_min+predict_max)/2)

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)

"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
def random_predict1(number:int=1)->int:
    """Игра угадай число
    Компьютер сам загадывает и угадывает число.
    Установим нижнюю и верхнюю границы.
    Если загаданное число меньше предполагаемого, то сужаем круг поиска. Предполагаемое число становится верхней границейю
    Если загаданное число больше предполагаемого, то сужаем круг поиска. Предполагаемое число становится нижней грацей.
    Если загаданное число и предполагаемое равны, то мы нашли загаданное число.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count=0 #количество попыток
    min_number=1 
    max_number=101
    predict_number=np.random.randint(1,101)
    while True:
        if number > predict_number:
            count+=1
            min_number=predict_number
            predict_number=np.random.randint(min_number,max_number)
        if number < predict_number:
            count+=1
            max_number=predict_number
            predict_number=np.random.randint(min_number,max_number)
        if number == predict_number:
            break
    return count        

def score_game(random_predict1)->int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм.

    Args:
        random_predict1 (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls=[] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    
    random_array=np.random.randint(1,101,size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict1(number))
    score=int(np.mean(count_ls)) #находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')
    return(score)

# RUN
score_game(random_predict1)

import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number  = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
print(f'Количество попыток: {random_predict()}')
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид (начальная точка) для воспроизводимости
    np.random_array = np.random.randint(1,101, size = (1000)) # загадали список чисел
    
    for number in np.random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #находим среднее количество попыток
    print(f'Ваш алгоритм в среднем угадывает за {score} количество попыток')
    return score
#RUN
if__name__=='_main_':
    score_game(random_predict)
import numpy as np

# Сам угадывает число
def random_predict(number: int = 1) -> int:
    '''Рандомно угадываем число.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: количество попыток
    '''
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # от 1 до 100 включительно
        if number == predict_number:
            break
            
    return count

def score_game(random_predict) -> int:
    '''За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм.
    
    Args:
        random_predict (function): функция угадывания числа.
        
    Returns:
        int: среднее количество попыток
    '''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводимым
    random_array = np.random.randint(1, 101, size=(1000))  # загадали числа
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


# Пример запуска
score_game(random_predict)

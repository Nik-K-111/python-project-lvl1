# progression.py for scripts/brain_progression.py

import random
REGULATIONS = 'What number is missing in the progression?'
ROUNDS = 3


def current_game():
    progression_string = ''
    list_n = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    [a] = random.sample(list_n, 1)
    d = random.randint(3, 9)
    n = random.randint(1, 10)
    j = 10
    while j > 0:
        if j != n:
            progression_string = progression_string + str(a) + ' '
        else:
            correct_answer = a
            progression_string = progression_string + '.. '
        a = a + d
        j -= 1
    question = (f'{progression_string}')
    
    return question, correct_answer

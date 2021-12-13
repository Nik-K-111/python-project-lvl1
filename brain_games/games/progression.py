# progression.py for scripts/brain_progression.py

import random

REGULATIONS = 'What number is missing in the progression?'
ROUNDS = 3


def current_game():
    progression_string = ''
    NUMBER_OF_MEMBERS = 10
    list_1_term = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    [term] = random.sample(list_1_term, 1)
    difference = random.randint(3, 9)
    n_unknown_term = random.randint(1, 10)
    j = NUMBER_OF_MEMBERS
    while j > 0:
        if j != n_unknown_term:
            progression_string = progression_string + str(term) + ' '
        else:
            correct_answer = term
            progression_string = progression_string + '.. '
        term = term + difference
        j -= 1

    question = (f'{progression_string}')

    return question, correct_answer

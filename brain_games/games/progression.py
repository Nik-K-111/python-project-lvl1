# progression.py for scripts/brain_progression.py

import random

DESCRIPTION = 'What number is missing in the progression?'


def a_progression(first_term, num_term, difference):
    progression = [first_term, ]
    for i in range(1, num_term):
        progression = progression + [first_term + difference * i]
    return progression


def current_game():
    first_term = random.randint(3, 9)
    num_term = 10
    difference = random.randint(3, 15)
    num_x_term = random.randint(0, num_term - 1)

    progression = a_progression(first_term, num_term, difference)
    correct_answer = progression[num_x_term]

    question = ''
    for i in range(num_term):
        if i != num_x_term:
            question = question + str(progression[i]) + ' '
        else:
            question = question + '.. '

    return question, correct_answer

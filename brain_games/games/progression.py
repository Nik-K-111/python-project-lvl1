# progression.py for scripts/brain_progression.py


import prompt
import random
from brain_games.offer import acquaintance
from brain_games.checking import checking


def unknown_element():
    regulations = 'What number is missing in the progression?'
    name = acquaintance(regulations)
    final = ''
    i = 3
    while i > 0:
        i -= 1
        sequence_string = ''
        list_n = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
        [a] = random.sample(list_n, 1)
        d = random.randint(3, 9)
        n = random.randint(1, 10)
        j = 10
        while j > 0:
            if j != n:
                sequence_string = sequence_string + str(a) + ' '
            else:
                correct_answer = a
                sequence_string = sequence_string + '.. '
            a = a + d
            j -= 1

        print(f'Question: {sequence_string}')
        user_answer = prompt.integer('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)

    print(final)

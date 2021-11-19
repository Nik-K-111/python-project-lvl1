#! usr/bin/env python3

# checking.py - Оценка ответа игрока, выход на финал
# 4 аргумента: i, user_answer, correct_answer, name
# 2 результата: final, i


def checking(i, user_answer, correct_answer, name):
    if user_answer == correct_answer:
        final = (f"Congratulations, {name}!")

        if i > 0:
            print('Correct!')

    else:
        final = (
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\n"
            f"Let's try again, {name}!"
        )
        i = 0
    return final, i

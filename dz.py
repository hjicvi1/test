
import random

questions = ['Сколько будет два плюс два умноженое на два?',
            'Бревно нужно распилить на десять частей, сколько нужно  распилов?',
            'На двух руках 10 пальцев, сколько пальцев на 5 руках?',
            'Укол делают каждые полчаса, сколько нужно минут для трёх уколов?',
            'Пять свечей горело, две потухли. Сколько свечей осталось?']


answers = [6, 9, 25, 60, 2]

result = ['Идиот.', 'Кретин.', 'Дурак.', 'Нормальный.', 'Талант.', 'Гений.']

count_right_answers = 0

print('Напишите пожалуйста как вас зовут. Ваше имя?')
user_name = input()


def result_count_right_answers():
    return result[count_right_answers]

def question_namber():   

    # это конечно работает, но это очень плохая практика, функции должны быть универсальные.
    # допустим у тебя есть два списка вопросов, что тогда?
    # гораздо правильнее было new_order_questions, quesions, i получить в качестве параметров.
    y = int(new_order_questions[i])    
    # если мы выводим, то return не нужен.
    return print('Вопрос номер:', i + 1, questions[y])

def new_order_question():
    symbols = ['0', '1', '2', '3', '4']
    # индексы нового порядка лучше складывать в список. Вдруг у нас будет 20 вопросов, что тогда?
    new_order_questions = ''
    for k in range(5):
        random_index = random.randint(0, len(symbols) - 1)
        new_order_questions += symbols[random_index]
        symbols.pop(random_index) 
    return new_order_questions


while True:

    new_order_questions = new_order_question()
    
    for i in range(len(questions)):
        
        
        question_namber()
        user_answer = int(input())
        
        right_answer = answers[i]
        if user_answer == right_answer:
            count_right_answers += 1
    
    print('Количество правильных ответов =', count_right_answers, '. Да вы ', user_name, ' просто', result_count_right_answers())

    # и чтобы корректно завершать программу, лучше сделать так

    user_confirm = input('Вы хотите пройти тест еще раз? Да/Нет')
    if user_confirm.upper() == 'ДА':
        continue
    else:
        break
print("Good bye")

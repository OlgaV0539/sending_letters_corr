from typing import Tuple


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    symbol1 = '@'
    endings1 = ('.com', '.ru', '.net')
    flag_first = False
    if symbol1 in recipient:
        for i in endings1:
            if i in recipient:
                flag_first = True
    symbol2 = '@'
    endings2 = ('.com', '.ru', '.net')
    flag_second = False
    if symbol2 in sender:
        for i in endings2:
            if i in sender:
                flag_second = True

    if flag_first is False or flag_second is False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

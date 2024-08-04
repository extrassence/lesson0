def send_email(message, recipient ,* , sender='university.help@gmail.com'):
    domainr = recipient.rpartition('.')[-1]
    domains = sender.rpartition('.')[-1]
    is_not_emailr = (recipient.find('@') == -1)
    is_not_emails = (sender.find('@') == -1)
    if is_not_emails or is_not_emailr or (domainr not in ('ru', 'com', 'net')) or (domains not in ('ru', 'com', 'net')):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ',recipient)
    elif recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
    elif sender.lower() == 'university.help@gmail.com':
        # тут должно быть не только сообщение, но еще и отправка письма
        # success = sendletter(sender, recipient, message) # Если отправилось успешно, то возвращает True, например
        # if success:
        print('Письмо успешно отправлено с адреса university.help@gmail.com на адрес', recipient)
        # else какая-то реакция на проблемы с отправкой
    else:
        # тут должно быть не только сообщение, но еще и отправка письма
        # success = sendletter(sender, recipient, message)
        # if success:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес', recipient)
        # else какая-то реакция на проблемы с отправкой




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.ua')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='URBAN.teacher@mail.ru')
send_email('Как же там этот чертов адрес', 'urban.mail.ru', sender='urban.teacher@mail.ru')
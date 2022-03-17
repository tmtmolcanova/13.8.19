price_all = 0
while True:
    try:
        ticket_amount = input('Какое колличесво билетов вы приобретаете? ')
        ticket_amount = int(ticket_amount)
        if type(ticket_amount) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_amount):
    i += 1
    while True:
        try:
            age = input(f'Введите возраст посетителя №{i}? ')
            age = int(age)
            if age < 18:
                print('Стоимость билета: 0,00 руб.')
            elif 25 > age >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_amount > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Итого: {price_all} руб.')
else:
    print(f'Итого: {price_all} руб.')
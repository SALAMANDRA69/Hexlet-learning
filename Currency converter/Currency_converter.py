import freecurrencyapi

def get_quotes_currency(): 
    client = freecurrencyapi.Client('fca_live_7biV5oZKQwAkn7Ot9GMPTCuhAtnj6GxJ5DzI0BJt').latest()
    return client['data']
 
CURRENCIES = get_quotes_currency()

def main(currencies):
    action = None
    print('''ДОБРО ПОЖАЛОВАТЬ В КОНВЕРТ ВАЛЮТ!

1 - Список валют с ценами~
2 - Конверт валют
0 - Выход''')
    while action != '0':
        action = input('\nНажмите для просмотра: ')
        if action == '1':
            print('\nСПИСОК ВАЛЮТ С ЦЕНАМИ\n')
            for key in currencies:
                print(f'{key} = {round(currencies[key], 2)}')
        elif action == '2':
            print('\nКОНВЕРТ ВАЛЮТ\n')
            value_current_currency = input('Введите исходную валюту: ')
            current_currency = check_availability_currency(currencies, value_current_currency)
            value_result_currency = input('Введите результирующую валюту: ')
            result_currency = check_availability_currency(currencies, value_result_currency)
            amount = check_amount()
            result = convert_currency(currencies, amount, current_currency, result_currency)
            print(f'\n{amount} {current_currency} = {result} {result_currency}')
    print('\nДО НОВЫХ ВСТРЕЧ!')

def check_availability_currency(currencies, value_currency):
    while True:
        if value_currency in currencies:
            return value_currency
        print('\nОШИБКА. Такой валюты нет!')
        value_currency = input('\nВведите другую валюту: ')

def check_amount():
    while True:
        try:
            value_amount = input('Введите количество: ')
            value_amount = float(value_amount)
            return value_amount
        except ValueError:
            print('\nОШИБКА. Неверное значение!\n')

def convert_currency(currencies, amount, current_currency, result_currency):
    from_value = currencies.get(current_currency)
    to_value = currencies.get(result_currency)
    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

if __name__ == '__main__':
    main(CURRENCIES)

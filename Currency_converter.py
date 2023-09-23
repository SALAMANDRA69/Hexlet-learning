import freecurrencyapi

API_KEY = 'fca_live_7biV5oZKQwAkn7Ot9GMPTCuhAtnj6GxJ5DzI0BJt'

def getting_currency_quotes(): 
    client = freecurrencyapi.Client(API_KEY)
    result = client.latest()
    return result

CURRENCIES = getting_currency_quotes()

def checking_availability_currency(CURRENCIES):
    while True:
        current_currency = input("Введите исходную валюту: ")
        if current_currency in CURRENCIES['data']:
            break
    while True:
        result_currency = input("Введите результирующую валюту: ")
        if result_currency in CURRENCIES['data']:
            break
    return current_currency, result_currency

def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)
    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

def main(CURRENCIES):
    status_actions = None
    print('''ДОБРО ПОЖАЛОВАТЬ В КОНВЕРТ ВАЛЮТ!
1 - Список валют с ценами
2 - Конверт валют
0 - Выход''')
    while status_actions != 0:
        status_actions = int(input('\nНажмите для просмотра: '))
        if status_actions == 1:
            print('\nСПИСОК ВАЛЮТ С ЦЕНАМИ\n')       
            for i in CURRENCIES['data']:
                print(f'{i} = {round(CURRENCIES["data"][i], 2)}')       
        elif status_actions == 2:
            print('\nКОНВЕРТ ВАЛЮТ\n')
            currency = checking_availability_currency(CURRENCIES)
            amount = input("Введите количество: ")
            result = convert(float(amount), currency[0], currency[1], CURRENCIES['data'])
            print(f'\n{amount} {currency[0]} = {result} {currency[1]}')
    print('\nДО НОВЫХ ВСТРЕЧ!')

if __name__ == '__main__':
    main(CURRENCIES)

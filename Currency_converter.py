import freecurrencyapi

API_KEY = "fca_live_7biV5oZKQwAkn7Ot9GMPTCuhAtnj6GxJ5DzI0BJt"

def getting_currency_quotes(): 
    client = freecurrencyapi.Client(API_KEY)
    result = client.latest()
    return result

CURRENCIES = getting_currency_quotes()

def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)
    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

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

print("Добро пожаловать в конвертатор валют!")
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")
print('Доступные валюты:')

for key in CURRENCIES['data']:
    print(f'* {key} ', end="")
print('\n')

currency = checking_availability_currency(CURRENCIES)
amount = input("Введите количество: ")
result = convert(float(amount), currency[0], currency[1], CURRENCIES['data'])
print(f'{amount} {currency[0]} = {result} {currency[1]}')

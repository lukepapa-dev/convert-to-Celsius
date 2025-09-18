# This will convert Fahrenheit to Celsius
print()
print('----Fahrenheit to Celsius Converter!----')
print()

while True:
    fahrenheit = input('Enter Temprature (f) or type "done" to exit: ')

    if fahrenheit.lower() == 'done':
        print('Goodbye!')
        break

    try:
        f = float(fahrenheit)
        c = (f - 32) / 1.8
        print(f"{f}°F is {c}°C")
    except ValueError:
        print('Invalid Input! Please try again')
    continue

# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# temp = input('Enter the temperature to convert: ')
# Is_temp = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()





# def convert_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
#     return celsius


# def convert_to_fahrenheit(celsius):
#     fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
#     return fahrenheit


# if Is_temp == 'C': 
#     newtemp = convert_to_fahrenheit(temp)
#     print(f'{temp}°C is {newtemp}°F')
# else: 
#     newtemp = convert_to_celsius(temp)
#     print(f'{temp}°F is {newtemp}°C')

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

temp = float(input("Enter the temperature to convert: "))
Is_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if Is_temp == "C":
    newtemp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {newtemp:.2f}°F")
elif Is_temp == "F":
    newtemp = convert_to_celsius(temp)
    print(f"{temp}°F is {newtemp:.2f}°C")
else:
    print("Invalid scale. Please enter C or F.")

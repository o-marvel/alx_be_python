# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5



# Function to convert Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# User input
temp = float(input("Enter the temperature to convert: "))
Is_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


# Using the functions
if Is_temp == "C":
    newtemp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {newtemp:.2f}°F")

elif Is_temp == "F":
    newtemp = convert_to_celsius(temp)
    print(f"{temp}°F is {newtemp:.2f}°C")

else:
    print("Invalid option. Please enter C or F.")



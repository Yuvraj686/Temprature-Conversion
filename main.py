def convert_temperature(value, unit):
    if unit.lower() == "celsius":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit.lower() == "fahrenheit":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit.lower() == "kelvin":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit
    else:
        return None

value = float(input("Enter temperature value: "))
unit = input("Enter unit (Celsius, Fahrenheit, Kelvin): ")

result = convert_temperature(value, unit)

if result:
    if unit.lower() == "celsius":
        print(f"Fahrenheit: {result[0]:.2f}")
        print(f"Kelvin: {result[1]:.2f}")
    elif unit.lower() == "fahrenheit":
        print(f"Celsius: {result[0]:.2f}")
        print(f"Kelvin: {result[1]:.2f}")
    elif unit.lower() == "kelvin":
        print(f"Celsius: {result[0]:.2f}")
        print(f"Fahrenheit: {result[1]:.2f}")
else:
    print("Invalid unit.")

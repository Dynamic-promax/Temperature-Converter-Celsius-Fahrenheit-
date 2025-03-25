def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 # Fixed multiplication error

# User Input
choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().lower()

if choice == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius:.2f}°C is {celsius_to_fahrenheit(celsius):.2f}°F") # Fixed degree symbol
elif choice == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit:.2f}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C") # Fixed degree symbol
else:
    print("Invalid choice! Please enter 'C' or 'F'.")
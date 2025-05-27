"""
define celsius_to_fahrenheit(celsius)
    return celsius * 9 / 5 + 32
end celsius_to_fahrenheit

define fahrenheit_to_celsius(fahrenheit)
    return (fahrenheit - 32) * 5 / 9
end fahrenheit_to_celsius

define main
    prompt user for celsius temperature
    convert celsius to fahrenheit and display result

    prompt user for fahrenheit temperature
    convert fahrenheit to celsius and display result
end main

run main
"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")

main()

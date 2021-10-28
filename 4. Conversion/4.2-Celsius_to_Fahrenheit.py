# problem : Take the temperature in degrees Celsius and convert it to Fahrenheit.

user_input = float(input("Enter temperature in Celsius : "))

temp_to_fahrenheit = user_input * (9/5) + 32

print(f"{user_input} celcius = {temp_to_fahrenheit} degree Fahrenheit")
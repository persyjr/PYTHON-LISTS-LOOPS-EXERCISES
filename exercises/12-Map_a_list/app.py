Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
    farenheit=(9/5)*x+32
    return farenheit
# the magic go here:
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)

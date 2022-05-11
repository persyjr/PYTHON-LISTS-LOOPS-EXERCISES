names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
#Your code go here:
names=['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']
def prepender(string):
    return ("My name is: "+string)

result =list(map(prepender,names))
print(result)

all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def my_function(string):
     
     if (string[0]=="R"):
         return string

resulting_names = list(filter(my_function, all_names))
print(resulting_names)





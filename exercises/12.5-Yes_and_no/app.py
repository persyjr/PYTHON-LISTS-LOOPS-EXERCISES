theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def my_function( element):
    
        if (element==1):
            return 'wiki'
        if (element==0):
           return 'woko'

thewikis=list(map(my_function,theBools))
print(thewikis)
arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(arr):
    suma=0
    for i in arr:
        if i%2!=0:
            suma=suma+i
    print(suma)

sumOdds(arr)

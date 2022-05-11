def lyrics_generator(listain):
    message=0
    entrega=''
    resul=[]
    
    for i in listain:
        if i==0:
            resul.append("Boom")
        if i==1:
            message=message+1
            resul.append("Drop the base")
            if message==3:
                resul.append("!!!Break the base!!!")
    for i in resul:
        entrega=entrega+''+i+' '
    return entrega

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
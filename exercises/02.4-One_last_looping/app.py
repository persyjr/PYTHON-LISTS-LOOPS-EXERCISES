names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1]='Steven'
names[len(names)-1]='Pepe'
concatenado=names[2]+names[4]
names[0]=concatenado

for i in range(len(names),0,-1):
    temp=names[i-1]
    print(temp)
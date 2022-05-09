people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:

def deletePerson(person_name):
    #Your code go here:
    new_person=[]
    for i in people:
        if i != person_name:
            new_person.append(i)
    return new_person

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
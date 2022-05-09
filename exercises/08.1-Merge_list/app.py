chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    list_Result=[]
    for i in list1:
        list_Result.append(i)
    for i in list2:
        list_Result.append(i)
    return list_Result
print(merge_list(chunk_one, chunk_two))

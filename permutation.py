def permutaion(list1 ,list2):
    if len(list1)!= len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1==list2:
     return True
    else:
       False

list1=[1,2,3]
list2=[2,8,1]

print(permutaion(list1,list2))
    
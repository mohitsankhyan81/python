def list1(list,index=0):
    if index==len(list):
        return
    print(list[index])
    list1(list,index+1)
        

list=[1,2,3,4,5]
list1(list)
list1=[[1,2,3]
       ,[1,2,3]
       ,[1,2,3]]
list1=[0]*3
print(list1)
list1=[[0]*3 for i in range(3)]
print(list1)
list1[0][0]=5
print(list1)
# list=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
# k=4
# list1=[]
# i=0
# while i<len(list):
#     if i==k:
#         list1.append(20)
#         k=k+4
#     list1.append(list[i])
#     i=i+1
# print(list1)    


# list=[6,1,3,5,6,3,1]
# a=[]
# i=0
# prod=1
# while i<len(list):
#     if list[i]not in a:
#         a.append(list[i])
#     i=i+1
# k=0
# while k<len(a):
#     prod=prod*a[k]
#     k+=1
# print(a,prod)           
    

# a=[2,3,4,2,3,4,5,6,7,8,9,10,11] 
# a=list(set(a))
# print(a)

# a=[2,3,4,2,3,4,5,6,7,8,9,10,11] 
# a=list.pop(a)
# print(a)

# a=[2,3,4,2,3,4,5,6,7,8,9,10,11] 
# most=max(set(a),key=a.count)
# print(most)

# d_squares=[i**2 for in range(11) if i%2==1]
# print(odd_squares)

name="bhagyashree bhnadari"[::-7]
print(name)
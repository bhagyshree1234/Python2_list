# list=["0","1","2","3","4"]
# list1=["red","green","black","blue","white"]
# list2=["100","200","300","400","500"]
# i=0
# a=[] 
# while i<len(list):
#     sum=list[i]+list1[i]+list2[i]
#     a.append(sum)
#     i=i+1
# print(a)    


# list=["0","1","2","3","4"]
# list1=["red","green","black","blue","white"]
# list2=["100","200","300","400","500"]
# i=0
# a=[]
# while i<len(list):
#     sum=list[i]+list1[i]+list2[i]
#     a.append(sum)
#     i=i+1
# print(a)    
   
# a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
# k=0
# i=0
# n=[]
# while i<len(n):
#     j=0
#     h=[]
#     while j<3 and k!=len(a):
#         h.append(a[k])
#         j=j+1
#         k=k+1
#     n.append(h)    
#     if k==len(a):
#         break
#     i=i+1
# print(n) 
#    
# i=int(input("enter the number"))
# num=int(input("enter number"))
# while i<=num:
#     j=1
#     count=0
#     while j<=i:
#        if i%j==0:
#             count+=1
#        j+=1
#     if count==2:
#         print(i)
#     i+=1
# a=int(input("enter number"))
# i=1
# count=0
# while i<=a:
#     if a%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print(a,"p")
# else:
#     print("n",a)




# num=123
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print("Reverse =",rev)
a=567
b=10
print(a%b)

# list=["flour","cheese","carrots"]
# i=0
# while i<len(list):
#     print(i,':',list[i])
#     i+=1

# list=["flour","cheese","carrots"]
# i=0
# while i<len(list):
#     print(i,":",list[i])
#     i=i+1

# list=[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# b=""
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         b=b+list[i][j]
#         j+=1
#     i+=1
# print(b)

# list=[6,1,3,5,6,3]
# i=0
# b=[]
# prod=1
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#         prod=prod*b[i]
#     i+=1
# print(b,prod)

# list=[6,1,3,5,6,3]
# i=0
# b=[]
# prod=1
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#         prod=prod*b[i]
#     i=i+1
# print(b,prod)

# list=["flour","cheese","carrots"]
# i=0
# while i<len(list):
#     print(i,":",list[i])
#     i=i+1

# n=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# max2=0
# while i<len(n):
#     if n[i]>max:
#        max=n[i]
#     if n[i]>max2 and n[i]!=max:
#        max2=n[i]
#     i=i+1
# print(max2,max)            
 
# n=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# while i<len(n):
#      if n[i]>max:
#          max=n[i]
#      i=i+1
# print(max)  

 
# i=0
# while i<6:
#     if i==3:
#       break
#     print(i)
#     i=i+1
# a=[3,4,6,7,2,5,9,10]
# odd_number=[]
# even_number=[]
# i=0
# while i<len(a):
#       if a[i]%2==0:
#           even_number.append(a[i])
#       else:
#             odd_number.append(a[i])
#       i=i+1      
# print(even_number)
# print(odd_number)            
        


# a=[["r","t","u","r",],["t","s","s",]]
# b=""
# i=0
# while i<len(a):
#       j=0
#       while j<len(a[i]):
#             b=b+a[i][j]
#             j=j+1
#       i=i+1
# print(b)            

# list=[6,1,3,5,6,3,1]
# i=0
# b=[]
# prod=1
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#         prod=prod*b[i]
#     i=i+1
# print(b,prod)           

# n=[50,40,23,70,56,12,5,10,7]     
# i=0
# a=0
# while i<len(n):
#     if n[i]>a:             
#         a=n[i]
#     i=i+1
# print(a)
# i=0
# b=0
# while i<len(n):
#     if n[i]>b:
#         if n[i]!=a:
#             b=n[i]
#     i=i+1
# print(b)
# i=0
# c=0
# while i<len(n):                                                                                                                                          
#     if n[i]>c:
#         if n[i]!=a and n[i]!=b:
#             c=n[i]
#     i=i+1
# print(c)

# i=1
# while i<=10:
#     print(i)
#     i=i+1
# else:
#     i=i-1
#     print(-i)

# i=1
# j=10
# while i<=10 and j>=1:
#     print(i,j)
#     j-=1
#     i+=1

# j=1
# i=10
# while i>=1 and j<=10:
#     print(i,j)
#     i=i-1
#     j+=1

# i=1
# sum=0
# count=0
# while i<=10:
#     sum+=i
#     count+=1
#     i=i+1
# print(sum,count,"average","=",sum/count)

# list=[1,2,2,5,8,4,4,8]
# i=0
# b=[]
# while i<len(list):
#     if list[i]not in b:
#       b.append(list[i])
#     i=i+1
# print(b)    

# list="9119"
# i=0
# while i<len(list):
#     b=int(list[i])**2 
#     i=i+1
#     print(b,end="")  

# n=[50,40,23,70,56,12,5,10,7,] 
# i=0
# a=0
# while i>len(n):
#     if n[i]<a:
#         a=n[i]
#     i=i+1
# print(a)
# i=0
# b=0
# while i>len(n):
#     if n[i]<b:
#         if n[i]!=a:
#             b=n[i]
#     i=i+1
# print(b)
# i=0
# c=0
# while i<len(n):
#     if n[i]<c:
#       if n[i]!=a and n[i]!=b:
#         c=n[i]
#     i=i+1
# print(c)                        

# n=[50,40,23,70,56,12,5,10,7] 
# i=0
# a=n[0]
# while i<len(n):
#     if n[i]<a:
#         a=n[i]
#     i=i+1
# print(a)      
# i=0
# b=n[0]
# while i<len(n):
#     if n[i]<b and n[i]!=a:
#         b=n[i]
#     i=i+1
# print(b)
# i=0
# c=n[0]
# while i<len(n):
#     if n[i]<c and n[i]!=a and n[i]!=b:
#         c=n[i]
#     i=i+1
# print(c)           


# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# l_max=len(list[0])
# l_min=len(list[i])
# while i<len(list):
#     if l_max<len(list[i]):
#         max=list[i]
#     if l_min>len(list[i]):
#         min=list[i]
#     # while j<len(list[i]):
#         # max=list[i][j]
#         # j=j+1
#     i=i+1
# print(i,max)
# print(i,min)        
    

# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# l=len(list)
# i=0
# max_list=list[0]
# min_list=list[0]
# while i<len(list):
#     if len(list[i])<len(min_list):
#         min_list=list[i]
#     if len(list[i])>len(max_list):
#         max_list=list[i]
#     i+=1
# print(len(max_list),max_list)
# print(len(min_list),min_list)

# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# l_max=len(list[0])
# l_min=len(list[i])
# while i<len(list):
#     if l_max<len(list[i]):
#         max=list[i]
#     if l_min>len(list[i]):
#         min=list[i]
#     # while j<len(list[i]):
#         # max=list[i][j]
#         # j=j+1
#     i=i+1
# print(i,max)
# print(i,min) 

# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# l_max=len(list[0])
# l_min=len(list[i])
# while i<len(list):
#     if l_max<len(list[i]):
#         max=list[i]
#     if l_min>len(list[i]):
#         min=list[i]
#     # while j<len(list[i]): 
#         # max=list[i][j]
#         # j=j+1
#     i=i+1
# print(i,max)
# print(i,min)         

# list=[1,2,3,4,5,6,7]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print(list[i],"even")
#     else:
#         print(list[i],"odd")
#     i=i+1    

# num=int(input("enter the number"))
# i=0
# while i<=100:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count=count+1
#         j=j+1
#     if count==2:
#         print(i)
#     i=i+1    

# list=[1,-3,6,-8,6,5,-4]
# i=0
# while i<len(list):
#     if list[i]>0:
#         print(list[i],"positive")
#     else:
#         print(list[i],"negative")    
#     i=i+1    
    

# list=[23,46,32,25,46,33,71,90]
# i=0
# a=[]
# b=[]
# while i<len(list):
#     if list[i]%2==0:
#         a.append(list[i])
#     elif list[i]%2!=0:
#         b.append(list[i])
#     i=i+1
# print(a,b)    

# list=[12,67,98,34]
# i=0
# while i<len(list):
#     a=str(list[i])
#     j=0
#     sum=0
#     while j<len(a):
#      sum=sum+int(a[j])
#      j=j+1
#     i=i+1
#     print(sum)      


# list=["python","list","excerise","practice","solution"]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     b=list[i][0:2]
#     a=list[i][2:]
#     while j<len(list[i]):
#         a.append(b+a)
#         j=j+1
#         # print(a+b)
#         break
#     i=i+1
# # print(a)    
    
# list=[1,2,3,1,2,2]
# i=0
# a=[]
# while i<len(list):
#     if list[i]not in a:
#         a.append(list[i])
#     i=i+1 
# print(a)    


# list=[4,6,4,3,3,4,3,4,3,8]
# i=0
# n=[]
# while i<len(list):
#     j=0
#     count=0
#     while j<len(list):
#         if list[i]==list[j]:
#             count=count+1
#         j=j+1
#     if count>2:
#         if list[i]not in n:
#             n.append(list[i])
#     i=i+1
# print(n)            
                                                                                                       
# list=[4,5,5,5,3,8,]
# n=[]
# for i in list:
#     c=0
#     for j in list:
#         if i==j:
#             c=c+1
#     if c>2:
#         if i not in n:
#             n.append(i)
# print(n)                    

list=[1,2,3]
for i in range(len(list)):
    for j in range(len(list)):
        for k in range (len(list)):
            if i!=j and j!=k and k!=i:
                print(list[i],list[j],list[k])





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































    
    
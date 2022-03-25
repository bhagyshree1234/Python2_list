# b = "Hello, World!"
# print(b[2:-3])

# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print(names_list)
# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print(type(names_list))

# a=int(input("enter the number"))   
# b=int(input("enter the number"))  
# while a<b:
#       i=1
#       while i<=10:
#           print(a*i)
#           i=i+1
#       print()
#       a=a+1   

  
# a="bhagyashree"
# b="bhandari"
# print("bhagyashree bhanadri")


# num=int(input("enter the number"))
# if num>0:
#     print(num%10,"is last digit number")
# else:
#     print("is not last digit number")  


# num=int(input("enter the number"))
# if num<10000:
#     print(num+2000-(num*10/100))
# elif num<1500:
#     print(num+3000-(num*12/100)) 
# elif num<25000:
#     print(num+5000-(num*15/100))
# else:
#     print("nothing") 

# i=1
# while i<=5:
#     b=1
#     while b<=5-1:
#         print("",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     k=i-1
#     while k>=1:
#         print(k,end=" ")   
#         k=k-1
#     print() 
#     i=i+1        

# banks_list=["kotak","hdfc","rbl","sbi"]
# print(banks_list)
# print(type(banks_list))

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)


# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist=["apple","banana","cherry"]
# print(thislist[2])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[3:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list") 

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[-2] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) 

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist) 

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist=["apple","banana","mango"]
# thistuple=("kiwi","dragonfruit")
# thislist.extend(thistuple)
# print(thislist)

# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(-3)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist 

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) 

# thislist=["apple","banana","cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist=[1,2,3,4,5,6,7]
# for i in range(len(thislist)):
#     print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1
 
# thislist=["apple","banana","cherry"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist] 

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 

# fruits=["apple","mango","cherry","kiwi"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#      newlist.append(x)
# print(newlist)    

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)

# things=["pen","pencil","books","colors"]
# newlist=[x for x in things if "c" in x]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#       return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# list1=["apple","mango","grapes"]
# list2=[1,2,3,4]
# list3=list1+list2
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1) 

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1) 

# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# x = points.count(9)


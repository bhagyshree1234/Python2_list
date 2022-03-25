# p, q, r = 10, 20 ,30
# print(p, q, r)
 
# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )

# print(type({}) is set)

# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# print(type(0xFF))

# print(2 * 3 ** 3 * 4)

# print(-18 // 4)


# a = 4
# b = 11
# print(a | b)
# print(a >> 2)


# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

# f = open("test.txt", "r")
# print(f.readline(3))
# f.close()

# print('%d %d %.2f' % (11, '22', 11.22))

# print(sep='--', 'Ben', 25, 'California')

# print('%x, %X' % (15, 15))

# x = float('NaN')
# print('%f, %e, %F, %E' % (x, x, x, x))

# for num in range(-2,-5,-1):
#     print(num, end=", ")

# x = 0
# while (x < 100):
#   x+=2
# print(x)

# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# for num in range(10, 14):
#        for i in range(2, num):
#         if num%i == 1:
#           print(num)
#           break

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)        

# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(x)

# for num in range(2,-5,-1):
#     print(num, end=", ")

# str1 = 'Welcome'
# print (str1[:6] + ' PYnative')

# str = "My salary is 7000";
# print(str.isalnum())

# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

# str1 = "my isname isisis jameis isis bond";
# sub = "is";
# print(str1.count(sub, 4))

# str = "my name is James bond";
# print (str.capitalize())

# str1 = 'Welcome'
# print(str1*2)

# a = 4
# b = 11
# print(a | b)
# print(a >> 2)

# numbers = [10, 20]
# items = ["Chair", "Table"]

# numbers = [10, 20]
# items = ["Chair", "Table"]
# for x in numbers:
#   for y in items:
#     print(x, y)

# number1 = 20
# number2 = 30
# if number1*number2<=1000:
#     print(number1*number2)
# else:
#     print(number1+number2)

# i=0
# sum=0
# while i<=8:
#     sum=sum+i
#     print(i,sum)
#     i+=1

# word = input('Enter word ')
# print("Original String:", word)
# x = list(word)
# for i in x[0::2]:
#     print(i)


# l=[10, 20, 33, 46, 55]
# i=0
# b=[]
# while i<len(l):
#     if i%5==0:
#         b.append(l[:5])
#     i+=1
# print(b)

a="9119"
i=0
while i<len(a):
    b=int(a[i])**2
    i=i+1
    print(b,end="")    
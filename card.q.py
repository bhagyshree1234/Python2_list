marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# sum=0
# average=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum%marks[i][j]
#         j=j+1
#     i=i+1
# print(average)        



a = [[78, 76, 94, 86, 88]
,[91, 71, 98, 65, 76]
,[95, 45, 78, 52, 49]]
i=0
count=0
count1=0
count2=0
column1=0
column2=0
column3=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if j==0:
            column1+=a[i][j]
            count+=1
        elif j==1:
            column2+=a[i][j]
            count1+=1
        elif j==2:
            column3+=a[i][j]
            count2+=1
        j+=1
    i+=1
print(column1,column1/count)
print(column2,column2/count1)
print(column3,column3/count2)

list1=["red","maroon","yellow","olive"]
i=0
n=[]
while i<len(list1):
    print(i)
    j=0
    h=[]
    while j<len(list1[i]):
        h.append(list1[i][j])
        j=j+1
    n.append(h)
    print()
    i=i+1
print(n)    






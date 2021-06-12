l=[22,56,1,0,77,66]
print(f"unsorted List:- {l}")
for j in range(len(l)-1):
        for i in range(len(l)-1-j):
                if l[i]>l[i+1]:
                        l[i],l[i+1]=l[i+1],l[i]
print(f"sorted List:- {l}")

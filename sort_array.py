"""You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Example:sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def sort_array(l):
    siz=len(l)
    x=[]
    i=j=0
    for item in l:
        if item%2==1:
            x.append(item)
    x.sort()
    while i<siz:
        if l[i]%2==1:
            l[i]=x[j]
            j=j+1
        i=i+1
    return l

a=[0,5,1,3,2,4,8,6,9,7,34,65,23]
s=sort_array(a)
print(s)

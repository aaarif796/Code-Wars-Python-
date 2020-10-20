"""
In this program.
The function should return the sum of number which is less than 10 i.e
16= 1+6=7
if 2354=2+3+5+4=14>0 so 1+4=14
435=4+3+5=12=1+2=3

"""
def digital_root(n):
    s=str(n)
    sum=0
    for i in s:
        sum=sum+int(i)
    if sum<10:
        return sum
    else:
        return digital_root(sum)
    
a=435
print(digital_root(a))

n= int(input("please enter n numbers:"))
n1=0
n2=1
temp=0
n_next=0
list1=[]
while temp < n:
    list1.append(n1)
    n_next=n1+n2
    n1=n2
    n2=n_next
    temp=temp+1
def Reverse(fiblist):
    return [x for x in reversed(fiblist)]
print(Reverse(list1))
countodd=0
counteven=0
list2=[]
oddlist=[]
evenlist=[]
for num in list1:
    if num % 2 != 0:
        countodd=countodd+1
        oddlist.append(num)
        list2.append(num+3)
    else:
        counteven=counteven+1
        list2.append(num+4)
        evenlist.append(num)
print(f"count of odd:{countodd}")
print(f"count of even:{counteven}")
print(list2)
print(oddlist)
print(evenlist)





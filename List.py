print("hello world!")
# empty list
l=[]
l.append(1)
l.append(2)
l.append(3)
# print 1st elemet of 0 index
print(l[0])
for x in l:
    print(x)
# to find out the keywords in python
import keyword
print(keyword.kwlist)
li=[1,2,3]
li.insert(-1,23)
print(li)
A=[1,2,3]
B=[4,5,6]
# TO CONCATE TWO LIST
C=A+B
print(C)
# 10 willl be added to list A
print(A+[10])
# another way to add 10 into list
A+=[10]
print(A)
# to repeat the elements * operator is used 
D=[10,20]
print(D*3)
# NO CHANGES IN LIST D
print(D)

# TO CHANGE PERMANENT
D*=3
print(D)
# to add a new element into mylist
mylist=[10,20,30]
mylist[0]=100
print(mylist)
# to remove the element
mylist.remove(20)
print(mylist)
D.clear()
print(D)
d=[1,2,3,4,5]
d.reverse()
print(d)
# pop fun will remove the element and return the element will remove functon do not return the element
# here in pop function index number is given to the pop function
d.pop(0)
print(d)
# In remove functon we have to give the value to the function
d.remove(3)
print(d)
a=[10,20,30,40]
a.remove(20)
print(a)
a.pop(2)
print(a)
b=[10,20,10,30,10,40,50]
print(b.index(10))
# 1st argument is for the element and 2nd argument is for the starting index and 3rd argument is for ending index
print(b.index(10,1))
print(b.index(10,1,6))















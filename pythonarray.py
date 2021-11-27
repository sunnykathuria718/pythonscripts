import array as arr
a=arr.array('i',[1,2,3,4,58])
print(a[1])
#Length of Array
print(len(a))
#Print Array number
print(a[-2])
#Append Array
a.append(800)
print"Array a=" ,a
a.extend([5,6,7])
print"Array a=" ,a
a.insert(3,225)
print"Array a=" ,a
#Remove Element
print"Remove last element of Array" , a.pop()
print"Remove 4th element of Array", a.pop(3)
print(a)
#remove command
a.remove(58)
a.remove(800)
print"Remove through remove command", a
#Array Concatenation
b=arr.array('i',[100,2200,300,400])
c=arr.array('i',[1000,2000,3000,4000])
d=arr.array('i')
d=b+c
print(d)
#Slicing
print(d[0:5])
print(d[::-1])

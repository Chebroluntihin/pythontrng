x=[10,2,3,4,5,6,7,8,9,1]
a=x[:]
x.sort()
if a==x:
    print("List is in Ascending order")
else:
    print("List is not in Ascending order")

y=[1,2,3,4,5,6,7,8,9,10]
for i in y:
    if i%2==0:
        print(i)

x=[3,5,6,8,10,15,78]
y=[45,67,84,90,35,87]
x.append(y)
print(x)
x.extend(y)
print(x)
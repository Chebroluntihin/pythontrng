str='nithin'
print(str)
print(str[0])
print(str[2])
print(str[-2])
print(str[1:4])

str1='ch'
str2=' nithin'
print(str1+str2)

count=0
for letter in 'nithin':
    if(letter=='i'):
        count+=1
print(count)


str='nithin'
list_enumerate=list(enumerate(str))
print(list_enumerate)
print(len(str))
birthdays={'Albert Einstein':'21-09-2010',
           'Benjamin Franklin':'30-10-2021',
           'Ada Lovelace':'20-01-2021'}
print(" Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
      print(name)
print("Who's birthday do you want to look up?")
name=input()
if name in birthdays:
      print(name,birthdays[name])
else:
       print("we don't have your birthday")


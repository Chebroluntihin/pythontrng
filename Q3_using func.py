def char_input():
    name= str(input("what is your name"))
    age=int(input("what is your age"))
    year=str((100-age)+2021)
    print(name + " will be 100 years old in the year " + year)
    pass
print(char_input())
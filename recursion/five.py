#print name five times
def name(Name, count):
    if(count > 6):
        return
    else:
        print(Name)
        name(Name, count + 1)


count = 0
Name = input("Enter Name: ")
name(Name, count)
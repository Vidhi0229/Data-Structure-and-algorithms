print("Enter length: ")
n = int(input())

# rectangular Star pattern
print("rectangular Star pattern\n")
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print("\n")

# Right-Angled Triangle Pattern
print("Right-Angled Triangle Pattern")
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print("\n")

# Inverted Right Pyramid
print("Inverted Right Pyramid\n")
for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end="")
    print("\n")

# Star Pyramid
print("Star Pyramid\n")
for i in range(n):
    for j in range(i):
        if(j % 2 != 0):
            print("* ", end="")
        else:
            print(" ", end="")
    print("\n")


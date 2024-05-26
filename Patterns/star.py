print("Enter length: ")
n = int(input())

# rectangular Star pattern
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print("\n")

# Right-Angled Triangle Pattern
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print("\n")

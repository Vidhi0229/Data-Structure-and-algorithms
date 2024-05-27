print("Enter length: ")
n = int(input())

# Right-Angled Number Pyramid
print("Right-Angled Number Pyramid\n")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print("\n")

# Right-Angled Number Pyramid - II
print("Right-Angled Number Pyramid - II\n")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end="")
    print("\n")

#Inverted Numbered Right Pyramid
print("Inverted Numbered Right Pyramid\n")
for i in range(n, 0, -1):
    for j in range(i):
        print(j+1, end="")
    print("\n")

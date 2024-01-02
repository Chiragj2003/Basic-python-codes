size = int(input("enter the size "))

# Square Pattern
print("this is Square Pattern")
for i in range(size):
    for j in range(size):
        print("* ", end="")
    print()

print("\n")


# Right triangle pattern 
print("this is  Right triangle Pattern")

for i in range(size):
    for j in range(i + 1):
        print("* ", end="")
    print()
print("\n")


# Inverted Right Triangle Pattern
print("this is Inverted Right Triangle Pattern")

for i in range(size, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
print("\n")


# Pyramid Pattern
print("this is Pyramid Pattern")
for i in range(size):
    print(" " * (size - i - 1) + "* " * (i + 1))
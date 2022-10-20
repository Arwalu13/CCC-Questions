# t = height of the tines
# s = spacing between tines
# h = the length of the handle
t = int(input())
s = int(input())
h = int(input())

width = s * 2 + 3

for i in range(t):
    print("*" + (" " * s) + "*" + (" " * s) + "*")

print(width * "*")

for i in range(h):
    print((width // 2) * " " + "*")
h = int(input())
m = int(input())

for i in range(0, m):
    if -6*i**4 + h*i**3 + 2*i**2 + i <= 0:
        print("The balloon first touches ground at hour:")
        print(i)
        break
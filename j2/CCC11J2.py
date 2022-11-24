h = int(input())
m = int(input())
touchGround = False

for i in range(1, m + 1):
    if -6*i**4 + h*i**3 + 2*i**2 + i <= 0:
        print("The balloon first touches ground at hour:")
        print(i)
        touchGround = True
        break

if touchGround == False:
    print("The balloon does not touch ground in the given time.")

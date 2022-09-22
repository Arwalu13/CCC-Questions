cFish = int(input())
cBiggestFish = 0

for i in range(cFish):
    temp = input("").split()
    weight = int(temp[0])
    length = int(temp[1])

    if length * weight > cBiggestFish:
        cBiggestFish = length * weight

nFish = int(input())
nBiggestFish = 0

for i in range(nFish):
    temp = input("").split()
    weight = int(temp[0])
    length = int(temp[1])

    if length * weight > nBiggestFish:
        nBiggestFish = length * weight

if cBiggestFish > nBiggestFish:
    print("Casper")

elif nBiggestFish > cBiggestFish:
    print("Natalie")

else:
    print("Tie")
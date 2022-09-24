parkingSpace = int(input())

dayOneParking = input()
dayTwoParking = input()

count = 0

for i in range(0, parkingSpace):
    if dayOneParking[i]  == 'C' and dayTwoParking[i] == 'C':
        count += 1

print(count)
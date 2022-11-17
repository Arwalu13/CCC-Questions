p = int(input())
n = int(input())
r = int(input())

if n > p:
    print(0)
currentDay = 0
total = n
previousDayInfected = n

while total <= p:
    previousDayInfected *= r
    currentDay += 1
    total += previousDayInfected

print(currentDay)
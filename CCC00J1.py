temp = input().split(" ")
startDay = int(temp[0])
numOfDays = int(temp[1])

currentDay = startDay

print("Sun Mon Tue Wed Thr Fri Sat")

if startDay == 1:
    print("", end = "")

else:
    print(" " * ((startDay -1) * 4), end = "")

for i in range(1, numOfDays + 1):
    if currentDay == 8:
        currentDay = 1
        print("")
    
    if i <= 9:
        print(f"  {i}", end = "")
    
    else: 
        print(f" {i}", end = "")

    currentDay += 1

    
    if currentDay != 0 and i != numOfDays:
        print(" ", end = "")

print("")
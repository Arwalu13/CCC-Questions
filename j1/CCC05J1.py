daytimeMin = int(input())
eveningMin = int(input())
weekendMin = int(input())

aCost = 0
bCost = 0

if daytimeMin > 100:
    aCost += (daytimeMin - 100) * 25
aCost += eveningMin * 15
aCost += weekendMin * 20


if daytimeMin > 250:
    bCost += (daytimeMin - 250) * 45
bCost += eveningMin * 35
bCost += weekendMin * 25

aCost = str(aCost/100)
bCost = str(bCost/100)

if (aCost[-1] == "0" and aCost[-2] == "."):
    aCost += "0"

if (bCost[-1] == "0" and bCost[-2] == "."):
    bCost += "0"

print(f"Plan A costs {aCost}")
print(f"Plan B costs {bCost}")

if aCost > bCost:
    print(f"Plan B is cheapest.")

elif aCost == bCost:
    print(f"Plan A and B are the same price.")

else:
    print(f"Plan A is cheapest.")

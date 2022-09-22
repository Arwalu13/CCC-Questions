totalWins = 0

for i in range(6):
    gameStat = input('')

    if gameStat == 'W':
        totalWins += 1

if totalWins == 5 or totalWins == 6:
    print("1")

elif totalWins == 3 or totalWins == 4:
    print("2")

elif totalWins == 1 or totalWins == 2:
    print("3")

else:
    print("-1")
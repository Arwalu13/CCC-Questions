diceOne = int(input())
diceTwo = int(input())

numWays = 0

for i in range(1, diceOne + 1):
    for j in range(1, diceTwo + 1):
        if i + j == 10:
            numWays += 1

if numWays == 1:
    print("There is 1 way to get the sum 10.")

else:
    print(f"There are {numWays} ways to get the sum 10.")
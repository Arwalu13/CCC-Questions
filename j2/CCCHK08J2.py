totalNum = int(input())

for i in range(totalNum):
    num = input()

    while len(num) != 0:
        newNum = 0

        for i in num:
            newNum += int(i)
            
        num = str(newNum)
    
    print(num)


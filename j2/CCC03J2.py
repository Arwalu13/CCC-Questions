while True:
    num = int(input())
    if num == 1:
        print("Minimum perimeter is 4 with dimensions 1 x 1")
        continue
    if num == 0:
        break

    minL = 0
    minW = 0
    minP = 10000000000009

    for i in range(1, num):
        if num % i != 0:
            continue
        
        l = i
        w = num / l
        perimeter = 2 * (l + w)

        if perimeter < minP:
            minP = perimeter
            minL = l
            minW = w
    
    print(f"Minimum perimeter is {int(minP)} with dimensions {int(minL)} x {int(minW)}")

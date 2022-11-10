startYear = int(input())
endYear = int(input())

for i in range(startYear, endYear + 1, 60):
    print(f"All positions change in year {i}")
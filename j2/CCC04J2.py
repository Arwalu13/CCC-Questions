startYear = int(input())
endYear = int(input())

mayor = []
treasurer = []
chiefProgrammer = []
dogCatcher = []

for i in range(startYear, endYear + 1, 4):
    mayor.append(i)

for i in range(startYear, endYear + 1, 2):
    treasurer.append(i)

for i in range(startYear, endYear + 1, 3):
    chiefProgrammer.append(i)

for i in range(startYear, endYear + 1, 5):
    if i in mayor and i in treasurer and i in chiefProgrammer:
        print(f"All positions change in the year {i}")


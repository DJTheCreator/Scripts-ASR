use_needed_columns = False
needed_columns = (0, 4, 5)

with open('hurricane dataset.txt') as f:
    lines = f.readlines()

hurricaneList = []

for line in lines:
    storm = []
    k = 0
    for i in line:
        if i == ',':
            column = line[0:line.find(',')]
            if k in needed_columns and use_needed_columns:
                storm.append(column.strip())
            elif not use_needed_columns:
                storm.append(column.strip())
            line = line[line.find(',')+1:]
            k += 1
    if len(storm) > 3:
        hurricaneList.append(storm)
for i in range(len(hurricaneList)):
    print(hurricaneList[i])

#Current Issue, data still includes occasional storm Name
#AL092022, IAN, 40
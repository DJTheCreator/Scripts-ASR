needed_columns = (0, 4, 5, 6)

with open('hurricane dataset.txt') as f:
    lines = f.readlines()

hurricaneList = []

for line in lines:
    storm = []
    k = 0
    for i in line:
        if i == ',':
            column = line[0:line.find(',')]
            if k in needed_columns:
                storm.append(column.strip())
            #print(k in needed_columns)
            line = line[line.find(',')+1:]
            k += 1
    if len(storm) > 3:
        hurricaneList.append(storm)
# for i in range(len(hurricaneList)):
#     print(hurricaneList[i])
f = open("Filtered_Hurricane_Dataset.txt", "w+")
for i in range(len(hurricaneList)):
    f.write(str(hurricaneList[i]) + "\n")

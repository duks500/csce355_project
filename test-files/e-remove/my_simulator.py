import sys

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    data = [x.strip() for x in data]

# for x in range(len(data)):
#     print(data[x])
print(data[3])
firstLine = list(data[3])
# print(firstLine)

firstLine.remove('4')


for x in range(len(firstLine)):
    print firstLine[x],

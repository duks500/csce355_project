import sys
import re

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    data = [x.strip() for x in data]

# for x in range(len(data)):
#     print(data[x])
print(data[3])
firstLine = list(data[3])
# print(firstLine)

# firstLine.remove('4')
firstEs = 0
firstEe = 0

str = "The rain in Spain { 5 , 4 }"
x = re.search(r"{((\d*),)*}", str)

print("The first white-space character is located in position:",x.start())
# r”{((\d*),)*}”

# for x in range(len(firstLine)):
#     if firstEe == 0:
#         if firstLine[x] == '{':
#             print('')
#             firstEs+1
#         elif firstLine[x] == '}':
#             print('')
#             firstEe+1
#         elif firstLine[x] == ',':
#             print('')
#         else:
#             # print (firstLine[x])
#             firstLine.pop(x)
#     elif firstEe == 1:
#         if firstLine[x] == '{':
#             print('')
#             firstEs+1
#         elif firstLine[x] == '}':
#             print('')
#             firstEe+1
#         elif firstLine[x] == ',':
#             print('')
#         else:
#             print (firstLine[x])
#     else:
#         if firstLine[x] == '{':
#             print('')
#             firstEs+1
#         elif firstLine[x] == '}':
#             print('')
#             firstEe+1
#         elif firstLine[x] == ',':
#             print('')
#         else:
#             print (firstLine[x])
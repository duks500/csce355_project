import sys
print(sys.argv, len(sys.argv))

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    data = [x.strip() for x in data]

for x in range(len(data)): 
    print(data[x]) 
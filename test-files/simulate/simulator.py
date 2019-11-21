#!/usr/bin/python
import string
import sys
import re

def part1(startstates):
    print(startstates)

alphabet_ascii = string.ascii_lowercase

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
with open(sys.argv[2]) as my_file:
    string_input = my_file.readlines()

# collect the string of number of states
string_number_states = data[0]
string_st_number = re.findall(r'\d' , data[0])
to_number_st = [int(x) for x in string_st_number]
int_states_size = len(data)

# collect the alphabet size
string_alphabet_size = data[1]
string_alp_number = re.findall(r'\d' , data[1])
to_number = [int(x) for x in string_alp_number]
int_alp_size = to_number.pop()

# collect the numbers of the starting states
acceptingStates = re.findall(r'(\d+),*' , data[2])
accept_numbers = [int(x) for x in acceptingStates]

lis = []
alp_size =[]
lis_int = []

b = 3
while b < int_states_size:
    dataSplitLine = data[b].split()
    lis.append(dataSplitLine)
    b += 1
for c in range(len(lis)):
    for d in range(len(lis[c])):
        lis[c][d] = re.findall(r'(\d+),*' , lis[c][d])

c = 0
while c < int_alp_size :
    alp_size.append(alphabet_ascii[c])
    c+=1
print(alp_size)

print(string_input[0])

for x in range(len(string_input)) :
    for y in range(len(string_input[x])):
        # print(string_input[x][y])
        print(len(alp_size))
        c = 0
        while c < len(alp_size) :
            if alp_size[c] == string_input[x] :
                print(string_input[x])
            c+=1
            # int_try = int(alp_size[c])
            # if alp_int == string_input[x][y] :
            #     print('=')

#!/usr/bin/python

import sys
import re

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    # data = [x.strip() for x in data]

# collect the string of number of states
string_number_states = data[0]

# collect the alphabet size
string_alphabet_size = data[1]

# collect the string for the statring states
string_accepting = re.findall( r'\D' , data[2])

## start algorithm by checking for accepting states
# collect the numbers of the starting states
acceptingStates = re.findall(r'(\d+),*' , data[2])
accept_numbers = [int(x) for x in acceptingStates]
# print (accept_numbers)

## chek for the e move
i = 3
while i < len(data):
    indexOfeState = 0
    # split the i line
    dataSplitLine = data[i].split()
    # print (dataSplitLine)
    # collect only the numbers
    findAllNumbers = re.findall(r'(\d+),*' , dataSplitLine[0])
    # print (findAllNumbers)
    # converst ['1'] to [1]
    numbers = [int(x) for x in findAllNumbers]
    # check for empty list
    # not empty! - check for e move to final styate
    if numbers != []:
        # deal with every e movement speratley
        while indexOfeState < len(numbers):
            # check if the state at e is accepting state
            for x in range(len(accept_numbers)):
                # if exept -> add this level to accept_numbers
                if accept_numbers[x] == numbers[indexOfeState]:
                    accept_numbers.append(i-3)
            indexOfeState += 1
    i += 1


####### OUTPUT #######

#number pf states is the same
print(string_number_states),

#alphabet size
print(string_alphabet_size),


# remove duplicate and sort the list from smallest to biggest
print('Accepting states:'),
accept_numbers_final = list(set(accept_numbers))
for x in range(len(accept_numbers_final)):
    print(accept_numbers_final[x]),
print('')

###### transfer every e transition to 0 - {}
y = 3
while y < len(data):
    dataSplitLine = data[y].split()
    findAllNumbers = re.findall(r'(\d+),*' , dataSplitLine[0])
    numbers = [int(x) for x in findAllNumbers]
    numbers = {}
    dataSplitLine[0] = numbers
    print(dataSplitLine[0]),
    ## still need to work on this, must change dataSplitLine to the right name
    ##size of 64
    # print(dataSplitLine[1]),
    # print(dataSplitLine[2])
    x = 1
    lenght_of_list = len(dataSplitLine) - 1
    while x < len(dataSplitLine):
        if x == lenght_of_list:
            print(dataSplitLine[x])
        else:
            print(dataSplitLine[x]),
        x += 1
    y += 1


######### for loop to go throug the all list
# for x in range(len(data)):
#     print (data[x])

######### while loop to go to each line
# i = 3
# while i < len(data):
#     print(data[i])
#     i += 1

######### split line into 3 diffrent items: {} , {} , {}
# dataSplitLine = data[3].split()
# print(dataSplitLine[0])





#
# str2 = "{1,4,5}      {}      {6}"
# str3 = str2.split()
# data1 = data[3].split()
# print (str3)
# xs = re.findall(r'(\d+),*', data[3])
# numbers = [int(x) for x in xs]
# print (numbers)
# for f in xs:
#     print f

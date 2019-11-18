#!/usr/bin/python

import sys
import re

def search(list,n):

    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    # data = [x.strip() for x in data]


# collect the string of number of states
string_number_states = data[0]
string_st_number = re.findall(r'\d' , data[0])
to_number_st = [int(x) for x in string_st_number]
int_states_size = len(data)
# int_states_size -= 4

# collect the alphabet size
string_alphabet_size = data[1]
string_alp_number = re.findall(r'\d' , data[1])
to_number = [int(x) for x in string_alp_number]
int_alp_size = to_number.pop()
# int_alp_size += 1

# collect the string for the statring states
string_accepting = re.findall( r'\D' , data[2])

## start algorithm by checking for accepting states
# collect the numbers of the starting states
acceptingStates = re.findall(r'(\d+),*' , data[2])
accept_numbers = [int(x) for x in acceptingStates]
# print (accept_numbers)


test_list = []
## chek for the e move
i = 3
while i < len(data):
    indexOfeState = 0
    # split the i line
    dataSplitLine = data[i].split()
    # collect only the numbers
    findAllNumbers = re.findall(r'(\d+),*' , dataSplitLine[0])
    # converst ['1'] to [1]
    numbers = [int(x) for x in findAllNumbers]
    # test_list.append(numbers)
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
    #check condition number 2 - r to s, so to t-> r to t
    i += 1

b = 3
while b < int_states_size:
    dataSplitLine = data[b].split()
    test_list.append(dataSplitLine)
    b += 1


test_list_final = []

for c in range(len(test_list)):
    for d in range(len(test_list[c])):
        test_list[c][d] = re.findall(r'(\d+),*' , test_list[c][d])
        # print(findAllNumbers),
        numbers = [int(x) for x in findAllNumbers]
        # print(numbers),
        test_list_final.append(findAllNumbers)

for z in range(len(test_list)):
    # print(test_list),
    for x in range(len(test_list[z])):
        # check for empty states first
        if len(test_list[z][0]) == 0 :
            # print('empty set, do nothing')
            pass
        #not empty! greate now check where the line is going to
        else:
            print('check if edge exist at state: ')
            for y in range(len(test_list[z][0])):
                check_if_edge_star = int(test_list[z][0][y])
                check_if_edge_end = test_list[check_if_edge_star][x]
                if len(check_if_edge_end) == 0 :
                    # test_list[z][0][y] = check_if_edge_end
                    print('no edge')
                # the following print show the diffrent path for diffrent states (e , a , b ....)
                print('the edge: '),
                print(check_if_edge_star),
                # if goes to 0 - no movment - set the current start edge to
                print('goes to: '),
                print (check_if_edge_end)
            print('')

#-----------------------------------------------------------#
#print(test_list[0])
#[['5', '9'], [], []]

#print(test_list[0][0])
#['5', '9']

#print(test_list[0][0][0])
#5
#-----------------------------------------------------------#



# empty list
# if len(test_list[0][1]) == 0 :
#     print('empty')


## test_list[z][x][y] - >
## z => state lile e or a or b
## x => the line |
## y => the row --

####### OUTPUT #######

#number pf states is the same
# print(string_number_states),
#
# #alphabet size
# print(string_alphabet_size),
#
#
# # remove duplicate and sort the list from smallest to biggest
# print('Accepting states:'),
# accept_numbers_final = list(set(accept_numbers))
# for x in range(len(accept_numbers_final)):
#     print(accept_numbers_final[x]),
# print('')
#
# ###### transfer every e transition to 0 - {}
# y = 3
# while y < len(data):
#     dataSplitLine = data[y].split()
#     findAllNumbers = re.findall(r'(\d+),*' , dataSplitLine[0])
#     numbers = [int(x) for x in findAllNumbers]
#     numbers = {}
#     dataSplitLine[0] = numbers
#     print(dataSplitLine[0]),
#     ## still need to work on this, must change dataSplitLine to the right name
#     ##size of 64
#     # print(dataSplitLine[1]),
#     # print(dataSplitLine[2])
#     x = 1
#     lenght_of_list = len(dataSplitLine) - 1
#     while x < len(dataSplitLine):
#         if x == lenght_of_list:
#             print(dataSplitLine[x])
#         else:
#             print(dataSplitLine[x]),
#         x += 1
#     y += 1

#################### end #######################3

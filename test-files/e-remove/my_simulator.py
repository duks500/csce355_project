#!/usr/bin/python

import sys
import re

def search(list,n):

    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

def Union(lst1, lst2):
    final_list = list(set().union(lst1, lst2))
    return final_list


def part4(test_og, test_q , testr , test_x):
    if testr == [] : ## the wanted state has no e moves
        start_edge = int(test_q) #the index of the state
        ab = 1
        while ab < len(test_og[start_edge]) :
            if test_og[start_edge][ab] != [] : # the state is not empty! do the union
                test_x[ab] = list(set().union( test_x[ab] , test_og[start_edge][ab]))
            # else: # set has no e movment - do nothing
            ab += 1

## test_list = list
## t_int = the current number of int like if we have [5,9] - looking at 5
def lastPart(test_list, t_int):
    if test_list[x][0] != [] :
        print(test_list[x][0][z]),
        r_int = int(test_list[x][0][z])
        print(r_int)


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


for x in range(len(test_list)):
    for y in range(len(test_list[x][0])):
        edge_q = int(test_list[x][0][y])
        edge_r = test_list[edge_q][0]
        part4(test_list , test_list[x][0][y] , test_list[edge_q][0], test_list[x])

# for x in range(len(test_list)):
    # for y in range(len(test_list[x])):
    #     for z in range(len(test_list[x][y])):
    #         if y != 0:
    #             s_edge = int(test_list[x][y][z]) #movment from s to r
    #
    #             print(s_edge)


# for x in range(len(test_list)):
#     for y in range(len(test_list[x])):
#             for z in range(len(test_list[x][0])) :
#                 #start recursive here
#                 lastPart(test_list, 0)
print('before')

for x in range(len(test_list)):
    print(test_list[x])

# def part4(test_og, test_q , testr , test_x):
#     if testr == [] : ## the wanted state has no e moves
#         start_edge = int(test_q) #the index of the state
#         ab = 1
#         while ab < len(test_og[start_edge]) :
#             if test_og[start_edge][ab] != [] : # the state is not empty! do the union
#                 test_x[ab] = list(set().union( test_x[ab] , test_og[start_edge][ab]))
#             # else: # set has no e movment - do nothing
#             ab += 1


#test_x[ab] = list(set().union( test_x[ab] , test_og[start_edge][ab]))


########## part 2 #############


    #print(test_list[x]),
    #[['5', '9'], [], []] [['0', '7'], [], ['6']] [[], [], ['8']] [['8'], [], []] [[], ['1', '2'], ['3']] [['2'],
    #[], []][['2', '6'], [], ['3', '4', '8']] [[], ['6'], ['6']] [['7'], [], ['9']] [['0'], [], ['5', '7']]

    # print(test_list[x][0]),
    # ['5', '9'] ['5', '9'] ['0', '7'] ['0', '7'] ['8'] ['2'] ['2', '6'] ['2', '6'] ['7'] ['0']

    # print(test_list[x][0][y]),
    # 5 9 0 7 8 2 2 6 7 0
########## end part 2 #############



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

#!/usr/bin/env python
import argparse
import sys

class DFA:
    def __init__(self, nodes, alphabet):
        self.nodes = nodes
        self.alphabet = alphabet

    def run_simulation(self, test_string):
        test_string_list = list(test_string)

        current_node = 0

        for char in test_string_list:
            # if the character isnt even in the alphabet dont bother
            if char not in self.alphabet: 
                sys.stdout.write("reject")
                return

            for edge in self.nodes[current_node].edges:
                if char in edge:
                    current_node = int(edge[1])
                    break

        if self.nodes[current_node].accepting:
            sys.stdout.write("accept")
        else:
            sys.stdout.write("reject")
        
class Node:
    def __init__(self, id, accepting, edges):
        self.id = id
        self.accepting = accepting
        self.edges = edges # list of tuples (character, next_node)


def main(dfa_info, test_strings):     
    dfa_info_arr = dfa_info.split("\n")
    test_strings = test_strings.split("\n")[:-1]

    num_states = int((dfa_info_arr[0])[18:]) # how many states 0-(n-1)
    accepting_states = ((dfa_info_arr[1])[18:]).split(" ") # list of accepting states (strings of nums)
    alphabet = list(((dfa_info_arr[2])[10:])) # list of alphabet chars

    table = dfa_info_arr[3:-1]

    nodes = [] # initialize nodes

    for state in range(0, num_states):
        node_id = state
        accepting = False

        if str(node_id) in accepting_states:
            accepting = True
        
        node_table_row_edges = table[state].split(" ")

        edges = [] # initialize edges

        for index, char in enumerate(alphabet):
            edges.append((char, int(node_table_row_edges[index])))

        nodes.append(Node(node_id, accepting, edges))

    dfa = DFA(nodes, alphabet)

    for string in test_strings:
        dfa.run_simulation(string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dfa_info')
    parser.add_argument('test_strings')

    args = parser.parse_args()

    with open(args.dfa_info) as fileObj:
        dfa_info = fileObj.read()

    with open(args.test_strings) as fileObj:
        test_strings = fileObj.read()

    main(dfa_info, test_strings)

import random
import os
import sys
from heapq import heappush, heappop
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
import numpy as np
import pickle





def cost(input_file, output_file, dist_dict, adjacency_matrix):
    input_data = utils.read_file(input_file)
    output_data = utils.read_file(output_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    kingdom_tour = output_data[0]
    conquered_kingdoms = output_data[1]

    kingdom_tour = [list_of_kingdom_names.index(name) for name in kingdom_tour]
    conquered_kingdoms = [list_of_kingdom_names.index(name) for name in conquered_kingdoms]

    return cylce_val(dist_dict, kingdom_tour) + dominating_set_value(adjacency_matrix, conquered_kingdoms)

def output_cost(file_num, dist_dict, adjacency_matrix):
    input_file, output_file = "./inputs/" + file_num + ".in", "./outputs/" + file_num + ".out"
    return cost(input_file, output_file, dist_dict, adjacency_matrix)


############### DOM SET #############################



def random_dominating_set(neighbor_dict, source_index, number_of_kingdoms, node_prob, temp):

    all_nodes = set(range(number_of_kingdoms))
    con = set()
    #sur = set([source_index])
    sur = set()
    prob = softmax(node_prob, temp)
    if (0 in prob):
        prob = None
    order = np.random.choice(number_of_kingdoms, number_of_kingdoms, replace=False, p =prob)
    for i in order:
        con.add(i)
        sur.add(i)
        sur.update(neighbor_dict[i])
        if len(sur) == len(all_nodes):
            return con
    return con

def get_dom_prob(neighbor_dict, adjacency_matrix, number_of_kingdoms):
    return [1*len(neighbor_dict[i])/(adjacency_matrix[i][i]) for i in range(number_of_kingdoms)]

def softmax(x, temp):
    """Compute softmax values for each sets of scores in x."""
    e_x = (np.exp(x - np.max(x))) / temp
    return e_x / e_x.sum(axis=0) # only difference


def dominating_set_value(adjacency_matrix, dom_set):
    val = 0
    for node in dom_set:
        val += adjacency_matrix[node][node]
    return val




def best_dominating_set(neighbor_dict, source_index, number_of_kingdoms, adjacency_matrix, temp):
    node_prob = get_dom_prob(neighbor_dict, adjacency_matrix, number_of_kingdoms)
    all_dom = []
    rep_check = set()
    for i in range(15000):
        dom_set = random_dominating_set(neighbor_dict, source_index, number_of_kingdoms, node_prob, temp)
        val = dominating_set_value(adjacency_matrix, dom_set)
        if val not in rep_check:
            rep_check.add(val)
            heappush(all_dom, (val, dom_set))
    top10 = []
    for i in range(15):
        if len(all_dom) == 0:
            break
        top10.append(heappop(all_dom))
    return top10




######################################### Cycle ##############


def best_cycle(dist_dict, dom_set, source_index):

    source_con = False
    if source_index in dom_set:
        dom_set.remove(source_index)
        source_con = True

    best_cycle = None
    if not dom_set:
        return (0, [0])
    for i in range(1000000):
        cycle = list(random_cycle(dom_set))
        cycle = [source_index] + cycle + [source_index]
        val = cylce_val(dist_dict, cycle)
        if best_cycle is None or best_cycle[0] > val:
            best_cycle = (val, cycle)

    if source_con:
        dom_set.add(source_index)

    return best_cycle



def random_cycle(dom_set):
    return np.random.choice(list(dom_set), len(dom_set), replace=False)

# def best_cycle(dist_dict, dom_set, source_index):

#     source_con = False
#     if source_index in dom_set:
#         dom_set.remove(source_index)
#         source_con = True

#     best_cycle = None
#     if not dom_set:
#         return (0, [0])
#     for i in range(100000):
#         if (i % 10000 == 0):
#             print("Processing: ", i)
#         cycle = get_cycle(dom_set, dist_dict, source_index)
#         cycle = [source_index] + cycle + [source_index]
#         val = cylce_val(dist_dict, cycle)
#         if best_cycle is None or best_cycle[0] > val:
#             best_cycle = (val, cycle)

#     if source_con:
#         dom_set.add(source_index)

#     return best_cycle



# def get_cycle(dom_set, dist_dict, source_index):
#     node_list = list(dom_set)
#     next_node = source_index
#     cycle = []
#     while node_list:
#         prob = next_prob(node_list, dist_dict, next_node)
#         next_node = np.random.choice(node_list, 1, p=prob)[0]
#         node_list.remove(next_node)
#         cycle.append(next_node)

#     return cycle 


# def next_prob(node_list, dist_dict, curr_node):
#     val_lst = [1/dist_dict[nd][curr_node] for nd in node_list]
#     return softmax(val_lst, 1)

def cylce_val(dist_dict, cycle):
    total_cost = 0
    for i in range(len(cycle) - 1):
        total_cost += dist_dict[cycle[i]][cycle[i + 1]]
    return total_cost


def get_path(cycle_order, path_dict):
    path = []
    order_len = len(cycle_order)
    for i in range(order_len - 2):
        path += path_dict[cycle_order[i]][cycle_order[i + 1]]
        path.pop()

    path += path_dict[cycle_order[order_len - 2]][cycle_order[order_len - 1]]
    return path



################# write solutions ##################

def write_output(file_num, solution, list_of_kingdom_names, path_dict):
    file = open("./outputs2/" + file_num + ".out", "w")
    cycle_order = solution[1]
    conquer_set = solution[2]
    path = get_path(cycle_order, path_dict)
    # print(path)
    for i in path:
        file.write(list_of_kingdom_names[i])
        file.write(" ")
    file.write("\n")
    for j in conquer_set:
        file.write(list_of_kingdom_names[j])
        file.write(" ")
    file.close()


######################################## SOLVER ##################

file_names = []
for i in range(0,726):
    file_names.append(str(i) + ".in")
file_names.remove("249.in")
file_names.remove("250.in")
file_names.remove("310.in")
file_names.remove("521.in")
file_names.remove("696.in")
file_names.remove("697.in")
file_names.remove("698.in")
file_names.remove("711.in")
file_names.remove("712.in")
file_names.remove("713.in")


for file_name in file_names:
    print("#########################")
    print(file_name)
    print("#########################")
    input_data = utils.read_file("./inputs/" + file_name)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    source_index = list_of_kingdom_names.index(starting_kingdom)

    temp = 1
    file_num = file_name.split(".")[0]

    neighbor_dict = pickle.Unpickler(open( "./neighbors_dict/" + file_num + "_neighbors_dict.p", "rb" )).load()

    dist_dict = pickle.Unpickler( open( "./shortest_dist_dict/" + file_num + "_dist_dict.p", "rb" ) ).load()
    path_dict = pickle.Unpickler( open( "./shortest_path_dict/" + file_num + "_path_dict.p", "rb" ) ).load()
    curr_best = output_cost(file_num, dist_dict, adjacency_matrix)


    top10_dom = best_dominating_set(neighbor_dict, source_index, number_of_kingdoms, adjacency_matrix, temp)
    for dom_cost, dom_set in top10_dom:
        if dom_cost >= curr_best:
            continue
        cycle_tup = best_cycle(dist_dict, dom_set, source_index)
        cycle_cost = cycle_tup[0]
        cycle_path = cycle_tup[1]
        val = dom_cost + cycle_cost
        with open("./curr.txt", "w") as file_curr:
                file_curr.write(file_num + "\n")       
        if curr_best > val:
            with open("./beaten.txt", "a") as file:
                file.write(file_num + "\n")
                file.write("curr_best: " + str(curr_best) + "\n")
                file.write("new_best: "+ str(val) + "\n" + "\n")
            best_solution = (dom_cost+cycle_cost, cycle_path, dom_set)
            write_output(file_num, best_solution, list_of_kingdom_names, path_dict)
            break;





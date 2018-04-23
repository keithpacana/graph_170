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



def graph_creator(adjacency_matrix, number_of_kingdoms):
    edge_list = []
    for i in range(number_of_kingdoms):
        for j in range(i):
            weight = adjacency_matrix[i][j]
            if weight == "x":
                continue
            edge_list.append((i,j, weight))
    G = nx.Graph()
    nodelist = range(number_of_kingdoms)
    G.add_weighted_edges_from(edge_list, nodelist=nodelist)
    return G



############### DOM SET #############################



def random_dominating_set(neighbor_dict, source_index, number_of_kingdoms, node_prob, temp):

    all_nodes = set(range(number_of_kingdoms))
    con = set()
    #sur = set([source_index])
    sur = set()
    prob = softmax(node_prob, temp)
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


def is_dominating_set(G, nbunch):

    testset = set(n for n in nbunch if n in G)
    nbrs = set()
    for n in testset:
        nbrs.update(G[n])
    if len(set(G) - testset - nbrs) > 0:
        return False
    else:
        return True




def dominating_set_value(adjacency_matrix, dom_set):
    val = 0
    for node in dom_set:
        val += adjacency_matrix[node][node]
    return val




def best_dominating_set(neighbor_dict, source_index, number_of_kingdoms, adjacency_matrix, temp):
    node_prob = get_dom_prob(neighbor_dict, adjacency_matrix, number_of_kingdoms)
    all_dom = []
    rep_check = set()
    for i in range(10000):
        dom_set = random_dominating_set(neighbor_dict, source_index, number_of_kingdoms, node_prob, temp)
        val = dominating_set_value(adjacency_matrix, dom_set)
        if val not in rep_check:
            rep_check.add(val)
            heappush(all_dom, (val, dom_set))
    top10 = []
    for i in range(10):
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

    all_cycle = []
    ep_check = set()
    for i in range(500000):
        cycle = list(random_cycle(dom_set))
        cycle = [source_index] + cycle + [source_index]
        val = cylce_val(dist_dict, cycle)
        all_cycle.append((val, cycle))

    if source_con:
        dom_set.add(source_index)

    return min(all_cycle, key=lambda x: x[0])



def random_cycle(dom_set):

    return np.random.choice(list(dom_set), len(dom_set), replace=False)


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
    file = open("./outputs/" + file_num + ".out", "w")
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
for i in range(15, 716):
    file_names.append(str(i) + ".in")


for file_name in file_names:
    print("#########################")
    print(file_name)
    print("#########################")
    input_data = utils.read_file("./inputs/" + file_name)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    source_index = list_of_kingdom_names.index(starting_kingdom)

    temp = 1
    file_num = file_name.split(".")[0]

    neighbor_dict = pickle.load( open( "./neighbors_dict/" + file_num + "_neighbors_dict.p", "rb" ) )
    neighbor_cost = pickle.load( open( "./neighbors_cost/" + file_num + "_neighbors_cost.p", "rb" ) )
    dist_dict = pickle.load( open( "./shortest_dist_dict/" + file_num + "_dist_dict.p", "rb" ) )
    path_dict = pickle.load( open( "./shortest_path_dict/" + file_num + "_path_dict.p", "rb" ) )


    top10_dom = best_dominating_set(neighbor_dict, source_index, number_of_kingdoms, adjacency_matrix, temp)
    best_solution = None
    # print("top_10_dom: ", top10_dom)
    for dom_cost, dom_set in top10_dom:
        cycle_tup = best_cycle(dist_dict, dom_set, source_index)
        cycle_cost = cycle_tup[0]
        cycle_path = cycle_tup[1]
        if best_solution is None or best_solution[0] > (dom_cost + cycle_cost):
            best_solution = (dom_cost+cycle_cost, cycle_path, dom_set)

    # print(best_solution)
    write_output(file_num, best_solution, list_of_kingdom_names, path_dict)






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
from rutgers_tsp import solve_for_cycle





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

    available = set(range(number_of_kingdoms))
    con = set()
    sur = set()
    prob = softmax(node_prob, temp)
    if (0 in prob):
        prob = None
    order = np.random.choice(number_of_kingdoms, number_of_kingdoms, replace=False, p =prob)
    for chosen in order:
        if chosen not in available:
            continue
        con.add(chosen)
        sur.add(chosen)
        sur.update(neighbor_dict[chosen])
        available = available - sur
        if len(sur) >= number_of_kingdoms:
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
    for i in range(60000):
        dom_set = random_dominating_set(neighbor_dict, source_index, number_of_kingdoms, node_prob, temp)
        val = dominating_set_value(adjacency_matrix, dom_set)
        if val not in rep_check:
            rep_check.add(val)
            heappush(all_dom, (val, dom_set))
    top10 = []
    for i in range(6):
        if len(all_dom) == 0:
            break
        top10.append(heappop(all_dom))
    return top10




######################################### Cycle ##############


def best_cycle(dist_dict, dom_set, source_index):

    has_source = True
    if source_index not in dom_set:
        dom_set.add(source_index)
        has_source = False

    best_cycle = None
    for i in range(3):
        cycle = solve_for_cycle(dom_set, dist_dict, source_index)
        val = cylce_val(dist_dict, cycle)
        print("VAL", i, ":", val)
        if best_cycle is None or best_cycle[0] > val:
            print("BEAT: ", i)
            best_cycle = (val, cycle)

    if not has_source:
        dom_set.remove(source_index)

    return best_cycle


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

def write_output(file_num, solution, list_of_kingdom_names, path_dict, write_to):
    file = open(write_to + file_num + ".out", "w")
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
def solver(curr_file, iter_file, beaten_file, write_to, poly2, range_start, range_end):
    for j in range(10000):
        with open(iter_file, "a") as file_iter:
            file_iter.write(str(j) + "\n")  

        file_names = []
        for i in range(range_start, range_end):
            if i in [102, 103, 104, 210, 211, 212, 375, 376, 377, 705, 706, 707, 249, 250, 310, 521, 696, 697, 698, 711, 712, 713]:
                continue
            if i in [195, 207, 208, 209, 336, 337, 338, 528, 529, 594, 596, 642, 643, 644]:
                continue
            file_names.append(str(i) + ".in")

        for file_name in file_names:
            print("#########################")
            print(file_name)
            print("#########################")
            input_data = utils.read_file("./inputs/" + file_name)
            number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
            source_index = list_of_kingdom_names.index(starting_kingdom)

            temp = 10
            file_num = file_name.split(".")[0]
            with open(curr_file, "a") as file_curr:
                file_curr.write(file_num + "\n")  

            poly_path = "./"
            if poly2:
                poly_path = "./dict_poly2/"

            neighbor_dict = pickle.Unpickler(open( poly_path + "neighbors_dict/" + file_num + "_neighbors_dict.p", "rb" )).load()

            dist_dict = pickle.Unpickler( open( poly_path + "shortest_dist_dict/" + file_num + "_dist_dict.p", "rb" ) ).load()
            path_dict = pickle.Unpickler( open( poly_path + "shortest_path_dict/" + file_num + "_path_dict.p", "rb" ) ).load()
            curr_best = output_cost(file_num, dist_dict, adjacency_matrix)

            top10_dom = best_dominating_set(neighbor_dict, source_index, number_of_kingdoms, adjacency_matrix, temp)
            for dom_cost, dom_set in top10_dom:
                if dom_cost >= curr_best or len(dom_set) < 8:
                    print("Skipping: ", len(dom_set))
                    continue
                cycle_tup = best_cycle(dist_dict, dom_set, source_index)
                cycle_cost = cycle_tup[0]
                cycle_path = cycle_tup[1]
                val = dom_cost + cycle_cost    
                if curr_best > val:
                    with open(beaten_file, "a") as file_beat:
                        file_beat.write(file_num + "\n")
                        file_beat.write("curr_best: " + str(curr_best) + "\n")
                        file_beat.write("new_best: "+ str(val) + "\n" + "\n")
                        print("write")
                    best_solution = (dom_cost+cycle_cost, cycle_path, dom_set)
                    write_output(file_num, best_solution, list_of_kingdom_names, path_dict, write_to)
                    break;
            
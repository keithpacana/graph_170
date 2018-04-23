import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
from dijkstra import single_source_dijkstra_path_length
from min_dominating_set import min_weighted_dominating_set



###### Helper Functions ######

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



##### Graph Solve Object Class #######
class GraphSolver:

	def __init__(self, input_file):
		input_data = utils.read_file(input_file)
		self.number_of_kingdoms, self.list_of_kingdom_names, self.starting_kingdom, self.adjacency_matrix = data_parser(input_data)
		

		self.source_index = self.list_of_kingdom_names.index(self.starting_kingdom)
		
		self.G = Graph(self.adjacency_matrix, self.number_of_kingdoms, self.source_index)
		
		self.dijk = self.G.get_dijkstra()

		self.kingdom_dict = dict()
		self.c_n = []

		for i in range(self.number_of_kingdoms):
			self.c_n.append(self.adjacency_matrix[i][i])
			self.kingdom_dict[i] = self.list_of_kingdom_names[i]

		self.unconq = set(range(self.number_of_kingdoms))

		self.dominating_set = self.get_dominating_set()
		print(self.dominating_set)

	def get_conquer_cost(self, node_index):

		return self.adjacency_matrix[node_index][node_index]

	def get_total_neighbor_cost(self, node_index):
		total = 0
		for neighbor in self.G.get_neighbors(node_index):
			if neighbor == self.source_index:
				continue
			total += self.get_conquer_cost(neighbor)

		return total 

	def get_dom_weight(self):
		lst = []
		for i in range(self.number_of_kingdoms):
			lst.append(self.get_conquer_cost(i))
		return lst

	def get_dominating_set(self):
		return min_weighted_dominating_set(self.G.graph, self.get_dom_weight())



####### Graph Object Class ####
class Graph:
	def __init__(self, adjacency_matrix, number_of_kingdoms, source_index):
		self.graph = graph_creator(adjacency_matrix, number_of_kingdoms)
		self.source = source_index


	def get_dijkstra(self):
		return single_source_dijkstra_path_length(self.graph, self.source)

	def get_neighbors(self, node):
		return self.graph.neighbors(node)

	def get_neighbors_levels(self, node, level):
		neighbors = set()
		curr_level = []
		while level > 0:
			curr_level = []

	def get_dominating_set():
		return 0

solver = GraphSolver("small_test.in")





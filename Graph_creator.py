import networkx as nx
from Graph_matrix import adjacency_matrix
from Atomic_creator import create_50






def create_50_input():
	graph1 = nx.Graph()
	nodelist = list(range(0,50))
	graph1.add_weighted_edges_from(create_50(), nodelist=nodelist)
	arr = adjacency_matrix(graph1).toarray()
	file = open("50.in","w")
	file.write("50\n")
	file.write(string_of_nodes(50) + "\n")
	file.write("0\n")
	for row in arr:
		r = ""
		for element in row:
			if element == 0:
				element = "x"
			r += str(element)
			r += " "
		r += "\n"
		file.write(r)

	file.close()


def string_of_nodes(num_nodes):
	s = ""
	for i in range(num_nodes):
		s += str(i)
		s += " "
	return s


create_50_input()
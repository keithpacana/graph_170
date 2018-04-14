import networkx as nx
from Graph_matrix import adjacency_matrix
from Atomic_creator import create_50
from onehundred_creator import create_100
from twohundred_creator import create_200






def create_50_input():
	graph1 = nx.Graph()
	nodelist = list(range(0,50))
	lst = create_50()
	graph1.add_weighted_edges_from(lst, nodelist=nodelist)
	arr = adjacency_matrix(graph1).toarray()
	# for i in range(50):
	# 	for tup in lst:
	# 		if (tup[0] == i) and (tup[1] == i):
	# 			print(tup, " : ", arr[i][i])
	file = open("50.in","w")
	file.write("50\n")
	file.write(string_of_nodes(50) + "\n")
	file.write("0\n")
	for row in arr:
		r = ""
		for element in row:
			if element == 0:
				element = "x"
			else:
				element += 1879321462.62
			r += str(element)
			r += " "
		r += "\n"
		file.write(r)
	file.close()

def create_100_input():
	graph1 = nx.Graph()
	nodelist = list(range(0,99))
	graph1.add_weighted_edges_from(create_100(), nodelist=nodelist)
	arr = adjacency_matrix(graph1).toarray()
	file = open("100.in","w")
	file.write("99\n")
	file.write(string_of_nodes(99) + "\n")
	file.write("0\n")
	for row in arr:
		r = ""
		for element in row:
			if element == 0:
				element = "x"
			else:
				element += 1879321462.62
			r += str(element)
			r += " "
		r += "\n"
		file.write(r)
	file.close()

def create_200_input():
	graph1 = nx.Graph()
	nodelist = list(range(0,197))
	graph1.add_weighted_edges_from(create_200(), nodelist=nodelist)
	arr = adjacency_matrix(graph1).toarray()
	file = open("200.in","w")
	file.write("197\n")
	file.write(string_of_nodes(197) + "\n")
	file.write("0\n")
	for row in arr:
		r = ""
		for element in row:
			if element == 0:
				element = "x"
			else:
				element += 1879321462.62
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
create_100_input()
create_200_input()
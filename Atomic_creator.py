def type1_creator(source, start):
	lst = []
	

	####### Type 1
	###### define nodes
	# One is conqured in the solution
	zero1 = start
	one1 = zero1 + 1
	two1 = zero1 + 2
	three1 = zero1 + 2
	## four1 is conqured in solution
	four1 = zero1 + 4
	five1 = zero1 + 5
	middle1 = zero1 + 6

	print("one1: " + str(one1))
	print("four1: " + str(four1))

	# weights
	lst.append((zero1, zero1, 750))
	lst.append((one1, one1, 100))
	lst.append((two1, two1, 100))
	lst.append((three1, three1, 100))
	lst.append((four1, four1, 100))
	lst.append((five1, five1, 100))
	lst.append((middle1, middle1, 25))

	# connect all to the middle one
	lst.append((zero1, middle1, 1000))
	lst.append((one1, middle1, 1000))
	lst.append((two1, middle1, 1000))
	lst.append((three1, middle1, 1000))
	lst.append((four1, middle1, 1000))
	lst.append((five1, middle1, 1000))

	# connect the ones around the middle one
	lst.append((zero1, one1, 150))
	lst.append((zero1, two1, 150))
	lst.append((one1, three1, 150))
	lst.append((three1, five1, 150))
	lst.append((five1, four1, 150))
	lst.append((four1, two1, 150))


	####### Type 2
	###### define nodes
	zero2 = middle1 + 1
	one2 = zero2 + 1
	two2 = zero2 + 2
	three2 = zero2 + 3
	four2 = zero2 + 4
	five2 = zero2 + 5
	middle2 = zero2 + 6

	print("middle2: " + str(middle2))

	# weights
	lst.append((zero2, zero2, 750))
	lst.append((one2, one2, 1000))
	lst.append((two2, two2, 1000))
	lst.append((three2, three2, 1000))
	lst.append((four2, four2, 1000))
	lst.append((five2, five2, 1000))
	lst.append((middle2, middle2, 250))

	# connect all to the middle one
	lst.append((zero2, middle2, 500))
	lst.append((zero2, middle2, 500))
	lst.append((two2, middle2, 500))
	lst.append((three2, middle2, 500))
	lst.append((four2, middle2, 500))
	lst.append((five2, middle2, 500))

	# connect the ones around the middle one
	lst.append((zero2, one2, 20))
	lst.append((zero2, two2, 20))
	lst.append((one2, three2, 20))
	lst.append((three2, five2, 20))
	lst.append((five2, four2, 20))
	lst.append((four2, two2, 20))



	#Middle men intbetween type1 and type2
	mm1 = middle2 + 1
	mm2 = mm1 + 1
	mm3 = mm1 + 2
	mm4 = mm1 + 3
	mm5 = mm1 + 4
	mm6 = mm1 + 5
	mm7 = mm1 + 6
	mm8 = mm1 + 7


	#Middle men conquering cost
	lst.append((mm1, mm1, 750))
	lst.append((mm2, mm2, 750))
	lst.append((mm3, mm3, 750))
	lst.append((mm4, mm4, 750))
	lst.append((mm5, mm5, 750))
	lst.append((mm6, mm6, 750))
	lst.append((mm7, mm7, 750))
	lst.append((mm8, mm8, 750))

	#Firt three middle men connected to four1 so then don't need to be conqured
	lst.append((mm1, four1, 550))
	lst.append((mm2, four1, 550))
	lst.append((mm3, four1, 550))
	# Second 2 connected to one1 so don't need to be conqured as well
	lst.append((mm4, four1, 550))
	lst.append((mm5, four1, 550))
	#Last three connected to middle2
	lst.append((mm6, middle2, 550))
	lst.append((mm7, middle2, 550))
	lst.append((mm8, middle2, 550))


	#Useless edges which will never be used anyway
	lst.append((mm1, one2, 750))
	lst.append((mm2, one2, 750))
	lst.append((mm3, one2, 750))
	lst.append((mm4, one2, 750))
	lst.append((mm5, one2, 750))
	lst.append((mm6, one2, 750))
	lst.append((mm7, one2, 750))
	lst.append((mm8, one2, 750))

	lst.append((mm1, two2, 750))
	lst.append((mm2, two2, 750))
	lst.append((mm3, two2, 750))
	lst.append((mm4, two2, 750))
	lst.append((mm5, two2, 750))
	lst.append((mm6, two2, 750))
	lst.append((mm7, two2, 750))
	lst.append((mm8, two2, 750))

	lst.append((mm1, three2, 750))
	lst.append((mm2, three2, 750))
	lst.append((mm3, three2, 750))
	lst.append((mm4, three2, 750))
	lst.append((mm5, three2, 750))
	lst.append((mm6, three2, 750))
	lst.append((mm7, three2, 750))
	lst.append((mm8, three2, 750))

	lst.append((mm1, four2, 750))
	lst.append((mm2, four2, 750))
	lst.append((mm3, four2, 750))
	lst.append((mm4, four2, 750))
	lst.append((mm5, four2, 750))
	lst.append((mm6, four2, 750))
	lst.append((mm7, four2, 750))
	lst.append((mm8, four2, 750))

	lst.append((mm1, five2, 750))
	lst.append((mm2, five2, 750))
	lst.append((mm3, five2, 750))
	lst.append((mm4, five2, 750))
	lst.append((mm5, five2, 750))
	lst.append((mm6, five2, 750))
	lst.append((mm7, five2, 750))
	lst.append((mm8, five2, 750))

	lst.append((mm1, three1, 750))
	lst.append((mm2, three1, 750))
	lst.append((mm3, three1, 750))
	lst.append((mm4, three1, 750))
	lst.append((mm5, three1, 750))
	lst.append((mm6, three1, 750))
	lst.append((mm7, three1, 750))
	lst.append((mm8, three1, 750))


	#connect source to the two zeros
	lst.append((source, zero1, 350))
	lst.append((source, zero2, 350))

	return lst, mm8
	

def main_bushy_2_micro(source, start):
	lst = []
	
	# Each bushy micro connects each other by their number 4
	lst1, last1, four1 = micro_bushy(source, start)

	lst = lst + lst1

	lst2, last2, four2 = micro_bushy(four1, last1 + 1)

	lst = lst + lst2

	#Just a few more useless nodes to fill up to 50
	useless1 = last2 + 1
	useless2 = useless1 + 1
	useless3 = useless1 + 2

	# low weight conquering cost to trick people into wanting to conquer
	lst.append((useless1, useless1, 10))
	lst.append((useless2, useless2, 10))
	lst.append((useless3, useless3, 10))

	# connect them to both of the fours 
	lst.append((useless1, four1, 50))
	lst.append((useless2, four1, 50))
	lst.append((useless3, four1, 50))

	lst.append((useless1, four2, 50))
	lst.append((useless2, four2, 50))
	lst.append((useless3, four2, 50))

	# just some more useless edges
	lst.append((useless1, four1 + 4 , 50))
	lst.append((useless2, four1 + 4, 50))
	lst.append((useless3, four1 + 4, 50))
	lst.append((useless1, four2 + 4 , 50))
	lst.append((useless2, four2 + 4, 50))
	lst.append((useless3, four2 + 4, 50))


	lst.remove((source, start + 1, 50))
	lst.append((source,start + 1,400))
	lst.append((source, four2, 400))

	return lst, useless3



def micro_bushy(source, start):
	lst = []

	######define nodes
	one = start
	# two is connected to source
	two = start + 1
	three = start + 2
	# four is conqured
	four = start + 3
	five = start + 4
	# six is conquered
	six = start + 5
	seven = start + 6
	eight = start + 7
	nine = start + 8
	ten = start + 9
	eleven = start + 10
	# twelve is conquered
	twelve = start + 11

	lst.append((one, one, 100))
	lst.append((two, two, 100))
	lst.append((three, three, 100))
	lst.append((four, four, 20))
	lst.append((five, five, 100))
	lst.append((six, six, 30))
	lst.append((seven, seven, 100))
	lst.append((eight, eight, 100))
	lst.append((nine, nine, 100))
	lst.append((ten, ten, 100))
	lst.append((eleven, eleven, 100))
	lst.append((twelve, twelve, 50))

	# connect to source
	lst.append((source, two, 50))
	# all edges are of price 5
	lst.append((one, two, 5))
	lst.append((one, five, 5))
	lst.append((one, six, 5))

	lst.append((two, five, 5))
	lst.append((two, six, 5))
	lst.append((two, seven, 5))
	lst.append((two, three, 5))

	lst.append((three, six, 5))
	lst.append((three, seven, 5))
	lst.append((three, eight, 5))
	lst.append((three, four, 5))

	lst.append((four, seven, 5))
	lst.append((four, eight, 5))

	lst.append((five, nine, 5))
	lst.append((five, ten, 5))
	lst.append((five, six, 5))

	lst.append((six, nine, 5))
	lst.append((six, ten, 5))
	lst.append((six, eleven, 5))
	lst.append((six, seven, 5))

	lst.append((seven, ten, 5))
	lst.append((seven, eleven, 5))
	lst.append((seven, twelve, 5))
	lst.append((seven, eight, 5))

	lst.append((eight, eleven, 5))
	lst.append((eight, twelve, 5))

	lst.append((nine, ten, 5))

	lst.append((ten, eleven, 5))

	lst.append((eleven, twelve, 5))


	return lst, twelve, four



def create_50():
	lst = []

	#source cost
	source = 0
	lst.append((source,source, 800))

	lst1, last1 = type1_creator(source,1)

	#Print for debug, should be 22
	print(last1)

	lst2, last2 = main_bushy_2_micro(source, last1 + 1)

	#Print for debug, should be 49 cause source is 0 and matrix is 50 by 50
	print(last2)




	# Just some more expensive edges you don't wanna ever consider
	# to be continued

	lst = lst + lst1 + lst2

	for i in range(1,23):
		# not connecting these ones to make sure you wanna go back to source
		if i == 2 or i == 5 or i == 14:
			continue
		for j in range(23, 50):
			lst.append((i,j, 750))


	return lst



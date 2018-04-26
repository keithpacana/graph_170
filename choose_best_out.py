import numpy as np
import pickle
from output_cost import cost
import sys
import os.path
from shutil import copyfile

MAX_VAL = sys.maxsize


out_dir_0 = "./outputs/"
out_dir_1 = "./new_out/outputs/"
out_dir_2 = "./new_out_aws/outputs"
out_dir_3 = "./outputs_tsp/"
out_dirs = [out_dir_0, out_dir_1, out_dir_2, out_dir_3]
file_nums = []
input_dir = "./inputs/"
dst = "../170_output/outputs/"


for i in range(0,753):
    file_nums.append(str(i))
file_nums.remove("102")
file_nums.remove("103")
file_nums.remove("104")
file_nums.remove("210")
file_nums.remove("211")
file_nums.remove("212")
file_nums.remove("375")
file_nums.remove("376")
file_nums.remove("377")
file_nums.remove("705")
file_nums.remove("706")
file_nums.remove("707")
file_nums.remove("249")
file_nums.remove("250")
file_nums.remove("310")
file_nums.remove("521")
file_nums.remove("696")
file_nums.remove("697")
file_nums.remove("698")
file_nums.remove("711")
file_nums.remove("712")
file_nums.remove("713")


for file_num in file_nums:
	print("#####", file_num, "#####")
	winner_index = 0
	if file_num not in ["195", "207", "208", "209", "336", "337", "338", "528", "529", "594", "596", "642", "643", "644"]:
		costs = []
		for out_dir in out_dirs:
			output_file_path = out_dir + file_num + ".out"
			input_file_path = input_dir + file_num + ".in"
			val = 0
			if os.path.exists(output_file_path):
				val = cost(input_file_path, output_file_path)
			else:
				val = MAX_VAL

			costs.append(val)

		winner_index = np.argmin(costs)

	winner_path = out_dirs[winner_index]
	if winner_index != 0:
		print(winner_index, file_num)
		print(winner_path)
	copyfile(winner_path + file_num + ".out" , dst + file_num + ".out")


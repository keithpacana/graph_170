from tsp_aws_solver import solver


solver("./curr_hive1.txt", "./iter_hive1.txt", "./beaten_hive1.txt", "./out/", False, 0, 50)
#file write to what current file it is on, iteration it's on, beaten and value, where it's writing to
def get_int_input():
    in_ = raw_input()
    return int(float(in_))

def get_str_input():
    in_ = raw_input()
    return [int(float(ele)) for ele in in_.split(" ")]

output = []
T = get_int_input()
for t in range(T):
	N = get_int_input()
	coor_coll = []
	for n in range(N):
		coor_coll.append(get_str_input())
	int_val=zip(*coor_coll)
	x_val = max(int_val[0])-min(int_val[0])
	y_val = max(int_val[1])-min(int_val[1])
	output.append(max(x_val,y_val)**2)
for val in output:
	print val

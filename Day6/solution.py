# -*- coding: utf-8 -*-
# @Author: SharmiliSrinivasan
# @Date:   2019-01-01 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2019-01-01 17:07:14

from itertools import product
check_lst = list(product([0,1],repeat=3))

n = int(float(raw_input()))
output = []
for i in range(n):
    c_vals = [int(float(x)) for x in raw_input().split()]
    verified = "Yes"
    for (x,y,z) in check_lst:
        xy = c_vals[int("{}{}".format(x,y),2)]
        set_1 = c_vals[int("{}{}".format(xy,z),2)]
        yz = c_vals[int("{}{}".format(y,z),2)]
        set_2 = c_vals[int("{}{}".format(x,yz),2)]
        if set_1 != set_2:
            verified = "No"
            break
    output.append(verified)

for res in output:
    print res

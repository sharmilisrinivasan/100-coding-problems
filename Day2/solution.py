# -*- coding: utf-8 -*-
# @Author: SharmiliSri
# @Date:   2018-06-14 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2018-06-15 20:02:00

'''
Explanation:
If n is a number,
Number of zeros in n! is given by
n/(5^1) + n/(5^2) + ... + n/(5^k) ; till n>= (5^k) (taking only integer part of the division)

Eg:
n = 1000

(1000/5) + (1000/25) + (1000/125) + (1000/625) = 200 + 40 + 8 + 1 = 249

Thus, 249 trailing zeros in 1000!

Also, Number of zeros increases at every multiplier of 5,
leaving 5 numbers to have same number of zeros in their factorial.

'''

for _ in range(input()):
    no_of_zeros = int(input())
    n=0
    while True:
        zeros_acc = 0
        den = 5
        while (n/den != 0):
            zeros_acc += (n/den)
            den *=5
        if (zeros_acc< no_of_zeros):
            n+=5
            continue
        elif (zeros_acc == no_of_zeros):
            print "5"
            print "{} {} {} {} {}".format(n, (n+1), (n+2), (n+3), (n+4))
            break
        else:
            print "0"
            break

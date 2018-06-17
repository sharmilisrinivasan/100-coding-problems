# -*- coding: utf-8 -*-
# @Author: SharmiliSri
# @Date:   2018-06-14 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2018-06-17 15:08:06

'''
Explanation:
1. A number's multiples occur in pairs
eg: For X=100; (Divisor, Quotient): (1*100);(2*50);(4*25);(5*20);(10*10)
Thus, it is sufficient to look from 1 to sqrt(X)
2. The tipping point (where divisor's bits turns equal or greater than quotient) occurs at powers of 2
i.e. 1,2,4,8 etc. as bit gets added in the binary representation at these points.
Thus, it is sufficient to check only powers of 2 for change condition.
3. At the last value of multiple pairs obtained in step-1,
the bits of divisor and quotient are more and more equal.
Thus, the solution (changing value) is more probable to be near the last multiple pair.
4. Get a power of 2 which is near the last-multiple pair. Either the power or its counter-part ,
whichever is higher will be the solution
'''
for _ in range(input()):
    X=input()
    div_ = 1
    while ((div_*div_) <= X): # Getting value near last multiple pair
        div_ = div_<<1 # Checking only powers of 2
    div_1 = div_/2
    div_2 = X/div_
    # Checking both higher and lower powers of 2 and taking one more near to last multiple-pair
    to_sub = div_1-1 if div_1 > div_2 else div_2
    print X-to_sub

# -*- coding: utf-8 -*-
# @Author: SharmiliSri
# @Date:   2018-06-14 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2018-06-17 11:45:14

from collections import defaultdict

def get_bit_rep(char_):
    return 1<<(ord(char_)-97)

def get_balanced_substr_cnt(str_):
    # Example: str_ = abccba
    dp = []
    dp.append(0)
    for idx,char_ in enumerate(str_):
        dp.append(dp[idx]^get_bit_rep(char_))
    # dp = [0 , "a", "ab", "abc", "ab", "a", 0]
    # str comes back to old state if a balanced str exists in the substr
    # eg: "ab" -> "abc" ("cc" substr here) -> "ab"
    map_ = defaultdict(int)
    map_[dp[0]] += 1
    count_ = 0
    for idx in range(1,len(dp)):
        count_ += map_[dp[idx]]
        # Add number of occurences before,
        # to capture all possible openings closed by current pattern
        map_[dp[idx]] += 1
    return count_

for _ in range(input()):
    str_ = raw_input()
    print get_balanced_substr_cnt(str_)

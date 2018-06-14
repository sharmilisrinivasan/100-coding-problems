# -*- coding: utf-8 -*-
# @Author: SharmiliSri
# @Date:   2018-06-14 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2018-06-14 18:24:24

# Fetching input
string_ = raw_input()
decode_key = int(raw_input())

ret_str = ""
for char_ in string_:
    if char_.isalnum():
        if char_.isdigit():
            key_ = (decode_key%10)
            lower_ord = ord("0")
            upper_ord = ord("9")
        elif char_.isupper():
            key_ = (decode_key%26)
            lower_ord = ord("A")
            upper_ord = ord("Z")
        elif char_.islower():
            key_ = (decode_key%26)
            lower_ord = ord("a")
            upper_ord = ord("z")
        new_val = ord(char_)+key_
        if upper_ord and (new_val > upper_ord):
            new_val = (lower_ord-1+(new_val-upper_ord))
        ret_str+=chr(new_val)
    else:
        ret_str+=char_
print ret_str

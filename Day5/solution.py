# -*- coding: utf-8 -*-
# @Author: SharmiliSri
# @Date:   2018-06-14 18:10:03
# @Last Modified by:   SharmiliSri
# @Last Modified time: 2018-06-18 23:15:42

def encrypt_txt(txt_,len_):
    if len_<=1:
        return txt_
    mid = (len_-1)/2
    left_str = txt_[0:mid]
    right_str = txt_[(mid+1):]
    return txt_[mid]+encrypt_txt(left_str,len(left_str))+encrypt_txt(right_str,len(right_str))
    
for _ in range(input()):
    len_=input()
    txt_ = raw_input()
    print encrypt_txt(txt_,len_)

#!/usr/bin/python3
def uniq_add(my_list=[]):
    integers = set()
    for num in my_list:
        integers.add(num)
    sum_uniq = sum(integers)
    return sum_uniq

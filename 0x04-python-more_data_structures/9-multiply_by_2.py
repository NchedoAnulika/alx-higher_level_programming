#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_value = {}
    for key, value in a_dictionary.items():
        multiplied_value[key] = value * 2
    return multiplied_value

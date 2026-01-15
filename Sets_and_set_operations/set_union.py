#!/usr/bin/python3

"""
This function checks whether a set is is a union
"""

first_set = set([1,2,3])
second_set = set([4,5,6])

common_set = first_set | second_set
print("First union set", common_set)

third_set = set([7,8,9])
fourth_set = set([1,2,3])

common_set = third_set.union(fourth_set)

print("Secon union set", common_set)

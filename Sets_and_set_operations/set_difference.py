#!/usr/bin/python3

set_a = set([1,2,3,4,5,6])

set_b = set([3,4,5,6,7,8])

difference_a = set_a - set_b
difference_b = set_b - set_a

print(f"The elements that are only in set a, {set_a}  but not b, {set_b}  are", difference_a)
print(f"The elements that are only in set b, {set_b}  but not a, {set_a}  are", difference_b)


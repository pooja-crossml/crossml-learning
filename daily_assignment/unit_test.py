# from testing import complete_name

# print("Enter first and last name or enter x to exit")

# first_name = input("Enter first name")
# if first_name  == 'x':
#     print("goodbye!")
#     # break

# last_name = input("Enter last name")
# if last_name  == 'x':
#     print("goodbye!")
#     # break

import calc
import unittest

class TestCals(unittest.Testcase):
    def test_add(self):
        result = calc(6,7)
        self.ass
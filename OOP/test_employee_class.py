from employee_class import Employee, PartTime, FullTime, Casual

import unittest

class EmployeeClassTest(unittest.TestCase):
    """docstring for EmployeeClassTest"""

    def test_Employee_instance(self):
        Mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertIsInstance(Mark, Employee, msg='The object should be an instance of the `Employee` class')
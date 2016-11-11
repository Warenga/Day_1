from employee_class import Employee, PartTime

import unittest

class EmployeeClassTest(unittest.TestCase):
    """docstring for EmployeeClassTest"""

    def test_Employee_instance(self):
        mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertIsInstance(mark, Employee, msg='The object should be an instance of the `Employee` class')

    def test_Employee_Salary_method_1(self):
        mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertEqual(mark.salary(), 0, msg='Salary should be able to be executed in the object')

    def test_PartTime_Sub_Class(self):
        Kelly = PartTime(4, 'Kelly', 'Howard', 'kelly@gmail.com')
        self.assertIsInstance(Kelly, PartTime, msg='The object should be an instance of "PartTime" class ')


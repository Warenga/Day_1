from employee_class import Employee, PartTime, FullTime, Casual

import unittest

class EmployeeClassTest(unittest.TestCase):
    """docstring for EmployeeClassTest"""

    def test_Employee_instance(self):
        """ tests instance of Employee """
        mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertIsInstance(mark, Employee, msg='The object should be an instance of the `Employee` class')

    def test_Employee_Salary(self):
        """ tests if instance of Employee can call the method salary """
        mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertEqual(mark.salary(), 0, msg='Salary should be able to be executed in the object')

    def test_PartTime_Sub_Class(self):
        """ tests instance of PartTime subclass, passes attributes set in Superclass """
        Kelly = PartTime(4, 'Kelly', 'Howard', 'kelly@gmail.com')
        self.assertIsInstance(Kelly, PartTime, msg='The object should be an instance of "PartTime" class ')

    def test_PartTime_Salary_one(self):
        """ tests if instance of PartTime can call the method salary """
        Kelly = PartTime(4, 'Kelly', 'Howard', 'kelly@gmail.com')
        self.assertEqual(Kelly.salary(), 16000, msg='Salary should be able to be executed through an instance of the Sub Class')

    def test_FullTime_Sub_Class(self):
        """ tests instance of FullTime, passes attributs set in SuperClass """
        Jake = FullTime(7, 'Jake', 'Keane', 'jakekeane@gmail.com')
        self.assertIsInstance(Jake, FullTime, msg='The object should be an instance of "FullTime" class ')

    def test_Fulltime_Salary(self):
        """ tests if instance of FullTime can call the method salary """
        Jake = FullTime(7, 'Jake', 'Keane', 'jakekeane@gmail.com')
        self.assertEqual(Jake.salary(), 38400, msg='Salary should be able to be executed through an instance of the Sub Class')

    def test_Casual_Sub_Class(self):
        """ tests instance of Casual """
        Jake = Casual(7, 'Jake', 'Keane', 'jakekeane@gmail.com')
        self.assertIsInstance(Jake, Casual, msg='The object should be an instance of "Casual" class ')

    def test_Casual_Salary(self):
        """ tests if instance of Casual can call salary method """
        Jake = Casual(7, 'Jake', 'Keane', 'jakekeane@gmail.com')
        Jake.hours = 5
        Jake.days = 5
        self.assertEqual(Jake.salary(), 20000, msg='Salary should be able to be executed through an instance of the Sub Class')  

    def test_raise_polymorphism_error(self):
        """ tests if instance of Employee can call abstractmethod """
        mark = Employee(5,'Mark', 'Kenneth', 'markk@gmail.com' )
        self.assertEqual(mark.job_type(), 'Job type can only be set by SubClasses')

    def test_pay_encapsulation(self):
        """ tests if private __weeklyPay can be accessed through object._Employee__weeklyPay """
        Jill = PartTime(7, 'Jill', 'Keane', 'jakekeane@gmail.com')
        Jill.salary()
        self.assertEqual(Jill._Employee__weeklyPay, 4000)

    def test_abstractmethod(self):
        """ tests if job type abstractmethod can be called by subclasses """
        Jill = PartTime(7, 'Jill', 'Keane', 'jakekeane@gmail.com')
        self.assertEqual(Jill.job_type(), 'Part time')

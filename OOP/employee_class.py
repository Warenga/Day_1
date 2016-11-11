from abc import abstractmethod

class Employee():
	"""
	Super Class Employee initializes the attrbiutes:
		hours : number of hours employee works
		days : number of days employee works
		__weeklyPay : amount paid per month. This is set to private.
		employee_id : Employee's identification
		first_name : Employee's first name
		second_name : Employee's second name
		email : Employee's email
	"""

	hours = 0
	days = 0
	__weeklyPay = 0 

	def __init__(self, employee_id, first_name, second_name, email):
		self.employee_id = employee_id
		self.first_name = first_name
		self.second_name = second_name
		self.email = email

	def salary(self):
		"""
		Calculates the monthly salary of each employee
		"""
		self.__weeklyPay = (self.hours * self.days) * 200
		return self.__weeklyPay * 4

	@abstractmethod
	def job_type(self):
		"""
		Abstract method that can only be set by Sub classes
		"""
		return "Job type can only be set by SubClasses"

class PartTime(Employee):
	"""
	Sub class. It sets the hours and days of Part Time employees.
	Sets the correct job type
	"""

	hours = 5
	days = 4

	def job_type(self):
		return "Part time"

class FullTime(Employee):
	"""
	Sub class. It sets the hours and days of Full Time employees.
	Sets the correct job type
	"""

	hours = 8
	days = 6

	def job_type(self):
		return "Full time"

class Casual(Employee):
	"""
	Sub class. It sets the hours and days of Casual employees.
	Sets the correct job type
	"""

	hours = 0
	days = 0

	def job_type(Self):
		return "Casual Employee"












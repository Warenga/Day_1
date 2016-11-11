class Employee():

	hours = 0
	days = 0
	__pay = 0 

	def __init__(self, employee_id, first_name, second_name, email):
		self.employee_id = employee_id
		self.first_name = first_name
		self.second_name = second_name
		self.email = email

	def salary(self):
		self.__pay = (self.hours * self.days) * 200
		return self.__pay * 4

	def job_type(self):
		return "Job type set in subclass"

class PartTime(Employee):

	hours = 5
	days = 4

	def job_type(self):
		return "Part time"

class FullTime(Employee):

	hours = 8
	days = 6

	def job_type(self):
		return "Full time"

class Casual(Employee):

	hours = 0
	days = 0

	def job_type(Self):
		return "Casual Employee"










class Employee():

	hours = 0
	days = 0
	pay = 0

	def __init__(self, employee_id, first_name, second_name, email):
		self.employee_id = employee_id
		self.first_name = first_name
		self.second_name = second_name
		self.email = email

	def salary(self):
		self.pay = (self.hours * self.days) * 200
		return self.pay * 4

	def job_type(self):
		pass

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

Jake = Casual(7, 'Jake', 'Keane', 'jakekeane@gmail.com')
Jake.hours = 5
Jake.days = 5
print Jake.salary()
print Jake.job_type()






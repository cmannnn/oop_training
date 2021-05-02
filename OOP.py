class Employee:
	
	raise_amount = 1.04
	num_of_emp = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emp += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Gareth', 'Bale', 200000)
emp_2 = Employee('Test', 'User', 50000)
emp_3 = Employee('Test2', 'User2', 100)

print(Employee.num_of_emp)
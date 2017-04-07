# classes

class BankAccount:
	def __init__(self, bal, name):
		self.balance = bal
		self.name = name

	def greet_balance(self):
		print('hi {}, you have ${} '.format(self.name, self.balance))

	def withdrawal(self, amount):
		if self.balance - amount >= 0:
			self.balance -= amount
			print('You have withdrawn ${}. Your new balance is: {} '.format(amount, self.balance))
		else:
			print("You don't have enough money!")
		
	def deposit(self, much):
		self.balance += much
		print('Your new balance = {} '.format(self.balance))

chris = BankAccount(100, "Chris")
katie = BankAccount(20, "Katie")
chris.greet_balance()
katie.greet_balance()
chris.withdrawal(int(input('Withdraw how much? ')))
chris.deposit(int(input('Deposit how much? ')))


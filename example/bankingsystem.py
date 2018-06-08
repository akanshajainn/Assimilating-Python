from abc import ABCMeta, abstractmethod
from random import randint

class SavingsAccount(metaclass = ABCMeta):


	@abstractmethod
	def createSavingAccount():
		return 0
	
	@abstractmethod
	def authenticate():
		return 0

	@abstractmethod
	def withdraw():
		return 0

	@abstractmethod
	def deposit():
		return 0

	@abstractmethod
	def display():
		return 0


class Bank(SavingsAccount):


	def __init__(self):
		# accounts dictionary has key as account number and value 0 is name and value 1 is balance
		# for ex; accounts{12345:'abc', 54321}
		self.accounts = {}

	def createSavingAccount(self, name, initialDeposit):
		new_account_number = randint(10000, 99999)  # randint is inclusive at both ends
		self.accounts[new_account_number] = [name, initialdeposit]
		print("Account created successfully, your account nuber is {}".format(new_account_number))

	
	def authenticate(self, name, accountNum):
		if accountNum in self.accounts.keys():
			if name in self.accounts[accountNum][0]:
				self.accountNum= accountNum
				print('User Validated')
				return True
		else: 
			print('Account Not Found.. Try again')

	
	def withdraw(self, withdrawalAmmount):
		if withdrawalAmmount > self.accounts[self.accountNum][1]:
			print('Balance Insufficient')
		else:
			self.accounts[self.accountNum][1] -= withdrawalAmmount
			print("Withdraw successful...")
			self.display()

	
	def deposit(self, depositAmount):
		self.accounts[self.accountNum][1] += depositAmount
		print("Deposit successful...")
		self.display()


	def display(self):
		print("Available balance is {}".format(self.accounts[self.accountNum][1]))

	
		

trans = Bank()
while True:
	print("Enter your choice for banking services:")
	print("1. Create New Saving Account")
	print("2. Access Exisitng Account")
	print("3. Exit")
	Usrchoice = int(input())

	if Usrchoice is 1:
		print("Enter your name:")
		name = input()
		print("Enter your initial deposit:")
		initialdeposit = int(input())
		trans.createSavingAccount(name, initialdeposit)

	elif Usrchoice is 2:
		print("Enter your name:")
		name = input()
		print("Enter your account number:")
		accno = int(input())
		print("Accessing account")
		authenticationStatus = trans.authenticate(name, accno)
		if authenticationStatus is True:
			while True:
				print("Enter your choice")
				print("1. Withdraw")
				print("2. Deposit")
				print("3. Display balance")
				print("4. Go back")
				choice = int(input())
				if choice is 1:
					print("Enter how much you need to withdraw")
					takeamnt = int(input())
					trans.withdraw(takeamnt)
				if choice is 2:
					print("Enter how much you need to deposit")
					putamnt = int(input())
					trans.deposit(putamnt)
				if choice is 3:
					trans.display()
				if choice is 4:
					break
		else:
			continue
	elif Usrchoice is 3:
		print("Thank you for choosing our services. Have a nice day!")
		quit()
			
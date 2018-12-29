
# Class- defines the characteristics of an objec that will be created
class Account:

    def __init__(self, filepath):
        # Instance variables- variables defined within the methods of a class
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer_to_other_account(self, amount):
        self.balance = self.balance - amount - self.fee
 
# Object instance 
checking = Checking("balance.txt", 1)
checking.transfer_to_other_account(10)
print(checking.balance)
checking.commit()

# Class variables are shared by all instances of that class 
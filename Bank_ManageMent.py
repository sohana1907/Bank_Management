class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        account_number = len(self.users) + 1
        user = User(name, email, address, account_type, account_number)
        self.users[account_number] = user
        return user

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]

    def get_all_accounts(self):
        return self.users

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled


class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.loan_taken = False
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if not self.loan_taken:
            self.balance += amount
            self.loan_taken = True
            self.transaction_history.append(f"Loan Taken: {amount}")
        else:
            print("Loan already taken")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to Account Number {recipient.account_number}")
        else:
            print("Insufficient balance")

    def __repr__(self):
        return f"User: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}"


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def get_all_accounts(self):
        return self.bank.get_all_accounts()

    def get_total_balance(self):
        return self.bank.get_total_balance()

    def get_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()


bank = Bank()
admin = Admin(bank)

user1 = admin.create_account("John", "john@example.com", "123 Main St", "Savings")

user1.deposit(1000)


user1.withdraw(500)

print(user1.check_balance())

user1.take_loan(200)

user2 = admin.create_account("Alice", "alice@example.com", "456 Elm St", "Current")
user1.transfer(300, user2)


admin.delete_account(user1.account_number)

print(admin.get_total_balance())
print(admin.get_total_loan_amount())


# class BankAccount:
#     def __init__(self, int_rate, balance):
#         self.int_rate=.01
#         self.account_balance=0
#     def deposit(self, amount):
#         # increases the account balance by the given amount
#         self.account_balance += amount
#         return self
#     def withdrawal(self, amount):
#         # decreases the account balance by the given amount if there are sufficient funds
#         # if there is not enough money, print a message: "insufficient funds: Charging a $5 fee and deduct $5"
#         if self.account_balance - amount < 0:
#             print(f"Insufficient Funds: Charging a $5 fee")
#             self.account_balance -= 5
#         else: 
#             self.account_balance -= amount
#             return self
#     def display_account_info(self):
#         print(f"Balance: ${self.account_balance}")
#         return self
#     def yield_interest(self):
#         # increases the account balance by the current balance * the interest rate
#         if self.account_balance > 0:
#             new_bal = self.account_balance + (self.account_balance * self.int_rate)
#             return self

# class User:
#     def __init__(self, name, email, int_rate=0, balance=0):
#         self.name=name 
#         self.email=email
#         self.account=BankAccount(int_rate, balance)
#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         return self
#     def make_withdrawal(self, amount):
#         self.account.withdrawal(amount)
#         return self
#     def display_user_balance(self):
#         print(f"User:{self.name}, Email: {self.email}")
#         self.account.display_account_info()
#         return self


# user1 = User("Adam", "adam@gmail.com")
# user2 = User("Deanna", "deanna@gmail.com")
# user3 = User("Tom", "tom@me.com")

# user1.make_deposit(500).display_user_balance().make_deposit(400).display_user_balance().make_withdrawal(800).display_user_balance()
# user2.make_deposit(2000).make_withdrawal(200)
# user2.display_user_balance()
# user2.account.yield_interest()
# user2.display_user_balance()





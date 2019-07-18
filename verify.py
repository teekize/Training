class Verification:
    def __init__(self, email, password):
        self.email_=email
        self.password=password

    def password_strength(self):
        if len(self.password)<= 6:
            return "password must contain 7-8 charcters"
        return f"Your password {password} is very strong"

    def email_m(self):
        if "@" in self.email_:
            return "Valid email"
        return "Invalid email"

class BankAcc(Verification):
    def __init__(self, name, number,email, password):
        super( ).__init__(email,password)
        self.name=name
        self.number=number
        self.balance=0
        
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance=self.balance +amount
        return f"You have deposited {amount} new balance is {self.balance}"
    
    def withdraw(self, amount):
       self.balance =self.balance-amount
       return f"your request to withdraw {amount} has been approved new balance is {self.balance}"


ken = BankAcc ("ken muia", 7987545154,"ken@gmil.com", "teekalemein")
password=ken.password
print(password)

password_acc=ken.password_strength()
print(password_acc)

balance =ken.check_balance()
print(balance)

# pass_ =ken.deposit(1000)
# print(pass_)

# mail =ken.check_balance()
# print(mail)

# pass_ =ken.deposit(2000)
# print(pass_)
# w =ken.withdraw(100)
# print(w)
# mail =ken.check_balance()
# print(mail)
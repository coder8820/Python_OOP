# Create Account class with 2 attributes balance and Account-no
# Create Methods for debit and credit and printing the balance

class Account:
    def __init__(self, bal, acc,name,passw):
        self.name = name
        self.passw = passw
        self.bal = bal
        self.acc = acc

    
    # Debet method
    def debit(self, amount):
        print("This is your Debit Section")
        if(self.name == 'admin' and self.passw == 'admin'):
            self.bal -= amount
            print("Rs: ",amount, " was debited from your account")
            print("Total amount: ",self.get_balance())
        else:
            print("user name and password are wrong")
    
    # Credtit method
    def credit(self, amount):
        print("This is your Credit Section")
        if(self.name == "admin" and self.passw == 'admin'):
            self.bal += amount
            print("Rs",amount," are credited in your account")
            print("Total amount: ",self.get_balance())
        else:
            print("User name and passord incorrect ")

    def get_balance(self):
        return self.bal
    


name = input(" user name: ")
passward = input(" password: ")
amount = int(input("do you want to debit: "))
amount1 = int(input("do you want to credit: "))
print("Welcome ")
acc1 = Account(10000, 1234, name, passward)
acc1.debit(amount)
acc1.credit(amount1)


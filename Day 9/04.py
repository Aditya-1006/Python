class Bank:

    def __init__(self, BankName, acc_balance):
        self.BankName = BankName
        self.acc_balance = acc_balance

    def getStatus(self):
        print(f"The Bank Name = {self.BankName}")
        print(f"The Acc Balance = {self.acc_balance}")
        print("============================\n")


    def deposite(self, amount):
        self.acc_balance = self.acc_balance + amount
        print("Your amount has been Credited!")
        print("============================\n")
    

    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance = self.acc_balance - amount
            print("Your amount has been debited")
            print("============================\n")
        else:
            print("Insufficient Amount")



b1 = Bank("HDFC", 1000)
b1.getStatus()


b1.deposite(int(input("Enter Amount to Deposite: ")))
b1.getStatus()


b1.withdraw(int(input("Enter Amount to Withdraw: ")))
b1.getStatus()
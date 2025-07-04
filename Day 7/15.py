class Bank:
    BankName = "HDFC"

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



b1 = Bank()
b1.acc_balance = 100
b1.getStatus()


b1.deposite(500)
b1.getStatus()


b1.withdraw(200)
b1.getStatus()
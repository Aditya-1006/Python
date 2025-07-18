class Company:

    def __init__(self, name, designation, subnet):
        self.name = name
        self.designation = designation
        self.subnet = subnet

    def getInfo(self):
        print(f"The Name is = {self.name}")
        print(f"The Designation is = {self.designation}")
        print(f"The Subnet is = {self.subnet}")

c1 = Company("Aditya", "Analyst", "Student")
c1.getInfo()

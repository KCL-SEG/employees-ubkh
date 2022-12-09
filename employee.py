"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commision = commission

    def get_pay(self):
        pay = self.contract.get_amount()
        if self.commision != None:
            pay += self.commision.get_amount()
        return pay

    def __str__(self):
        final_string = '. Their total pay is ' + str(self.get_pay()) + '.'
        string = self.name + ' works on a ' + str(self.contract)
        if self.commision == None:
            return string + final_string
        return string + ' ' + str(self.commision) + final_string

class SalaryContract:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def __str__(self):
        return 'monthly salary of ' + str(self.get_amount())
        
class HourlyContract:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def get_amount(self):
        return self.hours*self.rate

    def __str__(self):
        return 'contract of ' + str(self.hours) + ' hours at ' + str(self.rate) + '/hour'

class BonusCommission:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def __str__(self):
        return 'and receives a bonus commission of ' + str(self.get_amount())

class ContractCommission:
    def __init__(self, contract_count, rate):
        self.contract_count = contract_count
        self.rate = rate

    def get_amount(self):
        return self.contract_count*self.rate

    def __str__(self):
        return 'and receives a commission for ' + str(self.contract_count) + ' contract(s) at ' + str(self.rate) + '/contract'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_contract = SalaryContract(4000)
billie = Employee('Billie', billie_contract, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_contract = HourlyContract(100, 25)
charlie = Employee('Charlie', charlie_contract, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract = SalaryContract(3000)
renee_commission = ContractCommission(4, 200)
renee = Employee('Renee', renee_contract, renee_commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract = HourlyContract(150, 25)
jan_commission = ContractCommission(3, 220)
jan = Employee('Jan', jan_contract, jan_commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_contract = SalaryContract(2000)
robbie_commission = BonusCommission(1500)
robbie = Employee('Robbie', robbie_contract, robbie_commission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_contract = HourlyContract(120, 30)
ariel_commission = BonusCommission(600)
ariel = Employee('Ariel', ariel_contract, ariel_commission)

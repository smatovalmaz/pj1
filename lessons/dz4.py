class SavingAccount:
    pass
class ChekingAccount:
    pass
class Stock:
    pass
class Bond:
    pass
class RealEstate:
    pass

class BankAccount(SavingAccount,ChekingAccount):
    pass

class Security(Stock,Bond):
    pass

class InterestBearingItem(BankAccount,Security):
    pass

class Asset(BankAccount,RealEstate,Security):
    pass

class InsurableItem(BankAccount,RealEstate):
    pass
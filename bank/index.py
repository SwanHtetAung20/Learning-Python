from bank_accounts import *

MgMg = BankAccount("Mg Mg", 1000)
SuSu = BankAccount("Su Su", 2000)

MgMg.get_balance()
SuSu.get_balance()

MgMg.deposit(500)
SuSu.deposit(1000)

MgMg.withdraw(10000)
MgMg.withdraw(900)

MgMg.transfer(SuSu, 500)

ZawGyi = InterestRewardsAccount("Zaw Gyi", 3000)

ZawGyi.get_balance()

ZawGyi.deposit(1000)

ZawGyi.transfer(SuSu, 2000)

KyawGyi = SavingsAccount("Kyaw Gyi", 5000)

KyawGyi.get_balance()

KyawGyi.deposit(2000)

KyawGyi.transfer(SuSu, 1000)

KyawGyi.withdraw(1000)
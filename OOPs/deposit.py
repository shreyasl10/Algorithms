class Account:
  def __init__(self,acc_no,name,balance):
    self.acc_no=acc_no
    self.name=name
    self.balance=balance
  def deposit_money(self,dep_amnt):
    self.balance=self.balance+dep_amnt
    return self.balance
  def withdraw_money(self,with_amnt):
    self.balance=self.balance-with_amnt
    if self.balance<1000:
      return f"insufficient amount"
    else:
      return f"output-{self.balance}"
accno=int(input())
name=input()
balance=int(input())
acc=Account(accno,name,balance)
depamnt=int(input())
withamnt=int(input())
print(acc.deposit_money(depamnt))
print(acc.withdraw_money(withamnt))

  
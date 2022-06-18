class Employee:
  def __init__(self,emp_no,empname,leaves):
    self.emp_no=emp_no
    self.empname=empname
    self.leaves=leaves
class Company():
  def __init__(self,cname,emps):
    self.cname=cname
    self.emps=emps
  def leave_available(self,emp_no,types):
    for i in self.emps:
      if i.emp_no==emp_no:
        return i.leaves[types]
  def leave_permission(self,emp_no,types,num):
    for i in self.emps:
      if i.emp_no==emp_no:
        if i.leaves[types]>=num:
          return "Granted"
        else:
          return "Rejected"
n=int(input())
emp=list()
for i in range(n):
  empno=int(input())
  name=input()
  a=int(input())
  b=int(input())
  c=int(input())
  leaves={'a':a,'b':b,'c':c}
  emp.append(Employee(empno,name,leaves))
c=Company('ABC',emp)
empid=int(input())
types=input()
num=int(input())
print(c.leave_available(empid,types))
print(c.leave_permission(empid,types,num))
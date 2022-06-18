class Student:
  def __init__(self,name,sub1,sub2,sub3):
    self.name=name
    self.sub1=sub1
    self.sub2=sub2
    self.sub3=sub3
  def CalculateResult(self):
    average=0
    if self.sub1>40 and self.sub2>40 and self.sub3>40:
      average=(self.sub1+self.sub2+self.sub3)/3
      return average
class School:
  passedList=[]
  def __init__(self,name,students):
    self.name=name
    self.students=students
  def getStudentResult(self):
    for i in self.students.keys():
      if i.CalculateResult()>60:
        self.students[i]='PASS'
        self.passedList.append(i.name)
      else:
        students[i]='FAIL'
    if len(self.passedList)==0:
      return "No students passed"
    return self.passedList
  def findStudentWithHighestMarks(self):
    avgs=[]
    for i in self.students:
        avg=i.CalculateResult()
        avgs.append(avg)
    m=max(avgs)
    for i in self.students:
      if i.CalculateResult()==m:
        return i.name
n=int(input())
students=list()
for i in range(n):
  name=input()
  sub1=int(input())
  sub2=int(input())
  sub3=int(input())
  students.append(Student(name,sub1,sub2,sub3))
d={s:None for s in students}
s=School('ABC',d)
print(s.getStudentResult())
print(f"\nStudent with highest score is {s.findStudentWithHighestMarks()}")


    
    


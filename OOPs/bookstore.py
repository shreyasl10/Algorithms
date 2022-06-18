class Book:
  def __init__(self,id,name,tech,price,author):
    self.id=id
    self.name=name
    self.tech=tech
    self.price=price
    self.author=author

class Bookstore:
  def __init__(self,bookdb,name):
    self.bookdb=bookdb
    self.storename=name
  def searchByName(self,name):
    result=[]
    for i in self.bookdb.keys():
      if self.bookdb[i].name==name:
        result.append(self.bookdb[i])
    return result
  def calculatePriceByTechnology(self,tech):
    s=0
    for i in self.bookdb.keys():
      if self.bookdb[i].tech==tech:
        s+=self.bookdb[i].price
    if s==0:
      return 0
    s-=(s*10)/100
    return s
n=int(input())
books={}
for i in range(n):
  id=int(input())
  name=input()
  tech=input()
  price=int(input())
  author=input()
  books[id]=Book(id,name,tech,price,author)
store=Bookstore(books,'ABC')
bookname=input()
tech=input()
result=store.searchByName(bookname)
if result:
  for i in result:
    print(i.id)
    print(i.name)
    print(i.tech)
    print(i.price)
    print(i.author)
else:
  print("No book Exists with the BookName")
output=store.calculatePriceByTechnology(tech)
if output!=0:
  print(output)
else:
  print("0.0")
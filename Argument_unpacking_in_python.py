#transaction = [
#    (20, "checking"),
#    (30,"checking"),
#    (40, "saving"),
#    (50,"checking"),
#    (60,"saving")
#]

#for t in transaction:
 #   print(t[0], *t)
 
class Employee:
    no_of_leaves = 8
    
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        
    def printdetails(self):
        return (f"{self.name}, salary is {self.salary} and role is {self.role}")
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
        
harry = Employee("Amar", 9000, "Data")

#(harry.change_leaves(14)) #class method ko kisi instance ya kisi class se access kar skte hain.
(Employee.change_leaves(14))

#Employee.no_of_leaves = 34

print(harry.no_of_leaves)


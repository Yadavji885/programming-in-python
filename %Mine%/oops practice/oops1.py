class Example:
    company = "Microsoft"

    def __init__(self,name,subunit,salary,experience):
        self.name = name
        self.subunit = subunit
        self.salary = salary
        self.experience = experience

    def Employee(self):
        print(f"Name is {self.name}")
        print(f"Subunit is {self.subunit}")
        print(f"Salary is {self.salary}")
        print(f"Expierence is {self.experience}")

a = Example("Jatin Yadav", "Office" , 500000 , 20)
a.Employee()
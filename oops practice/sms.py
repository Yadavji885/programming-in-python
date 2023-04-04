class SMS:

    def __init__(self, name ,rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def Add (self):
        with open('sms.txt' , 'a') as f:
            sms = f.write(f"Name = {self.name}\nRoll number = {self.rollno}\nMarks in First semester = {self.m1}\nMarks in second semester = {self.m2}\n\n")
            print(sms)

    def Update(self):
        rollno = int(input("Enter your roll no : \n"))
        for i in range():
            if i == rollno:
                print("cvjxv j bvx  ")
            
a = SMS("Jatin Yadav",54321,94,96)
a.Add()
a.Update()
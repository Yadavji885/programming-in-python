class KBC:
    def __init__(self,name):
        self.name = name
        
    def q(self):
        #question 1
        print("What is the capital of France?\nA) Berlin\nB) Madrid\nC) Paris\nD) Rome")
        answer1 = "Paris"
        ans1 = input("Enter the answer which you would like to lock:\n")
        if ans1 == answer1:
            print(f"{self.name} won 1000")
        else:
            afsos = print(f"You are wrong, The answer is {answer1}")
            print(f"{self.name} is going with 0 money as reward")
            return afsos
        #question 2
        print("Which planet is known as the Red Planet?\nA) Jupiter\nB) Mars\nC) Venus\nD) Saturn")
        answer2 = "Mars"
        ans2 = input("Enter the answer which you would like to lock:\n")
        if ans2 == answer2:
            print(f"{self.name} won 2000")
        else:
            afsos = print(f"You are wrong, The answer is {answer2}")
            print(f"{self.name} is going with 1000 money as reward")
            return afsos
        #quetion 3
        print("If a car travels at a constant speed of 60 miles per hour, how far will it travel in 3 hours?\nA) 30 miles\nB) 90 miles\nC) 120 miles\nD) 180 miles")
        answer3 = "120 miles"
        ans3 = input("Enter the answer which you would like to lock:\n")
        if ans3 == answer3:
            print(f"{self.name} won 3000")
        else:
            afsos = print(f"You are wrong, The answer is {answer3}")
            print(f"{self.name} is going with 2000 money as reward")
            return afsos
        #question 4
        print("Who is considered the Father of Modern Physics?\nA) Albert Einstein\nB) Isaac Newton\nC) Galileo Galilei\nD) Stephen Hawking")
        answer4 = "Albert Einstein"
        ans4 = input("Enter the answer which you would like to lock:\n")
        if ans4 == answer4:
            print(f"{self.name} won 5000")
        else:
            afsos = print(f"You are wrong, The answer is {answer4}")
            print(f"{self.name} is going with 3000 money as reward")
            return afsos
        #question 5
        print("In which year was the United Nations founded?\nA) 1942\nB) 1945\nC) 1951\nD) 1960")
        answer5 = 1945
        ans5 = input("Enter the answer which you would like to lock:\n")
        if ans5 == answer5:
            print(f"{self.name} won 10000")
        else:
            afsos = print(f"You are wrong, The answer is {answer5}")
            print(f"{self.name} is going with 5000 money as reward")
            return afsos

kbc = KBC("Jatin Yadav")
kbc.q()

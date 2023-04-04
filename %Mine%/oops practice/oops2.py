class Calculator :
    def Square(self):
        no = int(input("Enter any number for finding a square : \n"))
        square = no**2
        print(square)

    def Squareroot(self):
        no = int(input("Enter any number for finding a squareroot : \n"))
        squareroot = no**0.5
        print(squareroot)

    def cube(self):
        no = int(input("Enter any number for finding a cube : \n"))
        cube = no**3
        print(cube)

a = Calculator()
a.Square()
a.Squareroot()
a.cube()
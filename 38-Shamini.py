class CalUtils:
    def __init__ (self):
        self.names = []
        self.heights = []
        self.totalStudentHeight = 0
        self.totalStudentCount = 0
        self.avg = 0.0


    def calAvgHeight(self):
        print ("Name: " , "Height: ")
        with open("ListOfStudents.txt", "r")as f:
            for line in f:
                f = line.split("\t")
                name = f[0]
                height = f[1]
                self.names.append(str(name))
                self.heights.append(float(height))
            self.totalStudentCount = len(self.names)
            self.totalStudentHeight = sum(self.heights)
            avg = round(self.totalStudentHeight / self.totalStudentCount,2)
            print(f'{avg} meters')


        A = (input("Do you want to add new students to the list [ Y / N ] ?"))
        if A == "N":
            print(str(round(self.totalStudentHeight / self.totalStudentCount, 2)) + " " + "meters")
            exit()
        else :
            y = (input ("Enter Student's Name: "))
            z = float(input ("Enter Student's Height: "))
            with open ("ListOfStudents.txt" , "a") as f:
                f.write ("\n" + y + "\t" + str(z))
                self.names = []
                self.heights = []
                self.totalStudentHeight = 0
                self.totalStudentCount = 0
                self.avg = 0.0

                self.calAvgHeight()
Final = CalUtils()
Final.calAvgHeight()

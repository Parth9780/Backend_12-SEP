# What relationship is appropriate for Course and Faculty? 

class Faculty: #parent class
    def subject(self):
        print("The faculty is python..")

class Course (Faculty): #sub/child class
    def chapter(self):
        print("The Course is full-stack python..")

fc = Course() # object creat
fc.subject()
fc.chapter()

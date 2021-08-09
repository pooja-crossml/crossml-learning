class Training:
    # constructer
    def __init__(self, name, course):
        self.name= name
        self.course = course

    def display(self, name="kavita"):
        print(f"{self.name} wants to register for {self.course} course.") 
    

name,course= input("Enter your name and course preference.").split()
new_training = Training("meera", course)
new_training.display()
old_training = Training(name, course)
old_training.display()
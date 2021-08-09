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
# delete properties of the class
#del old_training.course #AttributeError: 'Training' object has no attribute 'course' error once we delete course

# delete class obj using del
#del old_training # NameError: name 'old_training' is not defined after deleting the object of the class.

old_training.display()

# Entering multiple values for a list 
# ls= [int(x) for x in input("Enter values for list").split()]
# print(ls)

# self parameter is a reference to the current instance of the calss.and is used to access variables that belongs to the class


# class Person:
     

#     def display(self):
#         print("Name:",self.name )

# class Student(Person):
#     def __init__(self, name, roll):

#         self.roll = roll
#         self.name=name

#     def show(self):
#         print("Roll:", self.roll)

# s = Student("Al-Amin", 101)
# s.display()
# s.show()







# class Demo:
#     def __init__(self):
#         print("Object Created")

# d = Demo()


class Demo:
    def __del__(self):
        print("Object Destroyed")

d = Demo()
del d

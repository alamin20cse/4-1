class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"
    
class Got:
    def  sound(self):
        return "Bhyaaaa"
        

for animal in [Cat(), Dog(),Got()]:
    print(animal.sound())

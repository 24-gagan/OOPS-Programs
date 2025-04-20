class Bird:
    def sound(self):
        print("Bird chirps")
class Cat:
    def sound(self):
        print("Cat meows")
def make_sound(animal):
    animal.sound()
b=Bird()
c=Cat()
make_sound(b)
make_sound(c)
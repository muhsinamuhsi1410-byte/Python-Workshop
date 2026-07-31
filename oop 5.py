#pet store(inheritance and polimorphism)

class Animal:
    def speak(self):
        print("....")
class Dog:
    def speak(self):
        print("Woof")
class Cat:
    def speak(self):
        print("Meow")
dog=Dog()
cat=Cat()
dog.speak()
cat.speak()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent constructor
        self.color = color

    def speak(self):
        super().speak()  # Call parent method
        print(f"{self.name} meows")

cat = Cat("Whiskers", "White")
cat.speak()
  
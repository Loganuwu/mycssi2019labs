pet = {
  "name": "Doggo",
  "animal": "dog",
  "species": "labrador",
  "age": 5
}

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"

    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much" % self.name)
            self.mood = "Lethargic"

    def move(self):
        print(">  after flying %s is %s " % self.name, self.is_hungry)



# Initialize a new instance of pet, with a name of "Fido" and an age of 3.
my_pet = Pet("Fido", 3, "dog")
print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)
# This should print `My pet Fido is 3 years old`.

my_pet2 = Pet("Cooper", 6, "dog")
print("My pet %s is %s years old" % (my_pet2.name, my_pet2.age))

my_pet3 = Pet("Shadow", 12, "dog")
print("My pet %s is %s years old" % (my_pet3.name, my_pet3.age))

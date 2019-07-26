num = int(raw_input("Enter a number: "))
if num > 0:
        print("That's a positive number!")
        print("good job :D")
elif num < 0:
        print("That's a negative number!")
else:
        print("Zero is neither positive nor negative")


my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"

print(
"My name is %s and my friends are %s, %s, and %s" %
(my_name, friend1, friend2, friend3)
)

name = "Logan"
age = 18
print("My name is %s and I'm %s years old." % (name,age))


def greetAgent(first_name, last_name):
    print("%s. %s %s. " % (last_name, first_name, last_name))

greetAgent("Logan","Barajas")

x = 1
while x <= 5:
    print(x)
    x = x +1

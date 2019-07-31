# print every element in the array and removes only the first javi, making it alice, damien, javi
students = ["Alice", " Javi", " Damien", "Javi"]
students.remove("Javi")
print(students)

# for loop that adds smith to each element
smith_siblings = ["Emily", "Monique", "Giovanni"]
smith_siblings.append("Logan")
smith_siblings.append("Ethan")
smith_siblings.append("Connor")

for name in smith_siblings:
    print(name + " Smith")

print(len(smith_siblings))

for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
print (smith_siblings)

superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
print(superheroes)
demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))

if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes:", superheroes)
else:
    print("Hero not found.")

names  = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
print(names[::-1]) #prints backwards Robb Jon Sansa Arya Bran Rickon
print(names[4:2:-1]) # reversed list, starting at index 4 and continues to 2 but does not print 2, prints Jon Sansa
print(names[::2])

states = {
    "NY": "New York",
    "CA": "California",
    "TX": "Texas",
    "AZ": "Arizona",
    "CO": "Colorado",
    "OH": "Ohio"
}

for abbreviation in states:
    print(abbreviation + " is short for " + states[abbreviation])

stateInput = str(raw_input("Enter a state abbreviation "))

if stateInput == abbreviation:
    print("Hi")

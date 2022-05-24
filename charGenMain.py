# Todo
# 1. Make a python script that generates a random fantasy character
# 2. Generator to a text File
# 3. Generate name, surname, race, gender, age, class, and a short bio
# 4. A short bio should be randomly generated.
# 5. Add GRAPHICS WOW

import random 
import mainNames
import races
import classes
import charBios

firstName = ""
lastName = random.choice(mainNames.lastNames)
gender = random.choice(["Male", "Female"])
race = random.choice(races.races)
age = None
charClass = random.choice(classes.classes)
parents = random.choice(charBios.parents)
earlyLife = random.choice(charBios.earlyLife)
adulthood = random.choice(charBios.adulthood)

if gender == "Male":
    firstName = random.choice(mainNames.maleNames)
elif gender == "Female":
    firstName = random.choice(mainNames.femaleNames)

if race == "Human":
    age = random.randrange(20, 80)
elif race == "Halfling":
    age = random.randrange(20, 75)
elif race == "Gnome":
    age = random.randrange(20, 90)
elif race == "Dwarf":
    age = random.randrange(20, 180)
elif race == "Elf":
    age = random.randrange(20, 300)

print("First Name:", firstName)
print("Last Name:", lastName)
print("Gender:", gender)
print("Race:", race)
print("Age:", age)
print("Class:", charClass)
print("Bio:", "{} {}'s".format(firstName, lastName), '{}'.format(parents), '\n    ', "{}'s".format(firstName), "{}".format(earlyLife), "\n    ", "{}'s".format(firstName), "{}".format(adulthood))

with open('{} {}.txt'.format(firstName, lastName), 'w') as c:
    c.write("This is the info page for {} {}.".format(firstName, lastName) + "\n")
    c.writelines(["First Name: ", firstName, '\n', "Surname: ", lastName, '\n', "Gender: ", gender, '\n', "Race: ", race, '\n', "Age: ", str(age), '\n', "Class: ", charClass, '\n', "Bio: ", "{} {}'s ".format(firstName, lastName), '{}'.format(parents), '\n    ', " {} ".format(firstName), "{}".format(earlyLife), "\n    ", " {} ".format(firstName), "{}".format(adulthood)])
    

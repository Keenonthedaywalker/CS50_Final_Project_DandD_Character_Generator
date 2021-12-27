from tkinter import Tk, Label, Button, messagebox, Entry
from tkinter.tix import *
import random

# TODO: Add 2 options at start. Manual generation, which lets the user create their own character however they want.
#                               Random Generation, which generates a completely random character for the user.

race = ""
maleFemale = ""
firstname = ""
lastname = ""
age = 0
charClass = ""
animalname = ""
animalClass = ""
invTest = False

# The main program class
class theGUI:
    def __init__(self, master):
        self.master = master
        master.title = "Test"
        
        self.introLabel = Label(master, text="Please select how you would like to generate your character from one of the two options below. \nManual will let you choose every detail about your character. \nRandom will randomly generate every detail of your character for you.")
        self.introLabel.pack()
        
        self.button1 = Button(master, text="Manual", font=('Fantasy', 10), command=self.manualGen)
        self.button1.pack()
        
        self.button2 = Button(master, text="Random", font=('Fantasy', 10), command=self.randomGen)
        self.button2.pack()
    
    # Function for manual generation
    def manualGen(self):
        self.introLabel.destroy()
        self.button1.destroy()
        self.button2.destroy()
        
        self.manualIntro = Label(self.master, text="Great! On the following pages you will be asked quetions about your character.")
        self.manualIntro.pack()
        
        self.raceButton = Button(self.master, text="Races", command=self.races)
        self.raceButton.pack()
    
    # Funcion for races
    def races(self):
        global race
    
        self.manualIntro.destroy()
        self.raceButton.destroy()
        
        self.raceIntro = Label(self.master, text="Please press one of the buttons below to select your character's race. \nHover over a button to get information on a race.")
        self.raceIntro.pack()
        
        self.humanButton = Button(self.master, text="Human", command=self.humanRace)
        self.humanButton.pack()
        
        humanInfo = Balloon(self.master)
        humanInfo.bind_widget(self.humanButton, balloonmsg="Humans are the most adaptable and ambitious people among the common races. \nWhatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.")
        
        self.elfButton = Button(self.master, text="Elf", command=self.elfRace)
        self.elfButton.pack()
        
        elfInfo = Balloon(self.master)
        elfInfo.bind_widget(self.elfButton, balloonmsg="Elves are a magical people of otherworldly grace, living in the world but not entirely part of it.")
        
        self.dwarfButton = Button(self.master, text="Dwarf", command=self.dwarfRace)
        self.dwarfButton.pack()
        
        dwarfInfo = Balloon(self.master)
        dwarfInfo.bind_widget(self.dwarfButton, balloonmsg="Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.")
        
        self.halflingButton = Button(self.master, text="Halfling", command=self.halflingRace)
        self.halflingButton.pack()
        
        halflingInfo = Balloon(self.master)
        halflingInfo.bind_widget(self.halflingButton, balloonmsg="The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.")
        
        self.halforcButton = Button(self.master, text="Half-Orc", command=self.halforcRace)
        self.halforcButton.pack()
        
        halforcInfo = Balloon(self.master)
        halforcInfo.bind_widget(self.halforcButton, balloonmsg="Half-orcs’ grayish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering builds make their orcish heritage plain for all to see.")
        
        # If race is equal to one of the races destroy the following
        if race == "Human" or race == "Elf" or race == "Dwarf" or race == "Halfling" or race == "Half-Orc":
            self.infoText1.destroy()
            self.nextButton.destroy()
            self.backButton.destroy()

    # Human function
    def humanRace(self):
        global race
        race = "Human"
        
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        
        self.infoText1 = Label(self.master, text="You're character is a " +  race + "\nDo you want to continue with the character creation?")
        self.infoText1.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.gender)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.races)
        self.backButton.pack()
    
    # Elf function
    def elfRace(self):
        global race
        race = "Elf"
        
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        
        self.infoText1 = Label(self.master, text="You're character is a " +  race + "\nDo you want to continue with the character creation?")
        self.infoText1.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.gender)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.races)
        self.backButton.pack()
        
    # Dwarf function
    def dwarfRace(self):
        global race
        race = "Dwarf"
        
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        
        self.infoText1 = Label(self.master, text="You're character is a " +  race + "\nDo you want to continue with the character creation?")
        self.infoText1.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.gender)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.races)
        self.backButton.pack()
    
    # Halfling function
    def halflingRace(self):
        global race
        race = "Halfling"
        
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        
        self.infoText1 = Label(self.master, text="You're character is a " +  race + "\nDo you want to continue with the character creation?")
        self.infoText1.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.gender)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.races)
        self.backButton.pack()
    
    # Half-Orc function
    def halforcRace(self):
        global race
        race = "Half-Orc"
        
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        
        self.infoText1 = Label(self.master, text="You're character is a " +  race + "\nDo you want to continue with the character creation?")
        self.infoText1.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.gender)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.races)
        self.backButton.pack()
        
    def gender(self):
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        self.infoText1.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        
        self.genderIntro = Label(self.master, text="What is your character's gender?")
        self.genderIntro.pack()
        
        self.maleButton = Button(self.master, text="Male", command=self.male)
        self.maleButton.pack()
        
        self.femaleButton = Button(self.master, text="Female", command=self.female)
        self.femaleButton.pack()
        
        if maleFemale == "Male" or maleFemale == "Female":
            self.infoText2.destroy()
            self.nextButton.destroy()
            self.backButton.destroy()
        
    def male(self):
        global maleFemale
        maleFemale = "Male"
    
        self.genderIntro.destroy()
        self.maleButton.destroy()
        self.femaleButton.destroy()
        
        self.infoText2 = Label(self.master, text="You're character is a " + maleFemale + "\nDo you want to continue with the character creation?")
        self.infoText2.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.charName)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.gender)
        self.backButton.pack()
        
        
    def female(self):
        global maleFemale
        maleFemale = "Female"
    
        self.genderIntro.destroy()
        self.maleButton.destroy()
        self.femaleButton.destroy()

        self.infoText2 = Label(self.master, text="You're character is a " + maleFemale + "\nDo you want to continue with the character creation?")
        self.infoText2.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.charName)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.gender)
        self.backButton.pack()
        
    def charName(self):
        self.raceIntro.destroy()
        self.humanButton.destroy()
        self.elfButton.destroy()
        self.dwarfButton.destroy()
        self.halflingButton.destroy()
        self.halforcButton.destroy()
        self.infoText2.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        
        self.nameIntro = Label(self.master, text="Now, please enter your character's name.")
        self.nameIntro.pack()
        
        self.firstName = Label(self.master, text="First Name: ")
        self.firstName.pack()
        
        self.entry1 = Entry(self.master)
        self.entry1.pack()
        
        self.lastName = Label(self.master, text="Last Name: ")
        self.lastName.pack()
        
        self.entry2 = Entry(self.master)
        self.entry2.pack()
        
        self.nameConfirm = Button(self.master, text="Confirm Name", command=self.continueToCharAge)
        self.nameConfirm.pack()
    
    # Confirm name function
    def continueToCharAge(self):
        global firstname, lastname
        firstname = str(self.entry1.get())
        lastname = str(self.entry2.get())
        
        # If firstname and lastname only have letter in then continue, otherwise give warning and then exit the program
        if firstname.isalpha() != True or lastname.isalpha() != True:
            nameError = messagebox.showerror(title="Incorrect Name Usage", message="You can only enter alphabetical characters when entering your character's name. \nThe Application will now close.")
            if nameError == "ok":
                root.destroy()
    
        self.nameIntro.destroy()
        self.firstName.destroy()
        self.lastName.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.nameConfirm.destroy()
        
        name = firstname + " " + lastname
        
        self.infoText3 = Label(self.master, text="Your character's name is " + name + "\nDo you want to continue with the character creation?")
        self.infoText3.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.charAge)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charName)
        self.backButton.pack()
        
    def charAge(self):
        self.infoText3.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        
        self.ageIntro = Label(self.master, text="Please enter your character's age")
        self.ageIntro.pack()
        
        self.entry3 = Entry(self.master)
        self.entry3.pack()
        
        self.ageConfirm = Button(self.master, text="Confirm Age", command=self.continueToCharClasses)
        self.ageConfirm.pack()
        
    def continueToCharClasses(self):
        global age
        # See if age is equal to a integer, if not then give error warning and exit.
        try:
            age = int(self.entry3.get())
        except ValueError:
            ageError = messagebox.showerror(title="Incorrect Age Usage", message="You can only enter numerical characters when entering your character's age. \nThe Application will now close.")
            if ageError == "ok":
                root.destroy()
            
        self.ageIntro.destroy()
        self.entry3.destroy()
        self.ageConfirm.destroy()
        
        self.infoText4 = Label(self.master, text="Your character's age is " + str(age) + "\nDo you want to continue with the character creation?")
        self.infoText4.pack()
        
        self.nextButton = Button(self.master, text="Next", command=self.charClasses)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charAge)
        self.backButton.pack()
        
    def charClasses(self):
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        
        self.classIntro = Label(self.master, text="Please select your character's class")
        self.classIntro.pack()
        
        self.classFighterButton = Button(self.master, text="Fighter", command=self.classFighter)
        self.classFighterButton.pack()
        
        fighterInfo = Balloon(self.master)
        fighterInfo.bind_widget(self.classFighterButton, balloonmsg="A master of martial combat, skilled with a variety of weapons and armor")
        
        self.classRogueButton = Button(self.master, text="Rogue", command=self.classRogue)
        self.classRogueButton.pack()
        
        rogueInfo = Balloon(self.master)
        rogueInfo.bind_widget(self.classRogueButton, balloonmsg="A scoundrel who uses stealth and trickery to overcome obstacles and enemies")
        
        self.classWizardButton = Button(self.master, text="Wizard", command=self.classWizard)
        self.classWizardButton.pack()
        
        wizardInfo = Balloon(self.master)
        wizardInfo.bind_widget(self.classWizardButton, balloonmsg="A scholarly magic-user capable of manipulating the structures of reality. \nWizards usually live longer than other people.")
        
        self.classRangerButton = Button(self.master, text="Ranger", command=self.classRanger)
        self.classRangerButton.pack()
        
        rangerInfo = Balloon(self.master)
        rangerInfo.bind_widget(self.classRangerButton, balloonmsg="A warrior who combats threats on the edges of civilization. \nGood with long range weaponry especially bows. \nAlso accompanied by an animal companion.")
        
    def classFighter(self):
        global charClass
        charClass = "Fighter"
        
        self.classFighterButton.destroy()
        self.classRogueButton.destroy()
        self.classWizardButton.destroy()
        self.classRangerButton.destroy()
        
        self.infoText5 = Label(self.master, text="You're character is a " +  charClass + "\nDo you want to finalize character creation?")
        self.infoText5.pack()
        
        self.nextButton = Button(self.master, text="Finish", command=self.charInfo)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charClasses)
        self.backButton.pack()
        
        
    def classRogue(self):
        global charClass
        charClass = "Rogue"
        
        self.classFighterButton.destroy()
        self.classRogueButton.destroy()
        self.classWizardButton.destroy()
        self.classRangerButton.destroy()
        
        self.infoText5 = Label(self.master, text="You're character is a " +  charClass + "\nDo you want to finalize character creation?")
        self.infoText5.pack()
        
        self.nextButton = Button(self.master, text="Finish", command=self.charInfo)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charClasses)
        self.backButton.pack()
        
    def classWizard(self):
        global charClass
        charClass = "Wizard"
        
        self.classFighterButton.destroy()
        self.classRogueButton.destroy()
        self.classWizardButton.destroy()
        self.classRangerButton.destroy()
        
        self.infoText5 = Label(self.master, text="You're character is a " +  charClass + "\nDo you want to finalize character creation?")
        self.infoText5.pack()
        
        self.nextButton = Button(self.master, text="Finish", command=self.charInfo)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charClasses)
        self.backButton.pack()
        
    def classRanger(self):
        global charClass
        charClass = "Ranger"
        
        self.classFighterButton.destroy()
        self.classRogueButton.destroy()
        self.classWizardButton.destroy()
        self.classRangerButton.destroy()
        
        self.infoText5 = Label(self.master, text="You're character is a " +  charClass + "\nDo you want to finalize character creation?")
        self.infoText5.pack()
        
        """self.nextButton = Button(self.master, text="Finish", command=self.charInfo)
        self.nextButton.pack()"""
        
        self.nextButton = Button(self.master, text="Create Animal Companion", command=self.animalCompanion)
        self.nextButton.pack()
        
        self.backButton = Button(self.master, text="Back", command=self.charClasses)
        self.backButton.pack()
        
    def animalCompanion(self):
        self.infoText5.destroy()
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        self.classIntro.destroy()
        
        self.animalInfo = Label(self.master, text="Every ranger needs an animal companion to travel with, please press one of the buttons below to select an animal.")
        self.animalInfo.pack()
        
        self.wolfButton = Button(self.master, text="Wolf", command=self.wolfFriend)
        self.wolfButton.pack()
        
        wolfInfo = Balloon(self.master)
        wolfInfo.bind_widget(self.wolfButton, balloonmsg="Fast, agile and loyal.")
        
        self.bearButton = Button(self.master, text="Bear", command=self.bearFriend)
        self.bearButton.pack()
        
        bearInfo = Balloon(self.master)
        bearInfo.bind_widget(self.bearButton, balloonmsg="Large and tough. Good at climbing trees.")
        
        self.lynxButton = Button(self.master, text="Lynx", command=self.lynxFriend)
        self.lynxButton.pack()
        
        lynxInfo = Balloon(self.master)
        lynxInfo.bind_widget(self.lynxButton, balloonmsg="Vicious and sneaky. You won't see it coming.")
        
        self.hawkButton = Button(self.master, text="Hawk", command=self.hawkFriend)
        self.hawkButton.pack()
        
        hawkInfo = Balloon(self.master)
        hawkInfo.bind_widget(self.hawkButton, balloonmsg="Great for scouting ahead or delivering a message.")
        
        self.backButton2 = Button(self.master, text="Back", command=self.charClasses)
        self.backButton2.pack()
    
    def wolfFriend(self):
        self.animalInfo.destroy()
        self.wolfButton.destroy()
        self.bearButton.destroy()
        self.lynxButton.destroy()
        self.hawkButton.destroy()
        self.infoText5.destroy()
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        self.backButton2.destroy()
        self.classIntro.destroy()
        
        self.animal = "Wolf"
        
        self.entry4 = Entry(self.master)
        self.entry4.pack()
        
        self.nextButton3 = Button(self.master, text="Next", command=self.charInfo3Cont)
        self.nextButton3.pack()
        
        self.backButton3 = Button(self.master, text="Back", command=self.charClasses)
        self.backButton3.pack()
        
    def bearFriend(self):
        self.animalInfo.destroy()
        self.wolfButton.destroy()
        self.bearButton.destroy()
        self.lynxButton.destroy()
        self.hawkButton.destroy()
        self.infoText5.destroy()
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        self.backButton2.destroy()
        self.classIntro.destroy()
        
        self.animal = "Bear"
        
        self.entry4 = Entry(self.master)
        self.entry4.pack()
        
        self.nextButton3 = Button(self.master, text="Next", command=self.charInfo3Cont)
        self.nextButton3.pack()
        
        self.backButton3 = Button(self.master, text="Back", command=self.charClasses)
        self.backButton3.pack()
        
    def lynxFriend(self):
        self.animalInfo.destroy()
        self.wolfButton.destroy()
        self.bearButton.destroy()
        self.lynxButton.destroy()
        self.hawkButton.destroy()
        self.infoText5.destroy()
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        self.backButton2.destroy()
        self.classIntro.destroy()
        
        self.animal = "Lynx"
        
        self.entry4 = Entry(self.master)
        self.entry4.pack()
        
        self.nextButton3 = Button(self.master, text="Next", command=self.charInfo3Cont)
        self.nextButton3.pack()
        
        self.backButton3 = Button(self.master, text="Back", command=self.charClasses)
        self.backButton3.pack()
        
    def hawkFriend(self):
        self.animalInfo.destroy()
        self.wolfButton.destroy()
        self.bearButton.destroy()
        self.lynxButton.destroy()
        self.hawkButton.destroy()
        self.infoText5.destroy()
        self.infoText3.destroy()
        self.infoText4.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        self.backButton2.destroy()
        self.classIntro.destroy()
        
        self.animal = "Hawk"
        
        self.entry4 = Entry(self.master)
        self.entry4.pack()
        
        self.nextButton3 = Button(self.master, text="Next", command=self.charInfo3Cont)
        self.nextButton3.pack()
        
        self.backButton3 = Button(self.master, text="Back", command=self.charClasses)
        self.backButton3.pack()
        
    def charInfo3Cont(self):
        global animalname
        
        animalname = str(self.entry4.get())
    
        self.entry3.destroy()
        self.entry4.destroy()
        self.nextButton3.destroy()
        self.backButton3.destroy()
        
        self.infoText5 = Label(self.master, text="Your pet's name is " + animalname)
        self.infoText5.pack()
        
        """self.nextButton = Button(self.master, text="Finish", command=self.charInfo)
        self.nextButton.pack()"""
        
        self.nextButton4 = Button(self.master, text="Finish Character Creation", command=self.charInfo3)
        self.nextButton4.pack()
        
    def charInfo3(self):
        global race, maleFemale, firstname, lastname, age, charClass, animalname
    
        self.infoText5.destroy()
        self.nextButton4.destroy()
        
        # If firstname and lastname only have letter in then continue, otherwise give warning and then exit the program
        if animalname.isalpha() != True:
            nameError = messagebox.showerror(title="Incorrect Name Usage", message="You can only enter alphabetical characters when entering your animal's name. \nThe Application will now close.")
            if nameError == "ok":
                root.destroy()
        
        self.infoNameFirst = Label(self.master, text="First Name: " + firstname)
        self.infoNameFirst.pack()
        
        self.infoNameLast = Label(self.master, text="Last Name: " + lastname)
        self.infoNameLast.pack()
        
        self.infoGender = Label(self.master, text="Gender: " + maleFemale)
        self.infoGender.pack()
        
        self.infoRace = Label(self.master, text="Race: " + race)
        self.infoRace.pack()
        
        self.infoClass = Label(self.master, text="Class: " + charClass)
        self.infoClass.pack()
        
        self.infoAge = Label(self.master, text="Age: " + str(age))
        self.infoAge.pack()
        
        self.animalFriend = Label(self.master, text="Animal Friend: " + self.animal)
        self.animalFriend.pack()
        
        self.animalFriendName = Label(self.master, text="Animal Name: " + animalname)
        self.animalFriendName.pack()
        
        self.invButton = Button(self.master, text="Generate Items in Inventory", command=self.inventory)
        self.invButton.pack()
        
        self.exportButton = Button(self.master, text="Export Character", command=self.export2)
        self.exportButton.pack()

    def charInfo(self):
        global race, maleFemale, firstname, lastname, age, charClass
    
        self.classIntro.destroy()
        self.entry3.destroy()
        self.ageConfirm.destroy()
        self.infoText5.destroy()
        self.nextButton.destroy()
        self.backButton.destroy()
        
        self.infoNameFirst = Label(self.master, text="First Name: " + firstname)
        self.infoNameFirst.pack()
        
        self.infoNameLast = Label(self.master, text="Last Name: " + lastname)
        self.infoNameLast.pack()
        
        self.infoGender = Label(self.master, text="Gender: " + maleFemale)
        self.infoGender.pack()
        
        self.infoRace = Label(self.master, text="Race: " + race)
        self.infoRace.pack()
        
        self.infoClass = Label(self.master, text="Class: " + charClass)
        self.infoClass.pack()
        
        self.infoAge = Label(self.master, text="Age: " + str(age))
        self.infoAge.pack()
        
        self.invButton = Button(self.master, text="Generate Items in Inventory", command=self.inventory)
        self.invButton.pack()
        
        self.exportButton = Button(self.master, text="Export Character", command=self.export2)
        self.exportButton.pack()
    
    def inventory(self):
        global race, maleFemale, firstname, lastname, age, charClass, invTest
    
        self.invButton.destroy()
        
        invTest = True
        
        fighterInvPrimary = ["Short Sword", "Long Sword", "Spear"]
        fighterInvSecondary = ["Short Sword", "Crossbow", "Shield", "Dirk"]
        fighterInvArmour = ["Leather Armour", "Iron Armour", "Steel Armour"]
        
        rogueInvPrimary = ["Short Sword", "Dagger", "Sai"]
        rogueInvSecondary = ["Short Sword", "Dagger", "Sai", "Small Crossbow"]
        rogueInvArmour = ["Leather Armour", "Plated Leather Armour", "Chainmail Armour"]
        
        wizardInvPrimary = ["Wooden Staff", "Iron Staff", "Wand"]
        wizardInvSecondary = ["Short Sword", "Long Sword"]
        wizardInvArmour = ["Magical Robes", "Leather Armour", "Chainmail Armour"]
        
        rangerInvPrimary = ["Yew Bow", "Oak Bow", "Crossbow"]
        rangerInvSecondary = ["Short Sword", "Dagger", "Small Crossbow"]
        rangerInvArmour = ["Leather Armour", "Plated Leather Armour", "Chainmail Armour"]
        
        gold = random.randint(1, 101)
        potions = random.randint(1, 21)
        ammo = random.randint(1, 101)
        
        misc = ["Gold Pieces", "Healing Potions"]
       
        if charClass == "Fighter":
            self.weapon1 = random.choice(fighterInvPrimary)
            self.weapon2 = random.choice(fighterInvSecondary)
            self.armour = random.choice(fighterInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Crossbow":
                self.miscItems = "Crossbow Bolts"
            
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            else:
                self.misc1 = potions
        elif charClass == "Rogue":
            self.weapon1 = random.choice(rogueInvPrimary)
            self.weapon2 = random.choice(rogueInvSecondary)
            self.armour = random.choice(rogueInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Small Crossbow":
                self.miscItems = "Crossbow Bolts"
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo 
        elif charClass == "Wizard":
            self.weapon1 = random.choice(wizardInvPrimary)
            self.weapon2 = random.choice(wizardInvSecondary)
            self.armour = random.choice(wizardInvArmour)
            self.miscItems = random.choice(misc)
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo
        elif charClass == "Ranger":
            self.weapon1 = random.choice(rangerInvPrimary)
            self.weapon2 = random.choice(rangerInvSecondary)
            self.armour = random.choice(rangerInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Small Crossbow" or self.weapon1 == "Crossbow":
                self.miscItems = "Crossbow Bolts"
            elif self.weapon1 == "Yew Bow" or self.weapon1 == "Oak Bow":
                self.miscItems = "Arrows"
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo 
        
        self.displayInv = Label(self.master, text="Items: " + str(self.weapon1) + ", " + str(self.weapon2) + ", " + str(self.armour) + ", " + str(self.misc1) + " " + str(self.miscItems))
        self.displayInv.pack()
    
    def export2(self):
        global race, maleFemale, firstname, lastname, age, charClass, animalname, invTest
        
        self.exportButton.destroy()
        
        self.exportMessage = Label(self.master, text="Character Exported")
        self.exportMessage.pack()
    
        f = open(firstname + " " + lastname + ".txt", "w")
        f.write("First Name: " + str(firstname))
        f.write("\nLast Name: " + lastname)
        f.write("\nGender: " + maleFemale)
        f.write("\nRace: " + race)
        f.write("\nClass: " + charClass)
        f.write("\nAge: " + str(age))
        
        if charClass == "Ranger":
            f.write("\nAnimal: " + self.animal)
            f.write("\nAnimal Name: " + animalname)
            
        if invTest == True:
            f.write("\nInventory: " + str(self.weapon1) + ", " + str(self.weapon2) + ", " + str(self.armour) + ", " + str(self.misc1) + " " + str(self.miscItems))
        

    def randomGen(self):
        self.introLabel.destroy()
        self.button1.destroy()
        self.button2.destroy()
        
        self.labelTest2 = Label(self.master, text="Click the button below to randomise your character.")
        self.labelTest2.pack()
        
        self.randomiseButton = Button(self.master, text="Randomise", command=self.randomise)
        self.randomiseButton.pack()
       
    
    def randomise(self):
        global race, maleFemale, firstname, lastname, age, charClass, animalClass
        
        self.randomiseButton.destroy()
        self.labelTest2.destroy()
        
        race = ["Human", "Elf", "Dwarf", "Halfling", "Half-Orc"]
        
        maleFemale = ["Male", "Female"]
        
        """firstname = {

        "Harriet" : "Male",
        "Orgric" : "Male",
        "Steffan" : "Male",
        "Leondar" : "Male",
        "Agnes" : "Male",
        
        "Alice" : "Female",
        "Uran" : "Female",
        "Steffanie" : "Female",
        "Leona" : "Female",
        "Agnes" : "Female"
        
        }
        
        lastname = ["Black", "Quickwind", "Urash", "Jinx", "Viper"]"""
        
        class Human:
            M = ["Harriet", "Steffan", "Ardam", "James", "Luke"]
            F = ["Alice", "Staffanie", "Merra", "Mia", "Lucia"]
            L = ["Black", "James", "Carpenter", "Bellows", "Celosi"]
            
        
        class Elf:
            M = ["Jandar", "Folre", "Durlan", "Nuvian", "Corym"]
            F = ["Darshee", "Sionia", "Nuovis", "Shalaevar", "Ialantha"]
            L = ["Valrel", "Carnorin", "Joran", "Olonan", "Greywind"]
            
        class Dwarf:
            M = ["Elgrol", "Bradgrarlig", "Hendreak", "Dwokdrumri", "Tuthem"]
            F = ["Khebrekara", "Sirbouthra", "Grussearen", "Jonwelyn", "Stromdorra"]
            L = ["Smeltstone", "Redfist", "Deathmaul", "Leatherback", "Silverhand"]
            
        class Halfling:
            M = ["Urios", "Jannad", "Herbry", "Zenton", "Quinsy"]
            F = ["Yolienne", "Uvine", "Nebrix", "Roswyn", "Rosella"]
            L = ["Earthpot", "Greenfingers", "Grassfound", "Swifthand", "Yellowapple"]
            
        class Halforc:
            M = ["Kiruk", "Korubash", "Gugak", "Brakudurk", "Nerall"]
            F = ["Nizura", "Nanchu", "Kirawar", "Falaz", "Ungrath"]
            L = ["Bloodfist", "Brokendog", "Chaoswheel", "Brokensword", "Ulga-Smor"]
            
        animalClass = ["Wolf", "Bear", "Lynx", "Hawk"]
            
        class Wolf:
            N = ["Sparky", "Midnight", "Snowball", "Biter", "Fast-Wind"]
        
        class Bear:
            N = ["Fluffy", "Pogo", "Furry", "Honey", "Striker"]
            
        class Lynx:
            N = ["Prowler", "Stalker", "Kitten", "Spot", "Hidden"]
            
        class Hawk:
            N = ["Eyes", "Beaky", "Bubba", "Screech", "Zippy"]
        
        charClass = ["Fighter", "Rogue", "Wizard", "Ranger"]
        
        self.gender = random.choice(maleFemale)
        self.charRace = random.choice(race)
        self.charClass2 = random.choice(charClass)
        self.animalClass2 = random.choice(animalClass)
        
        """if gender == "Male":
            firstname = random.choice(Human.M)
        elif gender == "Female":
            firstname = random.choice(Human.F)"""
            
        if self.charRace == "Human":
            if self.gender == "Male":
                firstname = random.choice(Human.M)
                lastname = random.choice(Human.L)
            elif self.gender == "Female":
                firstname = random.choice(Human.F)
                lastname = random.choice(Human.L)
            
            if self.charClass2 == "Wizard":
                age = random.randint(18, 200)
            else:
                age = random.randint(18, 65)
                
        elif self.charRace == "Elf":
            if self.gender == "Male":
                firstname = random.choice(Elf.M)
                lastname = random.choice(Elf.L)
            elif self.gender == "Female":
                firstname = random.choice(Elf.F)
                lastname = random.choice(Elf.L)
                
            if self.charClass2 == "Wizard":
                age = random.randint(18, 1000)
            else:
                age = random.randint(18, 500)
                
        elif self.charRace == "Dwarf":
            if self.gender == "Male":
                firstname = random.choice(Dwarf.M)
                lastname = random.choice(Dwarf.L)
            elif self.gender == "Female":
                firstname = random.choice(Dwarf.F)
                lastname = random.choice(Dwarf.L)
                
            if self.charClass2 == "Wizard":
                age = random.randint(18, 500)
            else:
                age = random.randint(18, 300)
                
        elif self.charRace == "Halfling":
            if self.gender == "Male":
                firstname = random.choice(Halfling.M)
                lastname = random.choice(Halfling.L)
            elif self.gender == "Female":
                firstname = random.choice(Halfling.F)
                lastname = random.choice(Halfling.L)
                
            if self.charClass2 == "Wizard":
                age = random.randint(18, 200)
            else:
                age = random.randint(18, 65)
                
        elif self.charRace == "Half-Orc":
            if self.gender == "Male":
                firstname = random.choice(Halforc.M)
                lastname = random.choice(Halforc.L)
            elif self.gender == "Female":
                firstname = random.choice(Halforc.F)
                lastname = random.choice(Halforc.L)

            if self.charClass2 == "Wizard":
                age = random.randint(18, 200)
            else:
                age = random.randint(18, 65)
               
        self.n = ""
        
        if self.charClass2 == "Ranger":
            if self.animalClass2 == "Wolf":
                self.n = random.choice(Wolf.N)
            elif self.animalClass2 == "Bear":
                self.n = random.choice(Bear.N)
            if self.animalClass2 == "Lynx":
                self.n = random.choice(Lynx.N)
            if self.animalClass2 == "Hawk":
                self.n = random.choice(Hawk.N)

        
        self.infoText6 = Label(self.master, text="Character has been generated. \nPress the 'Finish' button if you want to see your character.")
        self.infoText6.pack()
        
        self.nextButton = Button(self.master, text="Finish", command=self.charInfo2)
        self.nextButton.pack()
        
    def charInfo2(self):
        global race, maleFemale, firstname, lastname, age, charClass, animalClass
        
        self.infoText6.destroy()
        self.nextButton.destroy()
        
        """self.infoNameFirst = Label(self.master, text="First Name: " + random.choice(firstname))
        self.infoNameFirst.pack()
        
        self.infoNameLast = Label(self.master, text="Last Name: " + random.choice(lastname))
        self.infoNameLast.pack()
        
        self.infoGender = Label(self.master, text="Gender: " + random.choice(maleFemale)) 
        self.infoGender.pack()
        
        self.infoRace = Label(self.master, text="Race: " + random.choice(race))
        self.infoRace.pack()
        
        self.infoClass = Label(self.master, text="Class: " + random.choice(charClass))
        self.infoClass.pack()"""
        
        self.infoNameFirst = Label(self.master, text="First Name: " + str(firstname))
        self.infoNameFirst.pack()
        
        self.infoNameLast = Label(self.master, text="Last Name: " + lastname)
        self.infoNameLast.pack()
        
        self.infoGender = Label(self.master, text="Gender: " + self.gender) 
        self.infoGender.pack()
        
        self.infoRace = Label(self.master, text="Race: " + self.charRace)
        self.infoRace.pack()
        
        self.infoClass = Label(self.master, text="Class: " + self.charClass2)
        self.infoClass.pack()
       
        self.infoAge = Label(self.master, text="Age: " + str(age))
        self.infoAge.pack()
        
        if self.charClass2 == "Ranger":
            self.animalFriend = Label(self.master, text="Animal Friend: " + self.animalClass2)
            self.animalFriend.pack()
        
            self.animalFriendName = Label(self.master, text="Animal Name: " + self.n)
            self.animalFriendName.pack()
            
        self.invButton = Button(self.master, text="Generate Items in Inventory", command=self.inventory2)
        self.invButton.pack()
        
        self.exportButton = Button(self.master, text="Export Character", command=self.export)
        self.exportButton.pack()
        
    def inventory2(self):
        global race, maleFemale, firstname, lastname, age, charClass, invTest
    
        self.invButton.destroy()
        
        invTest = True
        
        fighterInvPrimary = ["Short Sword", "Long Sword", "Spear"]
        fighterInvSecondary = ["Short Sword", "Crossbow", "Shield", "Dirk"]
        fighterInvArmour = ["Leather Armour", "Iron Armour", "Steel Armour"]
        
        rogueInvPrimary = ["Short Sword", "Dagger", "Sai"]
        rogueInvSecondary = ["Short Sword", "Dagger", "Sai", "Small Crossbow"]
        rogueInvArmour = ["Leather Armour", "Plated Leather Armour", "Chainmail Armour"]
        
        wizardInvPrimary = ["Wooden Staff", "Iron Staff", "Wand"]
        wizardInvSecondary = ["Short Sword", "Long Sword"]
        wizardInvArmour = ["Magical Robes", "Leather Armour", "Chainmail Armour"]
        
        rangerInvPrimary = ["Yew Bow", "Oak Bow", "Crossbow"]
        rangerInvSecondary = ["Short Sword", "Dagger", "Small Crossbow"]
        rangerInvArmour = ["Leather Armour", "Plated Leather Armour", "Chainmail Armour"]
        
        gold = random.randint(0, 100)
        potions = random.randint(0, 20)
        ammo = random.randint(0, 100)
        
        misc = ["Gold Pieces", "Healing Potions"]
       
        if self.charClass2 == "Fighter":
            self.weapon1 = random.choice(fighterInvPrimary)
            self.weapon2 = random.choice(fighterInvSecondary)
            self.armour = random.choice(fighterInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Crossbow":
                self.miscItems = "Crossbow Bolts"
            
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            else:
                self.misc1 = potions
        elif self.charClass2 == "Rogue":
            self.weapon1 = random.choice(rogueInvPrimary)
            self.weapon2 = random.choice(rogueInvSecondary)
            self.armour = random.choice(rogueInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Small Crossbow":
                self.miscItems = "Crossbow Bolts"
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo 
        elif self.charClass2 == "Wizard":
            self.weapon1 = random.choice(wizardInvPrimary)
            self.weapon2 = random.choice(wizardInvSecondary)
            self.armour = random.choice(wizardInvArmour)
            self.miscItems = random.choice(misc)
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo
        elif self.charClass2 == "Ranger":
            self.weapon1 = random.choice(rangerInvPrimary)
            self.weapon2 = random.choice(rangerInvSecondary)
            self.armour = random.choice(rangerInvArmour)
            self.miscItems = random.choice(misc)
            
            if self.weapon2 == "Small Crossbow" or self.weapon1 == "Crossbow":
                self.miscItems = "Crossbow Bolts"
            elif self.weapon1 == "Yew Bow" or self.weapon1 == "Oak Bow":
                self.miscItems = "Arrows"
                
            if self.miscItems == "Gold Pieces":
                self.misc1 = gold
            elif self.miscItems == "Healing Potions":
                self.misc1 = potions
            else:
                self.misc1 = ammo 
        
        self.displayInv = Label(self.master, text="Items: " + str(self.weapon1) + ", " + str(self.weapon2) + ", " + str(self.armour) + ", " + str(self.misc1) + " " + str(self.miscItems))
        self.displayInv.pack()
        
    def export(self):
        global race, maleFemale, firstname, lastname, age, charClass, animalClass
        
        self.exportButton.destroy()
        
        self.exportMessage = Label(self.master, text="Character Exported")
        self.exportMessage.pack()
    
        f = open(firstname + " " + lastname + ".txt", "w")
        f.write("First Name: " + str(firstname))
        f.write("\nLast Name: " + lastname)
        f.write("\nGender: " + self.gender)
        f.write("\nRace: " + self.charRace)
        f.write("\nClass: " + self.charClass2)
        f.write("\nAge: " + str(age))
        
        if self.charClass2 == "Ranger":
            f.write("\nAnimal: " + self.animalClass2)
            f.write("\nAnimal Name: " + self.n)
            
        if invTest == True:
            f.write("\nInventory: " + str(self.weapon1) + ", " + str(self.weapon2) + ", " + str(self.armour) + ", " + str(self.misc1) + " " + str(self.miscItems))
        
    
# This helps display the root window and manages all the other components of the tkinter application.
root = Tk()
root.geometry("600x400")
my_gui = theGUI(root)
root.mainloop()
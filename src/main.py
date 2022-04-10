name = input ("Enter your name:- ")
age = int(input("Enter your age:- "))
weight = float(input("Enter your weight in kg:- "))

birth_year = 2022 - age
weightLBS = 2.2046226218 * weight

print ("Hello Mr/Mrs. "+ name+ "! Your birth year is", birth_year, "and your weight in lbs is", weightLBS, "lbs.")
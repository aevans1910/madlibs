#I would like to thank Mike Dane for helping me figure out the basic outline of 
# this project with his youtube tutorial "https://www.youtube.com/watch?v=u7g9mRzQLYE"
#on how to code Madlibs. I would also like to thank Meredith Murphy for helping me
#figure out how to put the basic outline of my code into functions and how to use
#a dictionary.

words = {}

def store_inputs ():
    words ["adjective1"] = input("Enter an adjective: ")
    words ["location1"] = input("Enter a location: ")
    words ["adjective2"] = input("Enter an adjective: ")
    words ["adjective3"] = input("Enter an adjective: ")
    words ["adjective4"] = input("Enter an adjective: ")
    words ["ocupation1"] = input("Enter an ocupation: ")
    words ["noun1"] = input("Enter a noun: ")
    words ["body_part1"] = input("Enter a bodypart: ")
    words ["verb1"] = input("Enter a verb: ")
    words ["adjective5"] = input("Enter an adjective: ")
    words ["beast1"] = input("Enter a creature: ")
    words ["verb2"] = input("Enter an verb: ")
    words ["noun2"] = input("Enter a noun: ")

store_input()

def print_Madlibs():
    print ("Once upon a time, a " + words["adjective1"] + " princess lived") 
    print ("in a " + words["location1"] + ". She was ignored by most " + words["adjective2"] + " knights")
    print ("because the idea of a " + words["location1"] + " princess wasn't")
    print (words["adjective3"] + " enough. But she deserved to be rescued as well!")
    print ("She deserved to be " + words["adjective4"] + ". Everyday she waited")
    print ("for her " + words["ocupation1"] + " charming to come, but he never")
    print ("came. One " + words["noun1"] + ", she decided to take her life into")
    print ("her own " + words["body_part1"] + ", she " + words["verb1"] + " the " + words["location1"] + " walls,")
    print ("defeated the " + words["adjective5"] + " " + words["beast1"] + ", and walked out")
    print ("the opening of the " + words["location1"] + ". Ever since then, she's")
    print ("been " + words["verb2"] + " all of the other princesses of the " + words["noun2"] + ".")

print_Madlib()



# from sys import argv
# from os.path import exists
# script,from_file,to_file = argv

# print "copying from %s to %s" %(from_file, to_file)

# in_file = open(from_file)
# in_data = in_file.read()

# print "The input file is %d bytes long" % len(in_data)

# print "does the output file exist? %r " % exists(to_file)

# print "hit return to continue , CTRL to abort."

# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(in_data)

# print "Alright, all done"
# out_file.close
# in_file.close



#Playing with functions

# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r arg2: %r" %(arg1,arg2)

# print_two("zed","singh")

# def two_names(arg1,arg2):
#     print "arg1: %r arg2: %r" %(arg1, arg2)
# two_names("vikas","singh")


#functions and variables

# def cheese_and_crackers(cheese,crackers):
#     print "Your cheese count is %d and crackers count is %d." % (cheese, crackers)
# cheese_and_crackers(20,30)

# print "OR,we can just use variable from our srript:"
# amount_of_cheese = 10
# amount_of_crackers = 50
# cheese_and_crackers(amount_of_cheese,amount_of_crackers)


# print "we can combine two var with maths"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)


# from sys import argv
# script, input_file = argv

# def print_all(f):
#     print f.read()

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, f):
#     print line_count, f.readline()

# current_file = open(input_file)

# print("lets print the whole file: \n")
# print_all(current_file)

# print("lets rewind the file: \n")
# rewind(current_file)

# print("lets print three lines:")

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)



# def add(a, b):
#     return a+b
# a = add(3,5)
# print(a)

# def breaks(stuff):
#     """this function will break words for us """
#     words = stuff.split(' ')
#     return words

# sentence = "all gud things come to those who wait."
# words = breaks(sentence)
# print(words)

# people = 10
# cats = 5
# dogs = 3

# if people < cats:
#     print("tooo many cats")
# else:
#     print("too many people")


# print("Enter from door 1 or door 2")

# door = raw_input("> ")

# if door == "1":
#     print("there's a bear")
#     print("1. take the cake")
#     print("2. scream at bear")

#     bear = raw_input("> ")
#     if bear == "1":
#         print("the bear eats your face off.")
#     elif bear == "2":
#         print("bear eats your leg off.")
#     else:
#         print("well, doing %s is bttr, bear runs away." %bear)

# elif door == "2":
#     print("acb")
#     print("1. a")
#     print("2. b")
#     print("3. c")

#     insanity = raw_input("> ")

#     if insanity == "1" or insanity == "2":
#         print("abcd")
#     else:
#         print("hey")

# else:
#     print("You Die.")


i = 0
numbers = []

for i in range(0,6) :
    print("at the top i is %d") %i
    numbers.append(i)

    i += 1
    print("numbers now:", numbers)
    # print("at the bottom i is %d") %i

print("The numbers:")

for num in numbers:
    print num















    
#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#open the fragment files
fragDnafile1 = open("fragment1.txt", "r")
fragDnafile2 = open("fragment2.txt", "r")
fragDnafile3 = open("fragment3.txt", "r")
fragDnafile4 = open("fragment4.txt", "r")
fragDnafile5 = open("fragment5.txt", "r")
fragDnafile6 = open("fragment6.txt", "r")

#open the suspect files
susDnafile1 = open("suspect1.txt", "r")
susDnafile2 = open("suspect2.txt", "r")
susDnafile3 = open("suspect3.txt", "r")
susDnafile4 = open("suspect4.txt", "r")
susDnafile5 = open("suspect5.txt", "r")

#read the suspect files to a variable
susDnavar1 = susDnafile1.read()
susDnavar2 = susDnafile2.read()
susDnavar3 = susDnafile3.read()
susDnavar4 = susDnafile4.read()
susDnavar5 = susDnafile5.read()

#read the fragment files to a variable
fragDnavar1 = fragDnafile1.read()
fragDnavar2 = fragDnafile2.read()
fragDnavar3 = fragDnafile3.read()
fragDnavar4 = fragDnafile4.read()
fragDnavar5 = fragDnafile5.read()
fragDnavar6 = fragDnafile6.read()

#closing the files
susDnafile1.close()
susDnafile2.close()
susDnafile3.close()
susDnafile4.close()
susDnafile5.close()
fragDnafile1.close()
fragDnafile2.close()
fragDnafile3.close()
fragDnafile4.close()
fragDnafile5.close()
fragDnafile6.close()

#find the index of the dna fragment sequence
indexPossus1frag1 = int(susDnavar1.find(fragDnavar1))
indexPossus1frag2 = int(susDnavar1.find(fragDnavar2))
indexPossus1frag3 = int(susDnavar1.find(fragDnavar3))
indexPossus1frag4 = int(susDnavar1.find(fragDnavar4))
indexPossus1frag5 = int(susDnavar1.find(fragDnavar5))
indexPossus1frag6 = int(susDnavar1.find(fragDnavar6))
indexPossus2frag1 = int(susDnavar2.find(fragDnavar1))
indexPossus2frag2 = int(susDnavar2.find(fragDnavar2))
indexPossus2frag3 = int(susDnavar2.find(fragDnavar3))
indexPossus2frag4 = int(susDnavar2.find(fragDnavar4))
indexPossus2frag5 = int(susDnavar2.find(fragDnavar5))
indexPossus2frag6 = int(susDnavar2.find(fragDnavar6))
indexPossus3frag1 = int(susDnavar3.find(fragDnavar1))
indexPossus3frag2 = int(susDnavar3.find(fragDnavar2))
indexPossus3frag3 = int(susDnavar3.find(fragDnavar3))
indexPossus3frag4 = int(susDnavar3.find(fragDnavar4))
indexPossus3frag5 = int(susDnavar3.find(fragDnavar5))
indexPossus3frag6 = int(susDnavar3.find(fragDnavar6))
indexPossus4frag1 = int(susDnavar4.find(fragDnavar1))
indexPossus4frag2 = int(susDnavar4.find(fragDnavar2))
indexPossus4frag3 = int(susDnavar4.find(fragDnavar3))
indexPossus4frag4 = int(susDnavar4.find(fragDnavar4))
indexPossus4frag5 = int(susDnavar4.find(fragDnavar5))
indexPossus4frag6 = int(susDnavar4.find(fragDnavar6))
indexPossus5frag1 = int(susDnavar5.find(fragDnavar1))
indexPossus5frag2 = int(susDnavar5.find(fragDnavar2))
indexPossus5frag3 = int(susDnavar5.find(fragDnavar3))
indexPossus5frag4 = int(susDnavar5.find(fragDnavar4))
indexPossus5frag5 = int(susDnavar5.find(fragDnavar5))
indexPossus5frag6 = int(susDnavar5.find(fragDnavar6))

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag1 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag1 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag1 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag1 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag1 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have a and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 1 matches suspect {0}".format(suspects))

#this print just spaces out the printed lines
print()

#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag2 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag2 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag2 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag2 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag2 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have an and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 2 matches suspect {0}".format(suspects))

#this print just spaces out the printed lines
print()

#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag3 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag3 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag3 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag3 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag3 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have a and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 3 matches suspect {0}".format(suspects))

#this print just spaces out the printed lines
print()

#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag4 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag4 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag4 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag4 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag4 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have a and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 4 matches suspect {0}".format(suspects))

#this print just spaces out the printed lines
print()

#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag5 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag5 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag5 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag5 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag5 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have a and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 5 matches suspect {0}".format(suspects))

#this print just spaces out the printed lines
print()

#setting the variables to be empty
suspect_1 = ""
suspect_2 = ""
suspect_3 = ""
suspect_4 = ""
suspect_5 = ""

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus1frag6 != -1:
    suspect_1 = ", 1"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus2frag6 != -1:
    suspect_2 = ", 2"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus3frag6 != -1:
    suspect_3 = ", 3"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus4frag6 != -1:
    suspect_4 = ", 4"

#checking if the fragment is in the suspect and setting the variable to the number of that suspect if the fragment is in the suspect
if indexPossus5frag6 != -1:
    suspect_5 = ", 5"

#putting the suspects that have that fragment into a variable for printing
suspects0 = "{0}{1}{2}{3}{4}".format(suspect_1, suspect_2, suspect_3, suspect_4, suspect_5)

#getting rid of the ", " at the start of the str
suspects1 = suspects0[2:]

#getting the last value of the str
suspects2 = str(suspects0[-1])

#making a variable to use to strip the str
suspects3 = ", " + suspects2

#getting the length of the str
suspectslen0 = len(suspects1)

# + 1 on to the length so i can index the str
suspectslen11 = (suspectslen0 + 1)

# - 3 off of the length so i can index the str
suspectslen12 = (suspectslen0 - 3)

#indexing the str so i can change the str to have a and for the last number
suspects4 = suspects1[suspectslen12:suspectslen11]

#replacing the ", " so it becomes an " and "
suspects5 = suspects4.replace(", ", " and ")

#stripping the ''', "number"'''
suspects6 = suspects1.strip(suspects3)

#putting the two strings that have been trimed and changed back together
suspects = suspects6 + suspects5

#printing the dna fragments and the suspects that matches
print("dna fragment 6 matches suspect {0}".format(suspects))
#open the fragment file
fragDnafile = open("fragment1.txt", "r")

#open the suspect file
susDnafile = open("suspect1.txt", "r")

#read the suspect file to a variable
susDnavar = susDnafile.read()

#read the fragment file to a variable
fragDnavar = fragDnafile.read()

#closing the files
susDnafile.close()
fragDnafile.close()

#find the index of the sequence
indexPos = susDnavar.find(fragDnavar)

#print the index of the fragment in the suspects dna
print("the fragment {0} is at the index of {1} in the suspects DNA".format(fragDnavar, indexPos))
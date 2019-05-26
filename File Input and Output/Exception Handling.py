#Exception Handling is useful in real life

try:
    #opening file, according to user input
    infile = open(str(input("What you want to open?")), "r")
    infile.close()

#in the event that the file is not found
# IOError = not found
except IOError:
    print("Hey dude! File does not exist.")

# open file
# first is the actual file name (remember to follow the exact naming)
# python file and data file must be in same folder else use /
# "r" = read mode (read only)
infile = open("DATA.TXT", "r")

#read one line
line = infile.readline()

#read all lines
#each line is read in as a text string (str)
lines = infile.readlines()

#closing file
infile.close()


# "w" = write mode
#be careful when using write mode, if file exists, it will be overwritten
#meaning all previous content will be gone
outfile = open("DATA.TXT", "w")

outfile.close()


# "a" = append mode
# if file exists, new content will be added to the file, else a new file will be created
outfile = open("DATA.TXT" , "a")

outfile.close()

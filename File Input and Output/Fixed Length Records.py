## Fixed Length Records
##<id><name><dob><email><mobile>
##1Lim Ah Seng  1995-01-01limahseng@hotmail.com   12345678
##2Tan Ah Lian  1995-12-31tanahlian@yahoo.com     87654321

#open file
outfile = open("DATA.TXT", "a")

#read all lines
records = infile.readlines()

# process each line using slicing
for record in records:
    rid = record[0:1]
    name = record[1:21]
    dob = record[21:31]
    email = record[31:61]
    mobile = record[61:69]

#writing to it
#\n is adding a newline to the record = nothing will be appended to the same line
outfile.write("{0}{1:12s}{2}{3:20s}{4}\n".format(1,
"Lim Ah Seng", "1995-01-01",
"limahseng@hotmail.com", "12345678"))

outfile.close()

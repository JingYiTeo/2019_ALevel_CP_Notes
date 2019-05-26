# delimited file (eg. csv [Comma Seperated Variables])
#python's csv module
import csv

# assigned infile as variabe
# opened file
with open("person1.csv", 'r', newline="") as infile:
    #using csv module to read
    #delimiter = the dividing factor/varible (in this case is a comma)
    records = csv.reader(infile, delimiter=",")

    #print all the records
    #else can assign variable to each record
    #treat it as an array if it's hard to visualise
    for record in records:
        print("ID:", record[0])
        print("Name:", record[1])
        print("DOB:", record[2])
        print("Email:", record[3])
        print("Mobile:", record[4])

infile.close()


#writing to file
with open("uperson.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter=",")

    #same as above, the records are seperated by commass
    writer.writerows([
        (1, 'Lim Ah Seng', '1995-01-01',
         'limahseng@hotmail.com', '12345678'),
        (2, 'Tan Ah Lian', '1995-12-31',
         'tanahlian@yahoo.com', '87654321')])

outfile.close()

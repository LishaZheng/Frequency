import matplotlib.pyplot as plt
import csv

csvFile = open("Frequencies - Sheet1.csv", 'r')
csvReader = csv.reader (csvFile, delimiter= ',')

SFrequency = []
EFrequency = [] 

for row in csvReader:
    SFrequency.append(row[0])
    EFrequency.append(row[1])

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
for value in SFrequency:
    if float(value) < 20:
        c1 = c1+1
    elif 20 <= float(value) <= 29:
        c2 = c2+1
    elif 30.0 <= float(value) <= 39.0:
        c3 = c3+1
    elif 40.0 <= float(value) <= 49.0:
        c4 = c4+1
    elif 50.0 <= float(value) <= 59.0:
        c5 = c5+1
    elif 60.0 <= float(value) <= 69.0:
        c6 = c6+1
    elif 70.0 <= float(value) <= 79.0:
        c7 = c7+1
    elif float(value) <= 80.0:
        c8 = c8+1
NoP = [c1,c2,c3,c4,c5,c6,c7,c8]
xlist = [10, 20, 30, 40, 50, 60, 70, 80]
    
plt.bar(xlist, NoP, width = 5)
plt.suptitle("People Begin to Hear")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Number of People")
plt.show()
    


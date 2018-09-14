#Octocats (Maggie Zhao, Shafali Gupta, Adil Gondal)
#SoftDev pd7
#K06: StI/O: Divine your Destiny!
#2018-09-13
#============================================================================
import random

def pickRand():
    file = open("occupations.csv", "r")
    dataocc = file.read().split("\n")
    #print dataocc
    #the range removes the header ['Job Class', 'Percentage'] as well as the footer ['Total', '99.8'] and the extra new line at the end.
    dataocc = dataocc[1:-2]
    #print dataocc

    for i in range(len(dataocc)):
        #if the occupation has commas or double quotes, split between the last double quote of the occupation name and the percentage
        if "\"" in dataocc[i]:
            dataocc[i] = dataocc[i].split("\",")
        #otherwise split normally on the comma
        else:
            dataocc[i] = dataocc[i].split(",")
        #print(dataocc[i])

    #creates an empty dictionary
    d = {}

    for row in dataocc:
        #typecasts the percentage from a string to a float
        row[1] = float(row[1])
        d[row[0]] = row[1]
        #print row
        #print type(row[1])

    #random.choices(population, weights=None, *, cum_weights=None, k=1)
    #Return a k sized list of elements chosen from the population with replacement. If the population is empty, raises IndexError.
    randOcc = random.choices(list(d.keys()), weights = list(d.values()), k = 1)
    return randOcc

#============================================================================

print (pickRand())

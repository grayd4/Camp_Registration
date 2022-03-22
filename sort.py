# A utility function to parse camp registration csv
# & output CSVs divided by camp & with one child per line

import csv
import sys

INDEX_CAMP_ONE = 23
CAMPER_COLUMN_COUNT = 8
MAX_CAMPERS = 5

def printHelp():
    print("Help here!")

def getNumCamps(columnNames):
    count = 0
    for i,j in enumerate(columnNames):
        if "Check All That Apply" == j:
            count += 1
    #print(count)
    if count % MAX_CAMPERS != 0:
        print("Invalid number of camps!")
        exit()
    return int(count / MAX_CAMPERS)

# For a given registration, see how many campers are registered within
def getNumCampers(reg, campCount):
    count = 0
    for i in range(MAX_CAMPERS):
        # If a first or last name is registered
        #print(f"{reg[INDEX_CAMP_ONE + (campCount * (i + 1)) + (i * CAMPER_COLUMN_COUNT)]}, {reg[INDEX_CAMP_ONE + (campCount * (i + 1)) + 1 + (i * CAMPER_COLUMN_COUNT)]}")
        if reg[INDEX_CAMP_ONE + (campCount * (i + 1)) + (i * CAMPER_COLUMN_COUNT)] != "" or reg[INDEX_CAMP_ONE + (campCount * (i + 1)) + 1 + (i * CAMPER_COLUMN_COUNT)] != "":
            count += 1
    return count

def main():
    #print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) != 2:
        printHelp()
        exit()
    fileName = sys.argv[1]
    print(f"Executing script on file \"{fileName}\"")

    columnNames = ""
    listRegs = []

    # open csv
    with open(fileName, mode="r") as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in reader:
            if 0 == lineCount:
                columnNames = row # Save column names
                #print(f"Column names are {', '.join(row)}")
                lineCount += 1
            else:
                listRegs.append(row)
                lineCount += 1
        print(f"Processed {lineCount} lines")
    

    campCount = getNumCamps(columnNames)
    print(campCount)
    listCamps = []
    listCampsWithCampers = []
    #print(listRegs)
    for i in range(campCount):
        listCamps.append("")
        campers = []
        listCampsWithCampers.append(campers)
        # TODO this can have blank values if they're signed up for just one...
        for reg in listRegs:
            if listCamps[i] == "" and reg[INDEX_CAMP_ONE + i] != "":
                listCamps[i] = (reg[INDEX_CAMP_ONE + i])
    
    print(f"Names of camps: {listCamps}")
                
    # Iterate through each rtegistration and extract the campers per camp
    for reg in listRegs:
        camper = [] # Empty list to hold indivdual camper info
        numCampers = getNumCampers(reg, campCount)
        #print(f"numCampers: {numCampers}")

        # List to track which camp the camper is attending
        campsForCamper = []
        
        for i in range(numCampers):
            
    









if __name__=="__main__":
    main()
#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     w0500154
#Student Name:  Joseph Petrash

# INPUT ------------------------------------------------------------------------------
# creates table with guides names and sales
def createTable():
    # init an empty 2 column table
    guide = [[],
             []]
    # ask for the number of guides    
    numOfGuides = int(input("Enter the number of guides selling cookies: "))
    # loop for the amount of guides
    for i in range(numOfGuides):
        # loop twice for the two inputs
        for j in range(2):
            # if its the first iteration ask for the name
            if j == 0:
                guide[j].append(input("Enter the name of guide #{0}: ".format(i + 1)))
            # if its the second iteration ask for boxes sold 
            else:
                guide[j].append(int(input("enter the number of boxes sold by {0}: ".format(guide[0][i]))))
    return guide

# PROCESS ------------------------------------------------------------------------------
# calculate the average of list items
def getAverage(list):
    # init sum
    sum = 0
    # go through every list item
    for i in range(len(list)):
        # add list item to sum
        sum = sum + list[i]
    # divide sum by length of list
    average = sum / len(list)
    return average

# calculate what prizes each guide won and add it to the table
def getPrizes(guide, average):
    # variables for readability
    name = 0
    sales = 1
    prizes = 2
    # init prize variable
    prize = ""
    
    # add another column to the guides table
    guide.append([])
    # go through each guide and calculate their prize
    for i in range(len(guide[name])):
        # if the current guides sales equals the most amount sold
        if guide[sales][i] == max(guide[sales]):
            prize = "Trip to Girl Guide Jamboree in Aruba!"
        # if the sales are above the average
        elif guide[sales][i] > average:
            prize = "Super stellar sellar Badge"
        # if the sales are below the average but above 0
        elif guide[sales][i] > 0:
            prize = "Left over cookies"
        # if the guide didnt sell any boxes
        elif guide[sales][i] == 0:
            prize = "Nothing"
        # if the guide bought boxes
        elif guide[sales][i] < 0:
            prize = "You owe us money"
        # append the current guides prize to the new column in the table
        guide[prizes].append(prize)

# OUTPUT ------------------------------------------------------------------------------
# display results to the user
def outputResults(guide, average):
    # intro
    print("The average number of boxes sold by each guide was {0:.1f}".format(average))
    # variables for readability
    name = 0
    sales = 1
    prizes = 2
    # temp table so that the table is outputted in the proper orientation for readability 
    outputTable = []
    # putting everything from the guide table into the new output table
    # swaps rows and columns so when its printed with .format the 
    # list will contain the 3 different stats rather than a list for each stat
    for i in range(len(guide[name])):
        outputTable.append([])
        outputTable[i].append(guide[name][i])
        outputTable[i].append(guide[sales][i])
        outputTable[i].append(guide[prizes][i])
    # table fields
    print("     Guide       |  Sales  |  Prizes Won:")
    print("-----------------------------------------")
    # cycle through each row in outputtable to be printed
    for row in outputTable:
        # print all the data in the list in a table format
        print("     {:<10}  |  {:<5}  |  {:<20}".format(*row))




def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # Init variables
    name = 0
    sales = 1
    # Create table with guide names and sales
    guide = createTable()
    # find the average sales between all guides
    average = getAverage(guide[sales])
    # add prizes to the guides table
    getPrizes(guide, average)
    # display results to user
    outputResults(guide, average)


    # YOUR CODE ENDS HERE
main()
#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     w0500154
#Student Name:  Joseph Petrash

def createTable():
    guide = [[],
             []]    
    numOfGuides = int(input("Enter the number of guides selling cookies: "))
    for i in range(numOfGuides):
        for j in range(2):
            if j == 0:
                guide[j].append(input("Enter the name of guide #{0}: ".format(i + 1)))
            else:
                guide[j].append(int(input("enter the number of boxes sold by {0}: ".format(guide[0][i]))))
    return guide

def getAverage(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = sum / len(list)
    return average

def getPrizes(guide, average):
    name = 0
    sales = 1
    prize = ""
    guide.append([])
    for i in range(len(guide[0])):
        if guide[sales][i] == max(guide[sales]):
            prize = "Trip to Girl Guide Jamboree in Aruba!"
        elif guide[sales][i] > average:
            prize = "Super stellar sellar Badge"
        elif guide[sales][i] > 0:
            prize = "Left over cookies"
        elif guide[sales][i] == 0:
            prize = "Nothing"
        elif guide[sales][i] < 0:
            prize = "You owe us money"
        guide[2].append(prize)


def outputResults(guide, average):
    print("The average number of boxes sold by each guide was {0:.1f}".format(average))
    name = 0
    sales = 1
    prize = 2
    outputTable = [[],
                   [],
                   []]
    
    for i in range(len(guide[name])):
        outputTable[i].append(guide[name][i])
        outputTable[i].append(guide[sales][i])
        outputTable[i].append(guide[prize][i])
    print("     Guide       |  Sales  |  Prizes Won:")
    print("-----------------------------------------")
    for row in outputTable:
        print("     {:<10}  |  {:<5}  |  {:<20}".format(*row))


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    name = 0
    sales = 1
    guide = createTable()
    average = getAverage(guide[sales])
    getPrizes(guide, average)
    outputResults(guide, average)


    # YOUR CODE ENDS HERE
main()
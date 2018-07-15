from RankedList import RankedList

def main():
    myList = RankedList()
    myList.addItem("France")
    myList.addItem("England")
    myList.addItem("Germany")
    myList.addItem("Australia")
    myList.handleVote("France", "England")
    myList.handleVote("Germany", "England")
    myList.handleVote("France", "Germany")
    myList.handleVote("Australia", "Germany")
    myList.handleVote("Australia", "France")
    myList.handleVote("Australia", "England")
    print("Score list:")
    print(myList.scoreList)
    print("Sorted list:")
    print(myList.sortedList)

if __name__== "__main__":
    main()
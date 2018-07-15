from Model.RankedList import RankedList

def main():
    myList = RankedList("Countries")
    myList.addItem("France")
    myList.addItem("England")
    myList.addItem("Germany")
    myList.addItem("Australia")
    myList.handleVote("France", "England")
    myList.handleVote("Germany", "England")
    myList.handleVote("France", "Germany")
    myList.handleVote("France", "Australia")
    myList.handleVote("Australia", "England")
    print(myList)

if __name__== "__main__":
    main()
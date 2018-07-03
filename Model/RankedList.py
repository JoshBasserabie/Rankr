class RankedList:

    def __init__(self):
        #List of Item IDs in ranked order
        sortedList = []
        #List of scores for each item
        scoreList = []
        #List of voting 'lists' (actually dictionaries)
        votingList = []
        # List of item references
        items = []

    def addItem(self, name):
        if name is None:
            return False
        newItem = Item(len(self.sortedList), name)
        if newItem is None:
            return False
        self.sortedList.append(len(self.sortedList))
        self.votingList.append({})
        self.items.append(newItem)
        self.scoreList.append(0)
        return True

    def handleVote(self, winnerID, loserID):
        voteDictionary = self.votingList[winnerID]
        if voteDictionary[loserID] is None:
            voteDictionary[loserID] = 0
        voteDictionary[loserID] += 1
        updateScore(winnerID)
        updateScore(loserID)
        updateSortedList(winnerID)
        updateSortedList(loserID)

    def updateScore(self, itemID):
        #update the score for itemID

    def updateSortedList(self, itemID):
        #fix the sorted list by moving itemID until it is in a valid position
from __future__ import division

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
        # number of items
        itemNum = 0

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
        self.itemNum += 1
        return True

    def handleVote(self, winnerID, loserID):
        voteDictionary = self.votingList[winnerID]
        if voteDictionary[loserID] is None:
            voteDictionary[loserID] = 0
        voteDictionary[loserID] += 1
        self.updateScore(winnerID)
        self.updateScore(loserID)
        self.updateSortedList(winnerID)
        self.updateSortedList(loserID)

    def updateScore(self, itemID):
        #update the score for itemID
        score = 0.0
        count = 0
        votes = self.votingList[itemID]
        for i in range(len(self.items)):
            currVotes = self.votingList[i]
            if i != itemID:
                if votes[i] != 0 or currVotes[itemID] != 0:
                    count += 1
                score += votes[i] / (votes[i] + currVotes[itemID])
        score /= count
        self.scoreList[itemID] = score

    def updateSortedList(self, itemID):
        #fix the sorted list by moving itemID until it is in a valid position
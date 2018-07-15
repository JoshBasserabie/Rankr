from __future__ import division
from Item import Item

class RankedList:

    def __init__(self):
        #List of Item IDs in ranked order
        self.sortedList = []
        #List of scores for each item
        self.scoreList = []
        #List of voting 'lists' (actually dictionaries)
        self.votingList = []
        #List of voting counts (how many other item each item has been compared to)
        self.votingCounts = []
        # List of item references
        self.items = []
        # number of items
        self.itemNum = 0

    def addItem(self, name):
        if name is None:
            return False
        newItem = Item(self.itemNum, name)
        if newItem is None:
            return False
        self.sortedList.append(self.itemNum)
        self.votingList.append({})
        self.items.append(newItem)
        self.votingCounts.append(0)
        self.scoreList.append(0.0)
        self.updateSortedList(self.itemNum)
        self.itemNum += 1
        return True

    def handleVote(self, winnerName, loserName):
        winnerID = self.findItemIDByName(winnerName)
        loserID = self.findItemIDByName(loserName)
        if winnerID is None or loserID is None:
            return
        voteDictionary = self.votingList[winnerID]
        try:
            voteDictionary[loserID]
        except KeyError:
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
        for i in range(self.itemNum):
            if i != itemID:
                currVotes = self.votingList[i]
                votesFor = votes.get(i, 0)
                votesAgainst = currVotes.get(itemID, 0)
                if votesFor != 0 or votesAgainst != 0:
                    count += 1
                    score += 2 * (votesFor / (votesFor + votesAgainst)) - 1
        score /= count
        self.votingCounts[itemID] = count
        self.scoreList[itemID] = score

    def updateSortedList(self, itemID):
        #fix the sorted list by moving itemID until it is in a valid position
        position = self.sortedList.index(itemID)
        while position < len(self.sortedList) - 1 and self.scoreList[itemID] <= self.scoreList[self.sortedList[position + 1]]:
            if self.scoreList[itemID] == self.scoreList[self.sortedList[position + 1]]:
                if self.votingCounts[itemID] >= self.votingCounts[self.sortedList[position + 1]]:
                    position += 1
                    continue
            self.sortedList[position], self.sortedList[position + 1] = self.sortedList[position + 1], self.sortedList[position]
            position += 1
        while position > 0 and self.scoreList[itemID] >= self.scoreList[self.sortedList[position - 1]]:
            if self.scoreList[itemID] == self.scoreList[self.sortedList[position - 1]]:
                if self.votingCounts[itemID] <= self.votingCounts[self.sortedList[position - 1]]:
                    position -= 1
                    continue
            self.sortedList[position], self.sortedList[position - 1] = self.sortedList[position - 1], self.sortedList[position]
            position -= 1

    def findItemIDByName(self, name):
        ID = None
        for i in range(len(self.items)):
            if self.items[i].name == name:
                ID = i
                break
        return ID

    def __str__(self):
        returnString = ""
        returnString += "Ranked items:"
        for item in self.sortedList:
            returnString += "\n"
            returnString += self.items[item].name
        return returnString
from __future__ import division
from random import sample
from Model.Item import Item

class RankedList:

    def __init__(self, name, itemNames = []):
        self.name = name
        # List of Item IDs in ranked order
        self._sortedList = []
        # List of scores for each item
        self.scoreList = []
        # List of voting 'lists' (actually dictionaries)
        self.votingList = []
        # List of voting counts (how many other item each item has been compared to)
        self.votingCounts = []
        # List of item references
        self._items = []
        # number of items
        self.itemNum = 0
        # items that should be voted on before others
        self.voting_items = []
        for item in itemNames:
            self.addItem(item)

    def addItem(self, name):
        if name is None:
            return False
        newItem = Item(self.itemNum, name)
        if newItem is None:
            return False
        self._sortedList.append(self.itemNum)
        self.votingList.append({})
        self._items.append(newItem)
        self.votingCounts.append(0)
        self.scoreList.append(0.0)
        self.updateSortedList(self.itemNum)
        self.voting_items.append(self.itemNum)
        self.itemNum += 1
        return True

    def handleVote(self, winnerID, loserID):
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
        position = self._sortedList.index(itemID)
        while position < len(self._sortedList) - 1 and self.scoreList[itemID] <= self.scoreList[self._sortedList[position + 1]]:
            if self.scoreList[itemID] == self.scoreList[self._sortedList[position + 1]]:
                if self.votingCounts[itemID] >= self.votingCounts[self._sortedList[position + 1]]:
                    position += 1
                    continue
            self._sortedList[position], self._sortedList[position + 1] = self._sortedList[position + 1], self._sortedList[position]
            position += 1
        while position > 0 and self.scoreList[itemID] >= self.scoreList[self._sortedList[position - 1]]:
            if self.scoreList[itemID] == self.scoreList[self._sortedList[position - 1]]:
                if self.votingCounts[itemID] <= self.votingCounts[self._sortedList[position - 1]]:
                    position -= 1
                    continue
            self._sortedList[position], self._sortedList[position - 1] = self._sortedList[position - 1], self._sortedList[position]
            position -= 1

    def findItemIDByName(self, name):
        ID = None
        for i in range(len(self._items)):
            if self._items[i].name == name:
                ID = i
                break
        return ID

    def get_random_pair(self):
        prioritise = None
        if len(self._items) < 2:
            return None
        if len(self.voting_items) < 2:
            prioritise = self.voting_items[0]
            self.voting_items = self._sortedList.copy()
        first, second = sample(self.voting_items, 2)
        if prioritise is not None and prioritise not in [first, second]:
            first = prioritise
            if sample(range(2), 1) == 1:
                first, second = second, first
        self.voting_items.remove(first)
        self.voting_items.remove(second)
        first = self._items[first]
        second = self._items[second]
        print(first, second)
        return [first, second]


    @property
    def sortedList(self):
        return self._sortedList

    @property
    def items(self):
        return self._items

    def __str__(self):
        returnString = ""
        returnString += self.name
        returnString += "\n"
        returnString += "Ranked items:"
        for item in self._sortedList:
            returnString += "\n"
            returnString += self._items[item].name
        return returnString
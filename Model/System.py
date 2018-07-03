from Model.RankedList import RankedList

class System:
    def __init__(self):
        rankedLists = []

    def createList(self, listName):
        newList = RankedList(len(self.rankedLists), listName)
        self.rankedLists.append(newList)

    def createList(self, listName, listItemNames = None):
        newList = RankedList(len(self.rankedLists), listName, listItemNames)
        if newList is not None:
            self.rankedLists().append(newList)
            return True
        return False

    def deleteList(self, listID):
        if listID > len(self.rankedLists) or listID < 0:
            return False
        self.rankedLists[listID], self.rankedLists[-1] = self.rankedLists[-1], self.rankedLists[listID]
        self.rankedLists.pop()
        return True

    def getList(self, listID):
        if listID > len(self.rankedLists) or listID < 0:
            return None
        return self.rankedList[listID]
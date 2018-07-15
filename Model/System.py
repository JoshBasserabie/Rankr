from Model.RankedList import RankedList

class System:
    def __init__(self):
        self.rankedLists = {}

    def createList(self, listName, listItemNames = []):
        newList = RankedList(listName, listItemNames)
        if newList is not None:
            self.rankedLists[listName] = newList
            return newList
        return None

    def deleteList(self, listID):
        if listID > len(self.rankedLists) or listID < 0:
            return False
        self.rankedLists[listID], self.rankedLists[-1] = self.rankedLists[-1], self.rankedLists[listID]
        self.rankedLists.pop()
        return True

    def contains(self, listName):
        return listName in self.rankedLists
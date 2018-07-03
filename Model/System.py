from Model.RankedList import RankedList

class System:
    def __init__(self):
        rankedLists = []

    def createList(self, listName):
        newList = RankedList(len(self.rankedLists), listName)
        rankedLists.append(newList)

    def createList(self, listName, listItemNames = None):
        newList = RankedList(len(self.rankedLists), listName, listItemNames)
        if newList is not None:
            self.rankedLists().append(newList)
            return True
        return False
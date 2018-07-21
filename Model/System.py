from Model.RankedList import RankedList


class System:
    def __init__(self):
        self.ranked_lists = {}

    def create_list(self, list_name, list_item_names=[]):
        new_list = RankedList(list_name, list_item_names)
        if new_list is not None:
            self.ranked_lists[list_name] = new_list
            return new_list
        return None

    def delete_list(self, list_name):
        return self.ranked_lists.pop(list_name, None)

    def contains(self, list_name):
        return list_name in self.ranked_lists

    def get_list(self, list_name):
        return self.ranked_lists.get(list_name, None)
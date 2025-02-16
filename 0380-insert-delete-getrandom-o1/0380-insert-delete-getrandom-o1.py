from random import randint
class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.my_list = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.my_list)
        self.my_list.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        removed = self.index_map[val]
        self.index_map[self.my_list[-1]] = removed

        self.my_list[removed],self.my_list[-1] = self.my_list[-1],self.my_list[removed]

        self.my_list.pop()
        del self.index_map[val]
        return True
    def getRandom(self) -> int:
        index = randint(0, len(self.my_list) - 1)
        return self.my_list[index]

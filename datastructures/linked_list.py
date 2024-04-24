from collections import deque

class LinkedList:
    
    def __init__(self):
        self.d = deque()

    
    def get(self, index: int) -> int:
        i = 0
        for element in self.d:
            if i == index:
                return element
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        self.d.appendleft(val)


    def insertTail(self, val: int) -> None:
        self.d.append(val)


    def remove(self, index: int) -> bool:
        i = 0
        for element in self.d:
            if i == index:
                del self.d[i]
                return True
            i += 1
        return False

    def getValues(self) -> List[int]:
        l = []
        for element in self.d:
            l.append(element)
        return l

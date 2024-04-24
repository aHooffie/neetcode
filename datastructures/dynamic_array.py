class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.l = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        if self.l[i] == None:
            self.size += 1
        self.l[i] = n

    def pushback(self, n: int) -> None:
        # assignment expects array to resize if full, instead of just adding 1 element
        if self.size == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.l[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.l[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        bigger_list = [None] * self.capacity 
        
        # Copy old elements to new list
        for i in range(self.size):
            bigger_list[i] = self.l[i]
        self.l = bigger_list

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
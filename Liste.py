class Liste:

    def __init__(self, *elements):
        self.list = [None, None]
        for element in elements:
            if self.list[0] == None:
                self.list[0] = element
                next = self.list
            else:
                next[1] = [element, None]
                next = next[1]
    
    def add(self, element):
        next = self.list
        while next[1] != None:
            next = next[1]
        next[1] = [element, None]

    def insert(self, index, element):
        next = self.list
        for _ in range(index-1):
            next = next[1]
        next[1] = [element, next[1]]

    def get(self, index):
        next = self.list
        for _ in range(index):
            next = next[1]
        print(next[0])

    def __len__(self):
        next = self.list
        i = 0
        if self.list[0] == None:
            return i
        while next[1] != None:
            i +=  1
            next = next[1]
        return i+1
    
    def remove(self, index):
        next = self.list
        for _ in range(index-1):
            next = next[1]
        next[1] =  next[1][1]

    def replace(self, index, value):
        next = self.list
        for _ in range(index):
            next = next[1]
        next[0] = value

    def clear(self):
        self.list = [None, None]

    def __repr__(self):
        return f'{self.list}'
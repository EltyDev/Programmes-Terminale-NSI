class linked_list: 



    def __init__(self, *elements):
        self.list = [None, None] 
        for element in elements: 
            if type(element) == list or type(element) == tuple:
                for element1 in element:
                    if self.list[0] == None: 
                        self.list[0] = element1 
                        thenext = self.list 
                    else:
                        thenext[1] = [element1, None]
                        thenext = thenext[1] 
            else:
                if self.list[0] == None: 
                    self.list[0] = element 
                    thenext = self.list 
                else:
                    thenext[1] = [element, None] 
                    thenext = thenext[1] 


    def add(self, element):
        thenext = self.list 
        while thenext[1] != None: 
            thenext = thenext[1] 
        thenext[1] = [element, None] 

    def insert(self, index, element):
        thenext = self.list 
        if index > len(self):
            return
        for _ in range(index-1): 
            thenext = thenext[1] 
        thenext[1] = [element, thenext[1]] 


    def get(self, index):
        thenext = self.list 
        for _ in range(index): 
            thenext = thenext[1]
        return thenext[0]


    def __len__(self):
        thenext = self.list 
        i = 0 
        if self.list[0] == None: 
            return i 
        else:
            while thenext[1] != None: 
                i +=  1 
                thenext = thenext[1] 
        return i+1 


    def del_ind(self, index):
        thenext = self.list 
        if index == 0:
            thenext[0] = thenext[1][0]
            thenext[1] = thenext[1][1]
        else:
            for _ in range(index-1): 
                thenext = thenext[1] 
            thenext[1] =  thenext[1][1] 

    def replace(self, index, valeur):
        thenext = self.list 
        if index > len(self):
            return
        for _ in range(index): 
            thenext = thenext[1] 
        thenext[0] = valeur 

    def del(self, valeur):
        old = None
        thenext = self.list
        while thenext[0] != valeur: 
            old = thenext 
            thenext = thenext[1] 
        if old == None: 
            thenext[0] = thenext[1][0]
            thenext[1] = thenext[1][1]
        else:
            old[1] = thenext[1] 

    #on vide la liste
    def clear(self):
        self.list = [None, None] 

    def copy(self):
        thefirt = Liste()
        thenext = self.list 
        while thenext[1] != None: 
            thefirt.add(thenext[0])
            thenext = thenext[1] 
        thefirt.del_ind(0)
        return thefirt
    
    def to_list(self):
        tab = []
        thenext = self.list 
        while thenext[1] != None: 
            tab.append(thenext[0])
            thenext = thenext[1] 
        tab.append(thenext[0])
        return tab

    def __repr__(self):
        thenext = self.list 
        theobject = "|"
        if self.list == [None, None]:
            return f'{theobject}{self.list[0]}, {self.list[1]}{theobject}'
        while thenext[1] != None: 
            theobject += str(thenext[0]) + ", "
            thenext = thenext[1] 
        theobject += str(thenext[0]) + "|"
        return f'{theobject}'

    def __str__(self):
        thenext = self.list 
        theobject = "|"
        if self.list == [None, None]:
            return f'{theobject}{self.list[0]}, {self.list[1]}{theobject}'
        while thenext[1] != None: 
            theobject += str(thenext[0]) + ", "
            thenext = thenext[1] 
        theobject += str(thenext[0]) + "|"
        return f'{theobject}'
    
    def __setitem__(self, index, valeur):
        return self.replace(index, valeur)

    def __getitem__(self, index):
        if index > len(self):
            return None
        return self.get(index)

    def __add__(self, x):
        tab = self.copy()
        thenext = tab.list 
        while thenext[1] != None: 
            thenext = thenext[1] 
        thenext[1] = x.list  
        return tab 

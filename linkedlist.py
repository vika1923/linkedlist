class linkedlist:
    def __init__(self, data, tail):   # head and tail - linkedlist objects
        self.data = data
        self.tail = tail

    def displaydata(self):
        print("data:",self.data, "   tail:",self.tail)

    def iterate(self, i=0):      # pass the first element (head???)
        self.displaydata()
        print(i)
        i+=1
        if self.tail:
            self.tail.iterate(i=i)
            return self
        # else:
        #     print("list ended")

    def getat(self, neededindex, i=0):      # pass the first element (head???) 
        if self.tail and i < neededindex:
            i+=1
            self.tail.getat(neededindex=neededindex, i=i)
        else:
            return self.displaydata()
        
    def append(self, value, index):
        self.getat(index)
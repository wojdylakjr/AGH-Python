class Stack:

    def __init__(self, currentStack = 0):
        if(isinstance(currentStack, Stack)):
            self.data = currentStack.data
        elif(currentStack == 0):
            self.data = []

    def add(self, n):
        self.data.append(n)
    
    def pop(self, n):
        if len(self.data) > 0:
            del self.data[-1]
        else:
            print("Nie mozna usunac")

    def addStackk(self, stackToAdd):

        if(isinstance(stackToAdd, Stack)):
            self.data += stackToAdd.data
        else:
            print("Nie mozna dodac")

    def print(self):
        print(self.data)

    def size(self):
      return len(self.data)

stos1 = Stack()
stos1.add(2)
stos1.add(8)
stos1.pop(8);
stos1.add(6)
stos1.print()
print(stos1.size())




class SortedStack(Stack):
    def add(self, n):
        if self.size() == 0 :
            self.data.append(n)

        elif(n >= self.data[self.size() -1 ]):
            self.data.append(n)
        
        else:
            print("Nie mozna dodac")
            
print("Posortowany stos: ")
stos2 = SortedStack()
stos2.add(0)
stos2.add(3)
stos2.add(6)
stos2.print()
print("Dodanie jedynki do posortowanego stosu")
stos2.add(1)
stos1.addStackk(stos2)
stos1.print()
stos3 = Stack(stos1)
stos3.print()
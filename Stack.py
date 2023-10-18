####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

class Stack:
    
    def __init__(self):
        self.base = []

    def push(self, item):
        self.base.append(item)

    def pop(self):
        return self.base.pop()

    def peek(self):
        if len(self.base) == 0:
            return None
        return self.base[-1]
    
    def size(self):
        return len(self.base)
    
    def is_empty(self):
        if len(self.base)==0:
            return True
        return False



def reverse_string(str):
    stack = Stack()
    length = len(str)
    
    for i in range(0,length):
        stack.push(str[i])

    string = ''
    while stack.is_empty()==False:
        string+=stack.pop()
    return string

print(reverse_string("buggy"))



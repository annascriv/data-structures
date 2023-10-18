####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:

    def __init__(self):
        self._q = []

    def __str__(self):
        return f"{self._q}"
    
    def enqueue(self,item):
        self._q.insert(0,item)

    def dequeue(self):
        return self._q.pop()
    
    def peek(self):
        return self._q[-1]
    
    def size(self):
        return len(self._q)
    
    def is_empty(self):
        if len(self._q)==0:
            return True
        return False
    
def pizza_line(str):
    queue = Queue() 

    str = str.split("/")

    for i in range(0,len(str)):
        queue.enqueue(str[i])
    print(queue._q)
    while queue.is_empty() == False:
        print(f"{queue._q.pop()}, you are #{len(str)-queue.size()} in line.")
            

pizza_line("Anna/Robert/Emily/Jenna/Amy")
    

    

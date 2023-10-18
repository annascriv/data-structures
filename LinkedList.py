####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"
    
class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    def search(self, search_value):
        current_node = self.head
        #print(current_node.value)
        if current_node.value == search_value:
            return f"{current_node} is at position 0."
        if current_node.next is None:
            return f"{search_value} is not in the linked list."
        else:
            temp = self.head
            v = []
            while temp:
                v.append(temp.value)
                temp = temp.next
            if search_value in v:
                return f"{search_value} is at position {v.index(search_value)+1}"
        return "Couldn't find it!"
    
    def remove(self, remove_value):
        if self.head is None:
            return "List is empty"
        
        if self.head.value == remove_value:
            self.head = self.head.next
            return
        previous_node = self.head

        for node in self:
            if node.value == remove_value:
                previous_node.next = node.next
                return
            previous_node = node

        # if current_node.value == remove_value:
        #     current_node.next == current_node.next.next
        
        # if current_node.next is None:
        #     return f"{remove_value} is not in the linked list."
        # else:
        #     temp = linked_list.head
        #     v = []
        #     while temp:
        #         v.append(temp.value)
        #         temp = temp.next
        #     if remove_value in v:
    def size(self):
        count=0
        current_node = self.head

        if current_node == None:
            return count
        elif current_node.next == None:
            return count+1
        else:
            v = []
            temp = linked_list.head
            while temp:
                v.append(temp.value)
                count = count+1
                temp = temp.next
            return count
    
    def is_empty(self):
        current_node = self.head
        if current_node == None:
            return True
        return False

                
                
        

        
first_node = Node("names")
linked_list = LinkedList()       
linked_list.insert("Anna")
linked_list.insert("Louise")
linked_list.insert("Scriven")
linked_list.insert("Robert")
linked_list.insert("Davidson")
#linked_list.insert("")
# print(linked_list.head.value)
# print(linked_list.head.next.value)
# print(linked_list.head.next.next.value)
print(linked_list.search("Louise"))

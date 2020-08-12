class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def print_linked_list(self, linked_list):
        """ To print linked list """
        itr = linked_list
        while itr:
            print(itr.val)
            itr = itr.next

    """ Functions for all insert types """   

    def insert_at_start(self, val, linked_list=None):
        print('Insert at start')
        newNode = Node(val)
        newNode.next = linked_list
        return newNode

    def insert_at_end(self, val, linked_list=None):
        print('Insert at end')
        newNode = Node(val)
        if linked_list is None:
            self.insert_at_start(val)
        itr = linked_list
        while itr.next is not None:
            itr = itr.next
        itr.next = newNode
        return linkedList

    def insert_at_index(self, val, index, linked_list=None):
        newNode = Node(val)
        # return new node if linked list is empty
        if linkedList is None:
            return newNode
        itr = linked_list
        
        #add at starting if index is 0
        if(index == 0):
            newNode.next = linked_list
            return newNode
        
        # looping till pointer itr gets to index
        while index > 1:
            itr = itr.next
            index-=1
        # adding new node to itr with next value for itr being the rest of the linked list
        itr.next = Node(val, itr.next)

        return linked_list

    """ Function for all delete types """
    
if __name__ == "__main__":
    ll = LinkedList()
    linkedList = ll.insert_at_start(1)
    linkedList = ll.insert_at_start(10, linkedList)
    linkedList = ll.insert_at_start(102, linkedList)
    linkedList = ll.insert_at_start(99, linkedList)
    ll.print_linked_list(linkedList)

    linkedList = ll.insert_at_end(6, linkedList)
    ll.print_linked_list(linkedList)
    linkedList = ll.insert_at_index(999, 5, linkedList)
    ll.print_linked_list(linkedList)





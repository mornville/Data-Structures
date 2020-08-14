class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def print_linked_list(self, linked_list):
        """ To print linked list """
        print("Printing")
        if linked_list is None:
            print('Empty list')
            return
        itr = linked_list
        while itr:
            print(itr.val)
            itr = itr.next

    """ --------- Functions for all insert types --------- """

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

        # add at starting if index is 0
        if(index == 0):
            newNode.next = linked_list
            return newNode

        # looping till pointer itr gets to index
        while index > 1:
            itr = itr.next
            index -= 1
        # adding new node to itr with next value for itr being the rest of the linked list
        itr.next = Node(val, itr.next)

        return linked_list

    """ --------- Function for all delete types --------- """

    def delete_at_start(self, linked_list=None):
        print('Delete at start')
        if linked_list is None:
            return None
        print(f'deleted Value: {linked_list.val}')
        linked_list = linkedList.next

        return linked_list

    def delete_at_end(self, linked_list=None):
        print('delete at end')
        if linked_list is None:
            return None

        itr = linked_list
        while itr:
            itr = itr.next
            if itr.next.next is None:
                print(f'Deleted Value: {itr.next.val}')
                itr.next = None
                return linked_list

    def delete_at_index(self, position, linked_list=None):
        # If linked list is empty 
        if linked_list == None: 
            return  None
  
        # Store head node 
        temp = linked_list 
  
        # If head needs to be removed 
        if position == 0: 
            linked_list = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None or temp.next is None: 
            print('Not found')
            return linked_list 

  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 
  
        return linked_list

    def delete_by_value(self, val, linked_list):
        print('In delete by value')
        if not linked_list:
            return None
        node = linked_list
        prev = node
        while node is not None:
            if prev.val == val:
                prev = node
                node = node.next
                if node.next is not None and node.next.next is not None:
                    node.val = node.next.val
                    node.next = node.next.next
                elif node.next is not None and node.next.next is None:
                    node.val = node.next.val
                    node.next = None
                else:
                    prev.next = None
            else:
                print('In else')
                node = node.next       
        return linked_list

    """ --------- General operations ---------- """

    # 1.1 Length of linked list - iterative
    def length_of_list(self, linked_list):
        print('Comparing length of linked list Iterative')
        if not linked_list:
            return 0
        cur = linked_list
        count = 1
        while cur.next is not None:
            count +=1
            cur = cur.next
        return count
    
    # 1.1 Length of linked list - recursive
    def length_of_list_recursive(self, linked_list):
        if not linked_list:
            return 0
        return 1 + self.length_of_list_recursive(linked_list.next)
            
    ## 2. Reverse list - iterative
    def reverse_list(self, linked_list):
        print('In reverse list')
        if linked_list is None:
            return None
        temp = None
        current = linked_list 
        while(current is not None): 
            next = current.next
            current.next = temp 
            temp = current 
            current = next
        linked_list = temp 
        return linked_list
        
    ## 3. Get node by index
    def get_node_by_index(self, linked_list, index):
        print('Getting node by index')
    
        temp = linked_list
        if index<0:
            return 'Invalid index'
        while index>1 and temp is not None:
            temp = temp.next
            index-=1
        if(temp is None):
            return 'No value at given index'
        return temp.val

    ## 4.1 Search - iterative 
    def search_iterative(self, linked_list, val):
        if linked_list is None:
            return False
        temp = linked_list
        index = 0
        while temp:
            index +=1
            if temp.val == val:
                return f'Found at index {index} by iteration'
            temp = temp.next
        return 'Not found'

    ## 4.2 Search - recursive
    def search_recursive(self, linked_list, val, index=0):
        temp = linked_list
        index+=1
        if temp is None:
            return 'Not found'
        if temp.val == val:
            return f'Found at index {index} by recursion'
        
        return self.search_recursive(temp.next, val, index)
            
if __name__ == "__main__":
    ll = LinkedList()
    linkedList = ll.insert_at_start(1)
    linkedList = ll.insert_at_start(10, linkedList)
    linkedList = ll.insert_at_start(102, linkedList)
    linkedList = ll.insert_at_start(102, linkedList)

    linkedList = ll.insert_at_start(99, linkedList)
    ll.print_linked_list(linkedList)

    linkedList = ll.insert_at_end(6, linkedList)
    ll.print_linked_list(linkedList)
    linkedList = ll.insert_at_index(999, 5, linkedList)
    ll.print_linked_list(linkedList)
    # linkedList = ll.delete_at_start(linkedList)
    # linkedList = ll.delete_at_start(linkedList)

    # ll.print_linked_list(linkedList)

    linkedList = ll.delete_at_end(linkedList)
    ll.print_linked_list(linkedList)
    # linkedList = ll.reverse_list(linkedList)
    # linkedList = ll.delete_by_value(99 , linkedList)
    ll.print_linked_list(linkedList)
    print(ll.length_of_list_recursive (linkedList))

    # Getting value of list by index
    print(ll.get_node_by_index(linkedList, 6))
    
    # Search iterative
    print(ll.search_iterative(linkedList, 102))    
    # Search recursive
    print(ll.search_recursive(linkedList, 999))
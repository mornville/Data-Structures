class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def star():
    # 0 for starting and 1 for star line at end
    print('\n***************************\n')

    return


def menu(choice):
    star()
    print('0. Print Linked List')
    star()

    star()
    print('Insert Operations: ')
    print('\n1. Insert at start')
    print('\n2. Insert at end')
    print('\n3. Insert at an Index')
    star()

    star()
    print('Delete Operations: ')
    print('\n4. Delete from start')
    print('\n5. Delete from end')
    print('\n6. Delete by index')
    star()

    input = print("Enter value: ")
    linkedList = LinkedList()


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        """ To print linked list """
        print("Printing")
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next

    """ Functions for all insert types """

    def insert_at_start(self, val):
        print('Insert at start')
        newNode = Node(val, self.head)
        self.head = newNode
        return

    def insert_at_end(self, val):
        print('Insert at end')
        newNode = Node(val)
        if self.head is None:
            self.insert_at_start(val)
            return
        
        itr = self.head
        
        while itr.next is not None:
            itr = itr.next
        itr.next = newNode
        return self.head

    def insert_at_index(self, val, index):
        newNode = Node(val)
        # return new node if linked list is empty
        if self.head is None:
            return newNode
        itr = self.head

        # add at starting if index is 0
        if(index == 0):
            newNode.next = self.head
            return newNode

        # looping till pointer itr gets to index
        while index > 1:
            itr = itr.next
            index -= 1
        # adding new node to itr with next value for itr being the rest of the linked list
        itr.next = Node(val, itr.next)

        return self.head

    """ Function for all delete types """

    def delete_at_start(self):
        print('Delete at start')
        if self.head is None:
            return None
        print(f'deleted Value: {self.head.val}')
        self.head = self.head.next

        return self.head

    def delete_at_end(self):
        print('delete at end')
        if self.head is None:
            return None

        itr = self.head
        while itr:
            itr = itr.next
            if itr.next.next is None:
                print(f'Deleted Value: {itr.next.val}')
                itr.next = None
                return self.head

    def delete_at_index(self, position):
        # If linked list is empty
        if self.head == None:
            return None

        # Store head node
        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None or temp.next is None:
            print('Not found')
            return self.head

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next

        return self.head


if __name__ == "__main__":
    menu(1)
    ll = LinkedList()
    # ll.insert_at_start(1)
    # ll.insert_at_start(10)
    # ll.insert_at_start(102)
    # ll.insert_at_start(99)
    ll.insert_at_end(100)
    ll.print_linked_list()

# linkedList = ll.insert_at_end(6, linkedList)
# ll.print_linked_list(linkedList)
# linkedList = ll.insert_at_index(999, 5, linkedList)
# ll.print_linked_list(linkedList)
# # linkedList = ll.delete_at_start(linkedList)
# # linkedList = ll.delete_at_start(linkedList)

# # ll.print_linked_list(linkedList)

# linkedList = ll.delete_at_end(linkedList)
# ll.print_linked_list(linkedList)
# linkedList = ll.delete_at_index(4, linkedList)
# ll.print_linked_list(linkedList)

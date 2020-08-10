class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def get_middle(self):
        fast = self.head
        slow = self.head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(20)
    ll.insert_at_end(10)
    ll.insert_at_begining(102)
    ll.print()
    ll.get_middle()
    pass
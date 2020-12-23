from Link import Link
class CircularLinkedList:
    def __init__(self):
        self.head = Link(None, None) # this is the sentinel node!
        self.head.next = self.head   # link it to itself

    def add(self, data):             # no special case code needed for an empty list
        self.head.next = Link(data, self.head.next)

    def __contains__(self, data):    # example algorithm, implements the "in" operator
        current = self.head.next
        while current != self.head:
            if current.data == data: # element found
                return True
            current = current.next
        return False
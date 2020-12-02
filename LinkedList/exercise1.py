class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = value

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def append(self,new_element):
        current = self.head

        if self.head:    #checks if head is not null 
            while current.next:   # checks if current pointer has next elem or not.
                current = current.next     # assigns next element to current pointer
            current.next = new_element     # pointing the cuurent.next  to new element 
        else:
            self.head = new_element        

    def get_position(self,position):
        counter= 1
        current= self.head

        if position<1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter +=1
        return None

    def insert(self,new_element,position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position -1:
                    new_element.next = current.next
                    current.next =new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element        

    def delete(self,value):
        current= self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value==value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.head

e1 = Element(5)
e2 = Element(21)
e3 = Element(4)
e4 = Element(8)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
class Song:
    def __init__(self, title,artist):
        self.title = title
        self.artist = artist
        self.next = None


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, title,artist):
        new_node = Song(title,artist)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


    # Method to add a node at any index
    def insertAtIndex(self, title,artist, index):
        new_node = Song(title,artist)
        current_node = self.head
        position = 0

        if position == index:
            self.insertAtBegin(title,artist)
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL
    def add_song(self, title,artist):
        new_node = Song(title,artist)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # Update node of a linked list
    # at given position
    def updateSongTitle(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.title = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.title = val
            else:
                print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if(self.head == None):
            return
        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_song(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, title):
        current_node = self.head
        while(current_node != None and current_node.next.title != title):
            current_node = current_node.next
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def get_next_song(self, title):
            current_node = self.head
            if(current_node.title == title):
                return current_node.next.title
            while(current_node != None and current_node.next.title != title):
                current_node = current_node.next
            if current_node == None:
                return
            else:
                if(current_node.next.next == None):
                    return None
                else:
                    return current_node.next.next.title

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.title)
            current_node = current_node.next
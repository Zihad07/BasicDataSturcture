
# Create Node

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    
    def __repr__(self):
        return repr(self.data)

# Linklist

class Linklist:
    def __init__(self):

        # empty head node
        self.head = Node()
    
    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        # for represent all node as string

        return ",".join(nodes)
    
    def append(self, data):
        # Add item in the link list - last

        node = Node(data)

        if self.head.next is None:
            # link list empty
            self.head.next = node
            return
            
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
            
        current_node.next = node
        # pass

    def prepend(self, data):
        # add data in the link list- 1st
        node = Node(data,self.head.next)
        self.head.next = node
        # pass
    
    def insert(self,data,new_data):
        cureent_data = self.head.next

        while cureent_data:
            if cureent_data.data == data:
                # create a new node
                new_node = Node(new_data, cureent_data.next)

                cureent_data.next = new_node
                break

            cureent_data = cureent_data.next

        # pass

    def search(self,item):
        currnet_node = self.head.next

        while currnet_node:
            if currnet_node.data == item:
                return currnet_node
            
            currnet_node = currnet_node.next
        
        return None
        # pass

    def remove(self,item):
        
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next
        

        if current_node is None:
            # if not remove value exit
            return None
        
        if self.head == previous_node:
            # if it is head for 1st item remove
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next
        
        

"""
Time Compexity 
Enqueue - O(1)
Dequeue - O(1)

"""

class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size

        self.head, self.tail, self.size = 0, 0, 0
    # -------------------------------------------------

    def enqueue(self, item):
    
        if self.is_full():
            print('Queue is full')
            return

        print('Inserting ->', item)
        self.items[self.tail] = item
        self.tail = (self.tail+1) % self.max_size

        self.size += 1

        

    # -----------------------------------------------------

    def dequeue(self):
        item = self.items[self.head]
        # for set 0 thats means no data
        self.items[self.head] = 0
        self.head = (self.head + 1) % self.max_size

        self.size -= 1

        return item

    # ------------------------------------------------------
    def is_empty(self):
        if self.size == 0:
            return True
        
        return False
    # --------------------------------------------------------

    def is_full(self):
        if self.size == self.max_size:
            return True
        
        return False

#*****************************************************************

if __name__ == "__main__":

    # Queue  object declare
    q = Queue(3)

    q.enqueue('Hasan')
    q.enqueue('zihad')
    q.enqueue('Nayem')

    print(q.items)

    while not q.is_empty():
        person = q.dequeue()
        print(person)

# ----------------------------------\
    
    q.enqueue('Nahid')
    print(q.items)
    print('Head: ->',q.head)
    print('tail: ->', q.tail)
    q.enqueue('Akash')
    print(q.items)
    print('Head: ->',q.head)
    print('tail: ->', q.tail)
    q.enqueue('Hello')
    print(q.items)
    print('Head: ->',q.head)
    print('tail: ->', q.tail)

    # full queue
    q.enqueue('Full')
    print(q.items)
    print('Head: ->',q.head)
    print('tail: ->', q.tail)


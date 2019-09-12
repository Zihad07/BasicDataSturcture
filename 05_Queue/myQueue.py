
# Define Queue Class

class Queue:

    def __init__(self):
        self.items = []
    
    # add item at last
    def enqueue(self, item):
        self.items.append(item)
    
    # dequeue item from first

    def dequeue(self):
        return self.items.pop(0)
    

    def is_empty(self):
        if self.items == []:
            return True
        
        # or

        return False

# -----------------------------------------------------

if __name__ == "__main__":

    # create Queue obeject
    q = Queue()

    q.enqueue("Nahid")
    q.enqueue('Rana')
    q.enqueue('Shuvo')

    # print the Queue item

    while not q.is_empty():
        print(q.dequeue())

    










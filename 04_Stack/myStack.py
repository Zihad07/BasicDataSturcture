
# Definde Stack Class

class Stack:

    def __init__(self):
        self.items = []
    
    # push method
    def push(self, item):
        self.items.append(item)
    
    # pop method
    def pop(self):
        return self.items.pop()
    
    # Stack empty check

    def is_empty(self):
        if self.items == []:
            return True
        
        # or 
        return False

    

# ---------------------------------------------------------------



if __name__ == '__main__':

    # Create Stack objec
     s = Stack()

     s.push(1)
     s.push(2)
     s.push(3)
     s.push(4)

     while not s.is_empty():
         item = s.pop()
         print(item)
    

    


from myLink_list import *

ll = Linklist()
print(ll)

ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
ll.prepend(5)
print(ll)

ll.prepend(6)
print(ll)

print(ll.search(88))
print(ll.search(5))

# remove operation
ll.remove(5);
print(ll)

# insert a data
ll.insert(1,'new-data')
print(ll)

ll.insert(6,'Another-newData')
print(ll)

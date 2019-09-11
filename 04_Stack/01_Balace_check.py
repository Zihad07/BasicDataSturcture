
def is_balanced(input_str):

    # declare empty stack
    s = [] 

    for ch in input_str:
        if ch == '(':
            s.append(ch)
        
        if ch == ')':
            if not s:
                # stack is empty
                return False
            # or
            s.pop()
    
    # stack is full empty if return False
    # or not empety if return true
    return not s

    # -----------------------------

if __name__ == '__main__':
    input_str = input('Enter your expression like (, ) : ')

    if is_balanced(input_str):
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced")
            
        









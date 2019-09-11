
def is_balanced(input_str):

    # declare empty stack
    s = [] 

    for ch in input_str:

        if ch in '{([':
            s.append(ch)
        
        if ch in ')}]':
            if not s:
                # stack is empty
                return False
            # or
            item = s.pop()

            if ch == ']' and '[' != item:
                return False
            elif ch == '}' and  '{' != item:
                return False
            elif ch == ')' and '(' != item :
                return False
                
    
    # stack is full empty if return False
    # or not empety if return true
    return not s

    # -----------------------------


"""
input:{{([])}}
Balanced

input:[{{{[)}}
Not Balanced



"""
if __name__ == '__main__':
    input_str = input('Enter your expression like (, ) : ')

    if is_balanced(input_str):
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced")
            
        









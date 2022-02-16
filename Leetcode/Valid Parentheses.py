class Solution:
    def isValid(self, s: str) -> bool:
        open_element = ['(','[','{']
        pair_element = ['()','[]','{}']
        stack = []
        # TRAVERSE THROUGH THE STRING
        for i in s:
            # ADD OPEN ELEMENTS IN STACK
            if i in open_element:
                stack.append(i)
            else:
                # CHECK IF STACK IS EMPTY
                if stack == []:
                    return False
                ''''
                CHECK IF LAST STACK ELEMENT + TRAVERSED ELEMENT IS A PAIR
                IF ITS NOT, THEN return False
                "([])" --> True
                "[(])" --> False
                ''''
                if stack[-1]+i in pair_element:
                    stack.pop()
                else:
                    return False
        # IF ALL ELEMENTS ARE WITH PAIRS
        return len(stack) == 0

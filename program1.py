class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Check the top of the stack, or set it to a dummy value if stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the top of the stack does not match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been closed properly
        return not stack

def isValidParentheses(s):
    stack = []
    left = ["(", "[", "{"]
    right = [")", "]", "}"]
    for char in s:
        if char in left:
            stack.append(char)
        elif char in right:
            if not stack or left.index(stack.pop()) != right.index(char):
                return False
    return len(stack) == 0


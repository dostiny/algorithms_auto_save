while True:
    arr = input()
    if arr == '.':
        break
    stack = []
    point = True
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                point = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                point = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if point == True and not stack:
        print('yes')
    else:
        print('no')
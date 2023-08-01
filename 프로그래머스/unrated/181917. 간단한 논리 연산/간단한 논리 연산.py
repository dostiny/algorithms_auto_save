def solution(x1, x2, x3, x4):
    answer = True
    a = b = c = d = False
    if x1:
        a = True
    if x2:
        b = True
    if x3:
        c = True
    if x4:
        d = True
    answer = (a or b) and (c or d)
    return answer
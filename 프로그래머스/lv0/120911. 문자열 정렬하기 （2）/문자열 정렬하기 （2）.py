def solution(my_string):
    answer = ''
    st_li = []
    for i in list(my_string):
        if i.isupper():
            st_li.append(i.lower())
        else:
            st_li.append(i)
        st_li.sort()
        print(st_li)
    answer = ''.join(st_li)
    return answer
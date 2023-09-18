def solution(numbers):
    num_dic = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    answer = ''
    st = ''
    for i in numbers:
        st += i
        if st in num_dic:
            answer += num_dic[st]
            st = ''
    return int(answer)
def solution(s, n):
    s = s.replace('[', ' ')
    s = s.replace(']', ' ')
    s = s.replace(' ', '')
    s = s.replace('’', '')
    s = s.replace('‘', '')

    li = list(s.split(','))

    li.sort()
    li.sort(key=lambda x: x[n])
    print(li)

solution(input(), int(input()))
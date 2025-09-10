def solution(s, n):
    s = s[1:-1]
    li = list(s.split(','))

    li.sort(key=lambda x: x[n])
    print(li)

solution(input(), int(input()))
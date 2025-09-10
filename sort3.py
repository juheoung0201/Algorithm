def solution(s):
    answer = []

    s = s.replace('"', '')
    s = s.replace(' ', '')
    s = s[1:-2]

    li = s.split('}')
    li.sort(key=len)

    for i in li:
        xl = []
        i = i.replace('{', '')
        xl = i.split(',')

        for j in xl:
            if answer.count(j) == 0 and j != '':
                answer.append(j)



    print(answer)

solution(input())
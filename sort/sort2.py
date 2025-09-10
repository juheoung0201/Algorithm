def solution(n):
    answer = sorted(n, reverse=True)
    answer = int("".join(answer))
    print(answer)

solution(input())
def solution(n):
    return sum(i for i in range(n+1) if i&1==0)
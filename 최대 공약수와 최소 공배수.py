def solution(n, m):
    answer = []

    a = 0    

    # 최대 공약수
    for i in range(1,n+1):
        if n%i == 0 and m%i == 0:
            a = i

    answer.append(a)

    # 최소 공배수
    if answer[0] == 0:
        answer.append(n*m)
    else:
        answer.append(answer[0]*(n//answer[0])*(m//answer[0]))           

    # 최소 공배수 다른 풀이
    i = max(m,n)
    while True:
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
        i += 1

    return answer

# --------------------------------- 다른 풀이

def gcd(a,b):
    
    if (a<b):
        a, b = b, a
    while (b != 0 ):
        a, b = b, a%b
    return a

def solution2(n,m):
    return [gcd(n,m), n*m/gcd(n,m)]


print(solution2(3, 12))
print(solution2(2, 5))
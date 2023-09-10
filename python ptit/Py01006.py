t = int(input())

def check(n):
    for i in n:
        if i !='4' and i !='7':
            return "NO"
    return "YES"
             
while t>0:
    n = input()
    print(check(n))
    t-=1
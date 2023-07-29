def walk(s1, v, s2, x):

    a = x // (s1+s2)
    b = x % (s1+s2)
    if b <= s1:
        return v*(b+a*s1)
    elif s1<b:
        return v*(a+1)*s1

def main():
    a,b,c,d,e,f,x = [int(i) for i in input().split()]
    if walk(a, b, c, x) > walk(d,e,f,x):
        print("Takahashi")
    elif  walk(a, b, c, x) < walk(d,e,f,x):
        print("Aoki")
    else:
        print("Draw")

main()


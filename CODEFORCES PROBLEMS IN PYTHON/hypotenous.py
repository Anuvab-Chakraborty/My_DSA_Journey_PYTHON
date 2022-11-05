def right_angle(m):
    hypo=(m[0]**2) + (m[1]**2)
    hypo=(hypo**0.5)
    hypo=round(hypo)
    return hypo


if __name__=='__main__':
    n=int(input())
    for i in range(n):
        m=list(map(int,input().split()))
        z=right_angle(m)
        print(z)

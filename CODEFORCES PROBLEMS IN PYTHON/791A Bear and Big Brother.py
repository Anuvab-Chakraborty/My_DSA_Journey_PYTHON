def inc_year(m,n,year):
    if m<=n:
        year+=1
        m=m*3
        n=n*2
        return inc_year(m,n,year)
    return year


m,n=list(map(int,input().split()))
year=0
print(inc_year(m,n,year))
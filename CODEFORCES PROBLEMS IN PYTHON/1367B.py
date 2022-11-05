#1367B
# what is e_index_count?
# agar koi even index m even na mile uska e_index_count...
# formally move done on even index


for l in range(int(input())):
    e_index_count = 0
    o_index_count = 0
    n = int(input())
    lst = list(map(int,input().split()))
    for i in range(n):
        if lst[i]%2 == i%2:
            pass #good array (even is at even index) (odd is at odd index)
        else:
            #even-odd swap needed
            if i%2 == 0:
                e_index_count+=1
            else:
                o_index_count+=1 
        # note swap is  impossible if e_index__count != o_index_count
    if e_index_count != o_index_count:
        print(-1)
    else:
        print(e_index_count)
            # example 3 4 , 3 4 , 3
            # (e_index_count = 3) != (o_index_count = 2) impossible
            
            # example 4 3 , 4 3 , 4
            # (e_index_count = 0) == (o_index_count = 0) ans = e_index_count
            
            # example 3 4 , 4 3 , 4 3 , 4 4 , 3 3
            # (e_index_count = 2) == (o_index_count = 2) ans = e_index_count

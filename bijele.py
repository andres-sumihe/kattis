a,b,c,d,e,f = [int(i) for i in input().split(" ")]
q=1
k=1
bs=2
r=2
kg=2
p=8
for i in range(len(a)):
    if a > q:
        a-=q
    else a < q: 
        q-=a

    if b > k:
        b-=k
    else b < q: 
        q-=b
        
    if c > bs:
        c-=bs
    else c < bs: 
        bs-=c
    
    
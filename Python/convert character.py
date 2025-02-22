s = input()
d = {p: s.count(p) for p in s}
r = []
m = max(d.values())
x=input()
for p,q in d.items():
    if(q==m):
        r.append(p)
print(r)
r.sort()
res=''
for p in s:
    if p==r[0]:
        res+=x
    else:
        res+=p
print(res)

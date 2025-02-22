"""
Rajini Kanth Kakarla
R. K. Kakarla
store in list
[Rajini, Kanth, Kakarla]

"""
s = input()                        # Rajini Kanth Kakarla
l = s.split()                      # [Rajini, Kanth, Kakarla]
l2 = []
a = l[-1]                          # a = Kakarla 
l2.append(a)                       # [Kakarla]
l.remove(a)                        # [Rajini, Kanth]
z = ''
for e in range(len(l)):            # 0               ,1
    d = l[e]                       # d = Rajini      ,d = Kanth
    f = d[0]                       # f = R           ,f = K 
    x = f+'.'                      # x = R.          ,x = K. 
    y = ''.join(x)                 # y = R.          ,y = K.
    z += y                         # z = R.          ,z = R. K.
    if e<len(l)-1:                 # 1
        for sp in range(len(l)-1): # sp = 0
            sp = ' '               # sp = " "
            z+=sp                  # Z = "R. "
print(z,l2[0])                     # R. K. Kakarla

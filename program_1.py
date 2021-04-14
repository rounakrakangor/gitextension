# split without using split function.
s = 'rounak rakangor'
l = []
nl = []
ns = ''
for i in s:
    if i != ' ':
        ns = ns+i
    else:
        l.append(ns)
        ns = ''
l.append(ns)
print(l)
nl = l 
print(nl)

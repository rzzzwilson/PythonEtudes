#llist = []
#for x in range(3):
#    l = lambda y=x: print(y)
#    llist.append(l)
llist = [lambda y=x: print(y) for x in range(3)]
    
for l in llist:
    l()
    
print()

(l1, l2, l3) = llist
x = 'abc'
l1()
x = 'def'
l2(42)
x = 1.2
l3()


llist = []
for x in range(3):
    llist.append(lambda : print(f'lambda: x={x}'))
    
print(f"variable 'x' is {x}")
for l in llist:
    l()
    
(l1, l2, l3) = llist

x = 'abc'
print(f"set 'x' to {x}")
l1()

x = 1.0
print(f"set 'x' to {x}")
l2()

x = [1, 2]
print(f"set 'x' to {x}")
l3()

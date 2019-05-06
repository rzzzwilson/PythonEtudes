llist = []
for x in range(3):
    llist.append(lambda y=x: print(f'lambda: y={y}'))
    
print(f"variable 'x' is {x}")
for l in llist:
    l()
    
x = 'abc'
print(f"set 'x' to {x}")

for l in llist:
    l()

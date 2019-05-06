llist = []
for x in range(3):
    llist.append(lambda : print(f'lambda: x={x}'))
    
print(f"variable 'x' is {x}")
for l in llist:
    l()
    
x = 'abc'
print(f"set 'x' to {x}")

for l in llist:
    l()

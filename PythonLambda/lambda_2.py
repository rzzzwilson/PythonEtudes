def func():
    print(f'func: x={x}')

llist = []
for x in range(3):
    llist.append(func)
    
print(f"variable 'x' is {x}")
for l in llist:
    l()
    
x = 'abc'
print(f"set 'x' to {x}")

for l in llist:
    l()

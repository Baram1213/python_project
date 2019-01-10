x, y = map(int, input().split())

my_list =[]
for i in range(x,y+1):
    my_list.append(2**i)

del my_list[1]
del my_list[-2]
print(my_list)

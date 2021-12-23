mylist = [i * 2 for i in range(150)]
print(f"length = {len(mylist)}")
print(*[i ** 2 for i in mylist])
print(57 in mylist)
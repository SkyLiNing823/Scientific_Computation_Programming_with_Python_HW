L = [1, 10, 12, 2, 3, 320, 506]
L = list(map(lambda x: 'Y'+'0'*(len(str(max(L))) - len(str(x)))+str(x), L))
print(L)

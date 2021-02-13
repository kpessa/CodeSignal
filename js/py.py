# %%
m = 4
n = 4
k = 3
g = [[0, 1, 1, 1],
     [0, 2, 2, 1],
     [2, 3, 4, 5],
     [2, 3, 4, 5]]

h = 0
for a in range(m//k):
    for b in range(n//k):
        s = 0
        for i in range(k):
            for j in range(k):
                s += g[a*k+i][b*k+j]
                print(s)
        h = max(h, s)
        print(h)
print(h)

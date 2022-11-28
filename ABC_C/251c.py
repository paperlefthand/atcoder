n = int(input())
ss, ts = [], []
for i in range(n):
  s, t = input().split()
  ss.append(s)
  ts.append(int(t))

d = dict()
for s in set(ss):
  d[s] = (-1, -1)

for i in range(n):
  if d[ss[i]][0] == -1:
    d[ss[i]] = (ts[i], i)

score = -1
index = 0
for v in d.values():
  if v[0] > score:
    score, index = v
  
print(index+1)

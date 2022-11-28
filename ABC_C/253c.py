q = int(input())

s_min = 10**9
s_max = 0

s = dict()
s_set = set()

for i in range(q):
  query = input()

  if query[0]=='1':
    x = int(query[2])
    
    if x in s_set:
      s[x] = s[x]+1
    else:
      s_set.add(x)
      s[x] = 1
      s_min = min(x, s_min)
      s_max = max(x, s_max)

  elif query[0]=='2':
    x = int(query[2])
    c = int(query[4])

    if x in s_set:
      if s[x] > c:
        s[x] = s[x]-c 
      else:
        s[x] = 0
        s_set.remove(x)
        s_min = min(s_set)
        s_max = max(s_set)

  else:
    print(s_max - s_min)


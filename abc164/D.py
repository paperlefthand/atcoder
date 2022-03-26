S = input()
N = len(S)
ans = 0

mods = []
for i in range(N):
    mod = int(S[i:]) % 2019
    if mod == 0:
        ans += 1
    mods.append(mod)

print(ans+len(mods)-len(set(mods)))


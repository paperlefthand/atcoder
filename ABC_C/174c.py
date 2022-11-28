#!/usr/bin/env python3

def main(k: int) -> int:

    num = 0
    mod_count = [0]*k

    for i in range(k):
        num = (10*num + 7) % k
        if num==0:
            return (i+1)
        if mod_count[num] == 1:
            return -1
        mod_count[num] += 1
    
    return -1

if __name__ == '__main__':
    K = int(input())
    print(main(K))
#!/usr/bin/env python3

if __name__ == '__main__':
    s1, s2, s3 = input().split()
    s = ''.join([s[0].upper() for s in (s1, s2, s3)])
    print(s)

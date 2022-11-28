#!/usr/bin/env python3

from typing import List

def calculate(nums: List[int], sign: int) -> int:
    """ 正または負の値から始まる列に対し, 
        部分和の列が正負交互になるように必要な手数を算出 
    """
    l = len(nums) # 配列の長さ
    count = 0 # 手順数
    s = nums[0] # sign=1ならs>0, sign=-1ならs<0を前提とする
    
    # 添え字を進めながらその添え字の要素までの部分和sを更新していく
    for i in range(1, l):
        s += nums[i] 
        if sign*s >= 0: 
            # 同一符号が続く or 0なら, 部分和が1 or -1になるように調整 
            count += (1 + abs(s)) # nums[i]を更新
            s = -sign # s = 1 or -1
        sign *= (-1) # 正負判定を切り替える

    return count

def main(nums: List[int]) -> int:

    count = 0
    a = nums[0]

    if a>0:
        count = min(calculate(nums, 1), 1+abs(a)+calculate([-1]+nums[1:], -1))
    elif a<0:
        count = min(calculate(nums, -1), 1+abs(a)+calculate([1]+nums[1:], 1))
    else:
        count = 1 + min(calculate([1]+nums[1:], 1), calculate([-1]+nums[1:], -1))

    return count

if __name__ == '__main__':
    n = int(input())
    nums = [int(a) for a in input().split()]
    count = main(nums)
    print(count)


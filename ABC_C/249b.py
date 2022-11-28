def resolve():
    text = input()
    if text.islower() or text.isupper():
        return "No"
    count = len(text)
    nums = set()
    for s in text:
        nums.add(s)
    
    if count == len(nums):
        return "Yes"
    else:
        return "No"

print(resolve())


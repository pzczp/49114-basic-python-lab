nums = []
while True:
    ipt = input()
    if ipt == 'end':
        break
    nums.append(int(ipt))
print(f"max: {max(nums)}")
print(f"min: {min(nums)}")

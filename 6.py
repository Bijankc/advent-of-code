from functools import cmp_to_key

nums = [43, 2, 57, 72, 523, 22, 8, 778]

def largestNumber(nums):
    nums = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    nums.sort(key=cmp_to_key(compare))

    result = ''.join(nums)
    return '0' if result[0] == '0' else result

print(largestNumber(nums))

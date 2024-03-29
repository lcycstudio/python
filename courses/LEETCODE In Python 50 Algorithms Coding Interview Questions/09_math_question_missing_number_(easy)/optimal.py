def missingNumber(nums: []) -> int:
    n = len(nums)
    current_sum = sum(nums)
    intended_sum = n * (n + 1) / 2
    return int(intended_sum - current_sum)


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))
    print(missingNumber([0, 1]))
    print(missingNumber([1, 2]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 8, 7, 0, 1]))

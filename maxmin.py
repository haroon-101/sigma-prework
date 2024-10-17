def maxmin(nums):
    min = nums[0]
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return [min, max]


if __name__ == "__main__":
    print(maxmin([1,2,3,-4]))
    print(maxmin([100, -100]))
    
def insertion(list_nums):
    for i in range(1, len(list_nums)):  #[54, 43, 3, 11, 0]
        item = list_nums[i]
        i2 = i - 1
        while i2 >= 0 and list_nums[i2] > item:
            list_nums[i2 + 1] = list_nums[i2]
            i2 -= 1
            list_nums[i2 + 1] = item

nums = [54, 43, 3, 11, 0]
insertion(nums)
print(nums)  # Выведет [0, 3, 11, 43, 54]
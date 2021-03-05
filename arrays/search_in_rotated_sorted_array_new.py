def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid-1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid+1
            else:
                end = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search(nums, target))

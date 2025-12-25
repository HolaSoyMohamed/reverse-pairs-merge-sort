def reverse_pairs(nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, cnt_left = merge_sort(arr[:mid])
        right, cnt_right = merge_sort(arr[mid:])

        cnt = cnt_left + cnt_right

        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            cnt += j

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, cnt

    sorted_nums, ans = merge_sort(nums)
    return sorted_nums, ans

user_input = input("Enter numbers separated by space: ")
nums = list(map(int, user_input.strip().split()))

sorted_nums, result = reverse_pairs(nums)
print("Sorted list:", sorted_nums)
print("Number of reverse pairs:", result)
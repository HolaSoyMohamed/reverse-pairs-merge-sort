import time
import random


def reverse_pairs_naive(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count



def reverse_pairs_optimized(nums):
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

    _, ans = merge_sort(nums)
    return ans


def empirical_test(nums):
    nums1 = nums.copy()
    nums2 = nums.copy()

    start = time.time()
    ans1 = reverse_pairs_naive(nums1)
    end = time.time()
    naive_time = end - start

    start = time.time()
    ans2 = reverse_pairs_optimized(nums2)
    end = time.time()
    opt_time = end - start

    return ans1, naive_time, ans2, opt_time


if __name__ == "__main__":
    print("Enter numbers separated by space:")
    nums = list(map(int, input().split()))

    ans1, t1, ans2, t2 = empirical_test(nums)

    print("\nResults:")
    print("Naive Answer:", ans1)
    print("Naive Time:", t1, "seconds")

    print("Optimized Answer:", ans2)
    print("Optimized Time:", t2, "seconds")

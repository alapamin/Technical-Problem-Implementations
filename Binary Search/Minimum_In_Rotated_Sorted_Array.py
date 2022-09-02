from typing import List

def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14

left = 0
right = len(arr) - 1
mid = (left + right) // 2

if arr[mid] == target:
    print(target)

while True:
    if arr[mid] == target:
        print(mid)
    if left == target:
        print(left)
    if right == target:
        print(right)

    
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

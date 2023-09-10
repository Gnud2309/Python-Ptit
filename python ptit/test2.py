def next_permutation(n, x):
    i = n - 2
    while i >= 0 and x[i] >= x[i+1]:
        i -= 1
    if i < 0:
        return None  # Hoán vị cuối cùng
    j = n - 1
    while x[j] <= x[i]:
        j -= 1
    x[i], x[j] = x[j], x[i]
    x[i+1:] = reversed(x[i+1:])
    return x

# Đọc số lượng test
t = int(input())
for _ in range(t):
    # Đọc dữ liệu cho mỗi test
    n = int(input())
    x = list(map(int, input().split()))
    
    # Tìm hoán vị tiếp theo
    next_x = next_permutation(n, x)
    
    # In kết quả
    if next_x is None:
        print("No permutation")
    else:
        print(*next_x)
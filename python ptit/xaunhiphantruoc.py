def previous_binary_string(x):
    n = len(x)
    i = n - 2
    while i >= 0 and x[i:i+2] != '01':
        i -= 1
    if i < 0:
        return None  # Xâu nhị phân đầu tiên
    return x[:i] + '10' + x[i+2:][::-1]

# Đọc số lượng test
t = int(input())

for _ in range(t):
    # Đọc dữ liệu cho mỗi test
    x = input().strip()
    
    # Tìm xâu nhị phân trước đó
    prev_x = previous_binary_string(x)
    
    # In kết quả
    if prev_x is None:
        print("No previous binary string")
    else:
        print(prev_x)
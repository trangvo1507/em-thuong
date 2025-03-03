# Viết function is_prime kiểm tra xem một số có phải số nguyên tố hay không
def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Viết function all_prime trả về danh sách n phần tử,
# giá trị của mỗi phần từ thể hiện stt của nó là số nguyên tố hay không
# VD: n = 16
# KQ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     [F, F, T, T, F, T, F, T, F, F,  F,  T,  F,  T,  F,  F]
def all_prime(n: int) -> list[bool]:
    result = [True for i in range(n)]
    i = 2
    while i * i <= n:
        if result[i]:
            for j in range(i + i, n, i):
                result[j] = False
        i += 1
    return result


# function (Hàm): function(input...) -> output, VD: sqrt(n: float) -> float


# procedure (Thủ tục): procedure(input...), VD: print(s: str)

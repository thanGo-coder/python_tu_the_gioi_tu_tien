# ### **Bài 7: Tính giai thừa**

# - **Mô tả**: Nhập một số nguyên dương `n` và tính giai thừa của nó (giai thừa là tích các số từ 1 đến `n`).
# - **Input**: Một số nguyên dương `n` (ví dụ: 5).
# - **Output**: Giai thừa của `n` (ví dụ: 120, vì 1 * 2 * 3 * 4 * 5 = 120).
# - **Gợi ý**: Dùng vòng lặp `for` từ 1 đến `n`, nhân từng số vào biến kết quả.
N=int(input("nhap N    "))
S=1
for i in range (1,N+1):
    S=S*i
print(S)

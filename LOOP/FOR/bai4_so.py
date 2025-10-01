# ### **Bài 5: In bảng cửu chương**

# - **Mô tả**: Nhập một số nguyên dương `n` và in bảng cửu chương từ 1 đến `n`.
# - **Input**: Một số nguyên dương `n` (ví dụ: 3).
# - **Output**: Bảng cửu chương từ 1 đến `n` (ví dụ:
    
#     ```
#     1x1 = 1
#     1x2 = 2
#     1x3 = 3
#     ...
#     1x10 = 10
#     ....
    
#     2x1 =2
#     ..
#     2x10 = 20
    
#     ```
    
# - **Gợi ý**: Dùng hai vòng lặp `for` lồng nhau: vòng ngoài từ 1 đến `n` (hàng), vòng trong từ 1 đến `n` (cột), in ra phép nhân.
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
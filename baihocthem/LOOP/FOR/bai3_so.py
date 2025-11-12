# ### **Bài 4: Tìm số lớn nhất trong danh sách**

# - **Mô tả**: Nhập số lượng phần tử và danh sách các số nguyên, sau đó tìm số lớn nhất.
# - **Input**: Số lượng phần tử `n`, rồi `n` số nguyên (ví dụ: 5, rồi 3 1 4 1 5).
# - **Output**: Số lớn nhất (ví dụ: 5).
# - **Gợi ý**: Khởi tạo biến `max_value` bằng số đầu tiên, dùng vòng lặp `for` để so sánh từng số với `max_value`, nếu lớn hơn thì cập nhật lại `max_value`.
max_value=-99999999999999999
a=int(input("nhap      "))
   
for i in range(a):
    temp=int(input("nhap i     "))
    if temp > max_value:
        max_value=temp
print(max_value)





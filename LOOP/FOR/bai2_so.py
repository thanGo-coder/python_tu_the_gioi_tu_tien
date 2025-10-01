# ### **Bài tập 1: Đếm số lượng số chẵn và lẻ từ 1 đến n**

# - **Mô tả**:
# Nhập một số nguyên dương n và đếm số lượng số chẵn và số lẻ từ 1 đến n.
# - **Input**:
# Một số nguyên dương n (ví dụ: 10).
# - **Output**:
# Số lượng số chẵn và số lẻ từ 1 đến n (ví dụ: "Số chẵn: 5, Số lẻ: 5")
S=0
n=int(input("nhap N         "))
for i in range(1,n+1):
    if i%2==0:
        S=S+i
print (S)



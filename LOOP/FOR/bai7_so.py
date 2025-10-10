# ### **Bài 8: Đảo ngược danh sách**

# - **Mô tả**: Nhập số lượng phần tử và danh sách các số nguyên, sau đó in danh sách theo thứ tự đảo ngược.
# - **Input**: Số lượng phần tử `n`, rồi `n` số nguyên (ví dụ: 4, rồi 1 2 3 4).
# - **Output**: Danh sách đảo ngược (ví dụ: 4 3 2 1).
# # - **Gợi ý**: Lưu danh sách vào một biến, dùng vòng lặp `for` từ chỉ số cuối về đầu để in ra từng phần tử.
N=int(input("nhap skibiditoile        "))
penguin=[]
for i in range(N):
    temp=int(input(       ))
    penguin.append(temp)
print(penguin)
# ds =[1,2,3,4]

for i in range(len(penguin)-1,-1,-1):
    print(penguin[i])





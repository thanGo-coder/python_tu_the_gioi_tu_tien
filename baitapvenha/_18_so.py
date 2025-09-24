# ### **Bài 18: Tính thuế thu nhập**

# - **Mô tả**:
    
#     Nhập lương tháng, tính thuế:
    
#     - <= 5 triệu: 5%
#     - <= 10 triệu: 10%
#     - 10 triệu: 15%
# - **Input**:
    
#     `luong = 12_000_000`
    
# - **Output**:
    
#     `"Thuế phải đóng: 1,800,000"`


luong=int(input("nhapluongcuaban       "))
thue=int(input("nhapthuecuaban     "))
nop=(luong/100*thue)
print(nop)
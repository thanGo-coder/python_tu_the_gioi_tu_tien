# ### **Bài 19: Xếp hạng sao đánh giá sản phẩm**

# - **Mô tả**:
    
#     Nhập số sao (1–5), in ra đánh giá:
    
#     - 5: Xuất sắc
#     - 4: Tốt
#     - 3: Trung bình
#     - 2: Kém
#     - 1: Rất kém
sao=int(input("nhapsosao      "))
if sao==5:
    print("xuatsac")
elif sao==4:
    print("tot")
elif sao==3:
    print("trungbinh")
elif sao==2:
    print("kem")
else:
    print("ratkem")
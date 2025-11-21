# ### **Bài 2: Kiểm tra số chẵn/lẻ**

# - **Mô tả:** Viết một hàm nhận vào một số nguyên và trả về chuỗi "Chẵn" nếu số đó là số chẵn, ngược lại trả về "Lẻ".
# - **Signature:**
    
#     **Python**
    
#     `def kiem_tra_chan_le(so: int) -> str:
#         pass`
def kiem_tra_chan_le (a)->str:
    if a%2==0:
        print('chan')
    else: print("le")
    

a=int(input(  ))
end=kiem_tra_chan_le(a)
